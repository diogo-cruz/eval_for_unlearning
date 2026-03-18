#!/usr/bin/env python3
"""
Compile all WMDP benchmark evaluation data from multiple git branches
into clean CSV datasets.

Outputs:
  1. wmdp_aggregated_results.csv  - Model x task level accuracy
  2. wmdp_per_question_results.csv - Per-question binary responses
  3. wmdp_response_matrix.csv     - Model x question binary matrix

Data sources:
  - lm_eval_prompting branch: .bin/eval_results.csv (aggregated)
  - evals_040425 branch: output/wmdp/*/samples_*.jsonl, output/wmdp_rephrased/*/samples_*.jsonl,
                          results/*/samples_*.jsonl, results_multiturn/*/samples_*.jsonl
  - erasure branch: results/wmdp_*_run_results_.json, run_results_metadata.json
"""

import csv
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

REPO_DIR = "/home/dcruz/eval_for_unlearning"
OUT_DIR = "/home/dcruz/eval_for_unlearning/compiled_data"


def run_git(cmd):
    """Run a git command in the repo directory."""
    result = subprocess.run(
        cmd, shell=True, cwd=REPO_DIR, capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"WARNING: git command failed: {cmd}")
        print(f"  stderr: {result.stderr.strip()}")
    return result


def checkout(branch):
    """Checkout a branch."""
    run_git(f"git checkout {branch}")


# ============================================================
# Step 1: Aggregated results from lm_eval_prompting branch
# ============================================================
def collect_aggregated_from_lm_eval_prompting():
    """Read .bin/eval_results.csv from lm_eval_prompting branch."""
    print("=== Step 1: Collecting aggregated results from lm_eval_prompting ===")
    checkout("lm_eval_prompting")

    rows = []
    csv_path = os.path.join(REPO_DIR, ".bin", "eval_results.csv")
    with open(csv_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            model = row["model"].strip()
            task = row["task"].strip()
            acc_str = row["accuracy"].strip()
            stderr_str = row.get("stderr", "").strip()

            try:
                accuracy = float(acc_str)
            except ValueError:
                continue

            stderr = None
            if stderr_str and stderr_str != "N/A" and stderr_str != "":
                try:
                    stderr = float(stderr_str)
                except ValueError:
                    stderr = None

            rows.append({
                "model": model,
                "task": task,
                "accuracy": accuracy,
                "stderr": stderr,
                "source_branch": "lm_eval_prompting",
                "n_questions": None,  # will fill later if possible
                "eval_setting": "0-shot",
            })

    print(f"  Found {len(rows)} aggregated results")
    return rows


# ============================================================
# Step 2: Per-question data from evals_040425 branch
# ============================================================
def extract_task_from_filename(filename):
    """Extract task name from a samples_TASKNAME_TIMESTAMP.jsonl filename."""
    basename = os.path.basename(filename)
    # Pattern: samples_TASKNAME_TIMESTAMP.jsonl
    # TIMESTAMP is either "2025-04-01 05:58:13.639151" or "2025-04-23T02-31-20.877785"
    m = re.match(r"samples_(.+?)_(\d{4}-\d{2}-\d{2}[T ])", basename)
    if m:
        return m.group(1)
    return None


def parse_lm_eval_samples(filepath, model_name, task_name, eval_setting="0-shot"):
    """Parse an lm_eval samples JSONL file into per-question records."""
    records = []
    try:
        with open(filepath, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    item = json.loads(line)
                except json.JSONDecodeError:
                    continue

                doc_id = item.get("doc_id")
                doc = item.get("doc", {})
                target = item.get("target")
                acc = item.get("acc")

                question_text = doc.get("question", "")
                choices = doc.get("choices", [])
                correct_answer_idx = doc.get("answer")

                # Determine predicted answer from filtered_resps
                filtered_resps = item.get("filtered_resps", [])
                if filtered_resps:
                    # Each element is [loglikelihood, is_top]
                    # Find the index with highest loglikelihood
                    # Note: values can be strings in some files, so convert to float
                    lls = []
                    for resp in filtered_resps:
                        if isinstance(resp, list) and len(resp) >= 1:
                            try:
                                lls.append(float(resp[0]))
                            except (ValueError, TypeError):
                                lls.append(float("-inf"))
                        else:
                            lls.append(float("-inf"))
                    predicted_idx = lls.index(max(lls))
                else:
                    predicted_idx = None

                # Map indices to letters
                idx_to_letter = {0: "A", 1: "B", 2: "C", 3: "D"}
                correct_letter = idx_to_letter.get(correct_answer_idx, str(correct_answer_idx))
                predicted_letter = idx_to_letter.get(predicted_idx) if predicted_idx is not None else None

                # Use acc field from lm_eval (ground truth) when available;
                # fall back to comparing predicted vs correct index
                if acc is not None:
                    is_correct = int(float(acc))
                elif predicted_idx is not None and correct_answer_idx is not None:
                    is_correct = 1 if predicted_idx == correct_answer_idx else 0
                else:
                    is_correct = 0

                records.append({
                    "model": model_name,
                    "task": task_name,
                    "question_id": doc_id,
                    "question_text": question_text,
                    "correct_answer": correct_letter,
                    "predicted_answer": predicted_letter,
                    "is_correct": is_correct,
                    "eval_setting": eval_setting,
                    "source_branch": "evals_040425",
                })
    except Exception as e:
        print(f"  WARNING: Error parsing {filepath}: {e}")

    return records


def collect_per_question_from_evals_040425():
    """Collect per-question data from evals_040425 branch."""
    print("=== Step 2: Collecting per-question data from evals_040425 ===")
    checkout("evals_040425")

    all_records = []
    all_aggregate = []

    # --- output/wmdp/ ---
    wmdp_dir = os.path.join(REPO_DIR, "output", "wmdp")
    if os.path.isdir(wmdp_dir):
        for model_dir_name in sorted(os.listdir(wmdp_dir)):
            model_dir = os.path.join(wmdp_dir, model_dir_name)
            if not os.path.isdir(model_dir):
                continue
            for fn in sorted(os.listdir(model_dir)):
                if fn.startswith("samples_") and fn.endswith(".jsonl"):
                    task_name = extract_task_from_filename(fn)
                    if task_name is None:
                        continue
                    fp = os.path.join(model_dir, fn)
                    records = parse_lm_eval_samples(fp, model_dir_name, task_name, "0-shot")
                    all_records.extend(records)

    # --- output/wmdp_rephrased/ ---
    rephrased_dir = os.path.join(REPO_DIR, "output", "wmdp_rephrased")
    if os.path.isdir(rephrased_dir):
        for model_dir_name in sorted(os.listdir(rephrased_dir)):
            model_dir = os.path.join(rephrased_dir, model_dir_name)
            if not os.path.isdir(model_dir):
                continue
            for fn in sorted(os.listdir(model_dir)):
                if fn.startswith("samples_") and fn.endswith(".jsonl"):
                    task_name = extract_task_from_filename(fn)
                    if task_name is None:
                        continue
                    fp = os.path.join(model_dir, fn)
                    records = parse_lm_eval_samples(fp, model_dir_name, task_name, "0-shot")
                    all_records.extend(records)

    # --- results/ (non-shot subdirs) ---
    results_dir = os.path.join(REPO_DIR, "results")
    if os.path.isdir(results_dir):
        for model_dir_name in sorted(os.listdir(results_dir)):
            model_dir = os.path.join(results_dir, model_dir_name)
            if not os.path.isdir(model_dir):
                continue

            # Direct sample files (0-shot default)
            for fn in sorted(os.listdir(model_dir)):
                if fn.startswith("samples_") and fn.endswith(".jsonl"):
                    task_name = extract_task_from_filename(fn)
                    if task_name is None:
                        continue
                    fp = os.path.join(model_dir, fn)
                    records = parse_lm_eval_samples(fp, model_dir_name, task_name, "0-shot")
                    all_records.extend(records)

            # N-shot subdirectories
            for subdir in sorted(os.listdir(model_dir)):
                subdir_path = os.path.join(model_dir, subdir)
                if not os.path.isdir(subdir_path):
                    continue
                shot_match = re.match(r"(\d+)-shot", subdir)
                if shot_match:
                    n_shot = shot_match.group(0)
                    for fn in sorted(os.listdir(subdir_path)):
                        if fn.startswith("samples_") and fn.endswith(".jsonl"):
                            task_name = extract_task_from_filename(fn)
                            if task_name is None:
                                continue
                            fp = os.path.join(subdir_path, fn)
                            records = parse_lm_eval_samples(fp, model_dir_name, task_name, n_shot)
                            all_records.extend(records)

    # --- results_multiturn/ ---
    multiturn_dir = os.path.join(REPO_DIR, "results_multiturn")
    if os.path.isdir(multiturn_dir):
        for shot_dir in sorted(os.listdir(multiturn_dir)):
            shot_path = os.path.join(multiturn_dir, shot_dir)
            if not os.path.isdir(shot_path):
                continue
            shot_match = re.match(r"(\d+)-shot", shot_dir)
            n_shot = shot_match.group(0) if shot_match else shot_dir
            eval_setting = f"multiturn_{n_shot}"

            for model_dir_name in sorted(os.listdir(shot_path)):
                model_dir = os.path.join(shot_path, model_dir_name)
                if not os.path.isdir(model_dir):
                    continue
                for fn in sorted(os.listdir(model_dir)):
                    if fn.startswith("samples_") and fn.endswith(".jsonl"):
                        task_name = extract_task_from_filename(fn)
                        if task_name is None:
                            continue
                        fp = os.path.join(model_dir, fn)
                        records = parse_lm_eval_samples(fp, model_dir_name, task_name, eval_setting)
                        all_records.extend(records)

    # --- Aggregate results from results_*.json files ---
    if os.path.isdir(results_dir):
        for model_dir_name in sorted(os.listdir(results_dir)):
            model_dir = os.path.join(results_dir, model_dir_name)
            if not os.path.isdir(model_dir):
                continue

            def process_results_json(fp, model_name, eval_setting):
                """Extract aggregate results from an lm_eval results JSON."""
                agg = []
                try:
                    with open(fp) as f:
                        data = json.load(f)
                    results = data.get("results", {})
                    for task_name, task_results in results.items():
                        acc = task_results.get("acc,none")
                        stderr = task_results.get("acc_stderr,none")
                        n_samples = task_results.get("alias")  # sometimes stored here
                        if acc is not None:
                            agg.append({
                                "model": model_name,
                                "task": task_name,
                                "accuracy": acc,
                                "stderr": stderr,
                                "source_branch": "evals_040425",
                                "n_questions": None,
                                "eval_setting": eval_setting,
                            })
                except Exception as e:
                    print(f"  WARNING: Error parsing results JSON {fp}: {e}")
                return agg

            for fn in sorted(os.listdir(model_dir)):
                if fn.startswith("results_") and fn.endswith(".json"):
                    fp = os.path.join(model_dir, fn)
                    agg = process_results_json(fp, model_dir_name, "0-shot")
                    all_aggregate.extend(agg)

            for subdir in sorted(os.listdir(model_dir)):
                subdir_path = os.path.join(model_dir, subdir)
                if not os.path.isdir(subdir_path):
                    continue
                shot_match = re.match(r"(\d+)-shot", subdir)
                if shot_match:
                    n_shot = shot_match.group(0)
                    for fn in sorted(os.listdir(subdir_path)):
                        if fn.startswith("results_") and fn.endswith(".json"):
                            fp = os.path.join(subdir_path, fn)
                            agg = process_results_json(fp, model_dir_name, n_shot)
                            all_aggregate.extend(agg)

    print(f"  Found {len(all_records)} per-question records from evals_040425")
    print(f"  Found {len(all_aggregate)} aggregate results from results JSON files")
    return all_records, all_aggregate


# ============================================================
# Step 3: Per-question data from erasure branch
# ============================================================
def collect_per_question_from_erasure():
    """Collect per-question data from erasure branch."""
    print("=== Step 3: Collecting per-question data from erasure branch ===")
    checkout("erasure")

    all_records = []
    all_aggregate = []
    results_dir = os.path.join(REPO_DIR, "results")

    # We need the question text from run_results_metadata.json
    metadata_path = os.path.join(REPO_DIR, "run_results_metadata.json")
    rephrasing_metadata_path = os.path.join(REPO_DIR, "run_results_metadata_rephrasing.json")

    # Load question data (shared across models)
    questions_by_task = {}
    if os.path.exists(metadata_path):
        with open(metadata_path) as f:
            meta = json.load(f)
        for task_key, task_data in meta.items():
            if "questions" in task_data:
                questions_by_task[task_key] = task_data["questions"]

    if os.path.exists(rephrasing_metadata_path):
        with open(rephrasing_metadata_path) as f:
            meta_reph = json.load(f)
        for reph_key, reph_data in meta_reph.items():
            for task_key, task_data in reph_data.items():
                if "questions" in task_data:
                    composite_key = f"{reph_key}__{task_key}"
                    questions_by_task[composite_key] = task_data["questions"]

    # Map erasure filenames to (model, eval_setting, task_type)
    # Pattern: wmdp_0_shot_MODEL_run_results_.json
    erasure_files = []
    for fn in sorted(os.listdir(results_dir)):
        if not fn.endswith(".json"):
            continue
        # Skip breakpoint files (duplicates of results)
        if "breakpoint" in fn:
            continue
        # Skip metadata files
        if "metadata" in fn:
            continue

        fp = os.path.join(results_dir, fn)

        # Parse filename
        # wmdp_0_shot_zephyr_rmu_run_results_.json
        # wmdp_0_shot_zephyr_7b_beta_run_results_.json
        # wmdp_0_shot_zephyr_rmu_run_results__rephrased.json
        # wmdp_0_shot_zephyr_rmu_run_results__rephrasing.json
        # mmlu_0_shot_zephyr_7b_beta_run_results_.json
        # tinyMMLU_0_shot_zephyr_rmu_run_results_.json
        # run_results__anatomydev.json

        # Identify benchmark
        if fn.startswith("wmdp_"):
            m = re.match(r"wmdp_(\d+)_shot_(.+?)_run_results_(?:_(.+))?\.json", fn)
            if m:
                n_shot = f"{m.group(1)}-shot"
                model_name = m.group(2)
                suffix = m.group(3)  # "rephrased", "rephrasing", or None
                erasure_files.append((fp, fn, model_name, n_shot, "wmdp", suffix))
        elif fn.startswith("mmlu_"):
            m = re.match(r"mmlu_(\d+)_shot_(.+?)_run_results_(?:_(.+))?\.json", fn)
            if m:
                n_shot = f"{m.group(1)}-shot"
                model_name = m.group(2)
                suffix = m.group(3)
                erasure_files.append((fp, fn, model_name, n_shot, "mmlu", suffix))
        elif fn.startswith("tinyMMLU_"):
            m = re.match(r"tinyMMLU_(\d+)_shot_(.+?)_run_results_(?:_(.+))?\.json", fn)
            if m:
                n_shot = f"{m.group(1)}-shot"
                model_name = m.group(2)
                suffix = m.group(3)
                erasure_files.append((fp, fn, model_name, n_shot, "tinyMMLU", suffix))
        elif fn.startswith("run_results__"):
            # These appear to be MMLU subtask results from a specific model
            m = re.match(r"run_results__(.+)\.json", fn)
            if m:
                subtask = m.group(1)
                erasure_files.append((fp, fn, "unknown_model", "0-shot", f"mmlu_{subtask}", None))

    idx_to_letter = {0: "A", 1: "B", 2: "C", 3: "D"}

    for fp, fn, model_name, eval_setting, benchmark, suffix in erasure_files:
        try:
            with open(fp) as f:
                data = json.load(f)
        except Exception as e:
            print(f"  WARNING: Failed to load {fn}: {e}")
            continue

        for task_key, task_data in data.items():
            if not isinstance(task_data, dict):
                continue

            pred_answers = task_data.get("pred_answers", [])
            gold_answers = task_data.get("gold_answers", [])

            if not pred_answers:
                # Rephrasing files may have nested structure
                if isinstance(task_data, dict):
                    for sub_key, sub_data in task_data.items():
                        if isinstance(sub_data, dict) and "pred_answers" in sub_data:
                            sub_preds = sub_data.get("pred_answers", [])
                            sub_golds = sub_data.get("gold_answers", [])
                            if sub_preds:
                                # Construct task name
                                if suffix:
                                    task_name = f"{benchmark}_{suffix}_{task_key}_{sub_key}"
                                else:
                                    task_name = f"{benchmark}_{task_key}_{sub_key}"

                                for i, (pred, gold) in enumerate(zip(sub_preds, sub_golds)):
                                    pred_clean = pred.strip() if isinstance(pred, str) else str(pred)
                                    gold_clean = gold.strip() if isinstance(gold, str) else str(gold)
                                    is_correct = 1 if pred_clean == gold_clean else 0

                                    all_records.append({
                                        "model": model_name,
                                        "task": task_name,
                                        "question_id": i,
                                        "question_text": "",
                                        "correct_answer": gold_clean,
                                        "predicted_answer": pred_clean,
                                        "is_correct": is_correct,
                                        "eval_setting": eval_setting,
                                        "source_branch": "erasure",
                                    })
                continue

            # Construct task name
            if suffix:
                task_name = f"{benchmark}_{suffix}_{task_key}"
            else:
                task_name = f"{benchmark}_{task_key}"

            # Get questions if available
            questions = questions_by_task.get(task_key, [])

            # Compute per-question results
            for i, (pred, gold) in enumerate(zip(pred_answers, gold_answers)):
                pred_clean = pred.strip() if isinstance(pred, str) else str(pred)
                gold_clean = gold.strip() if isinstance(gold, str) else str(gold)
                is_correct = 1 if pred_clean == gold_clean else 0

                # Get question text if available
                q_text = ""
                correct_letter = gold_clean
                if i < len(questions):
                    q = questions[i]
                    q_text = q.get("question", "")
                    answer_idx = q.get("answer")
                    if answer_idx is not None:
                        correct_letter = idx_to_letter.get(answer_idx, gold_clean)

                all_records.append({
                    "model": model_name,
                    "task": task_name,
                    "question_id": i,
                    "question_text": q_text,
                    "correct_answer": correct_letter if correct_letter else gold_clean,
                    "predicted_answer": pred_clean,
                    "is_correct": is_correct,
                    "eval_setting": eval_setting,
                    "source_branch": "erasure",
                })

            # Aggregate
            n_correct = sum(1 for p, g in zip(pred_answers, gold_answers)
                           if p.strip() == g.strip())
            n_total = len(pred_answers)
            all_aggregate.append({
                "model": model_name,
                "task": task_name,
                "accuracy": n_correct / n_total if n_total > 0 else 0,
                "stderr": None,
                "source_branch": "erasure",
                "n_questions": n_total,
                "eval_setting": eval_setting,
            })

    print(f"  Found {len(all_records)} per-question records from erasure")
    print(f"  Found {len(all_aggregate)} aggregate results from erasure")
    return all_records, all_aggregate


# ============================================================
# Step 4: Deduplicate and compile
# ============================================================
def deduplicate_per_question(records):
    """Deduplicate per-question records.
    When same (model, task, question_id, eval_setting) appears multiple times,
    keep the latest one (last in the list, which comes from files sorted by date).
    """
    seen = {}
    for r in records:
        key = (r["model"], r["task"], r["question_id"], r["eval_setting"])
        seen[key] = r  # last one wins
    deduped = list(seen.values())
    print(f"  Deduplicated {len(records)} -> {len(deduped)} per-question records")
    return deduped


def deduplicate_aggregate(rows):
    """Deduplicate aggregate results.
    When same (model, task, eval_setting) appears, keep the one with more info.
    """
    seen = {}
    for r in rows:
        key = (r["model"], r["task"], r["eval_setting"])
        if key in seen:
            existing = seen[key]
            # Prefer the one with n_questions or stderr
            if r.get("n_questions") and not existing.get("n_questions"):
                seen[key] = r
            elif r.get("stderr") and not existing.get("stderr"):
                seen[key] = r
        else:
            seen[key] = r
    deduped = list(seen.values())
    print(f"  Deduplicated {len(rows)} -> {len(deduped)} aggregate results")
    return deduped


def compute_aggregate_from_per_question(per_question_records):
    """Compute aggregate accuracy from per-question data."""
    groups = defaultdict(list)
    for r in per_question_records:
        key = (r["model"], r["task"], r["eval_setting"], r["source_branch"])
        groups[key].append(r["is_correct"])

    aggregate = []
    for (model, task, eval_setting, source_branch), correctness in groups.items():
        n = len(correctness)
        acc = sum(correctness) / n
        # Binomial stderr
        stderr = (acc * (1 - acc) / n) ** 0.5 if n > 0 else None
        aggregate.append({
            "model": model,
            "task": task,
            "accuracy": acc,
            "stderr": stderr,
            "source_branch": source_branch,
            "n_questions": n,
            "eval_setting": eval_setting,
        })
    return aggregate


def build_response_matrix(per_question_records):
    """Build model x question binary response matrix.
    Only include 0-shot, non-multiturn, wmdp_bio task (original, not rephrased) records.
    Use task::question_id as column identifier.
    """
    # Filter to standard eval setting
    filtered = [r for r in per_question_records
                if r["eval_setting"] == "0-shot"
                and r["task"].startswith("wmdp_bio")
                and "rephrased" not in r["task"]
                and "renellm" not in r["task"]
                and "tinyMMLU" not in r["task"]]

    # Group by model
    matrix = defaultdict(dict)
    all_questions = set()
    for r in filtered:
        q_id = f"{r['task']}::{r['question_id']}"
        matrix[r["model"]][q_id] = r["is_correct"]
        all_questions.add(q_id)

    return matrix, sorted(all_questions)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    # Collect from all branches
    agg_lm_eval = collect_aggregated_from_lm_eval_prompting()
    per_q_evals, agg_evals = collect_per_question_from_evals_040425()
    per_q_erasure, agg_erasure = collect_per_question_from_erasure()

    # Switch back to main
    checkout("main")

    # ---- Per-question results ----
    print("\n=== Step 4: Compiling outputs ===")
    all_per_question = per_q_evals + per_q_erasure
    all_per_question = deduplicate_per_question(all_per_question)

    # Sort
    all_per_question.sort(key=lambda r: (r["model"], r["task"], r["eval_setting"], r["question_id"]))

    per_q_path = os.path.join(OUT_DIR, "wmdp_per_question_results.csv")
    with open(per_q_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "model", "task", "question_id", "question_text",
            "correct_answer", "predicted_answer", "is_correct",
            "eval_setting", "source_branch"
        ])
        writer.writeheader()
        writer.writerows(all_per_question)
    print(f"  Wrote {len(all_per_question)} rows to {per_q_path}")

    # ---- Aggregated results ----
    # Combine all sources + compute from per-question
    computed_agg = compute_aggregate_from_per_question(all_per_question)

    all_aggregate = agg_lm_eval + agg_evals + agg_erasure + computed_agg
    all_aggregate = deduplicate_aggregate(all_aggregate)
    all_aggregate.sort(key=lambda r: (r["model"], r["task"], r["eval_setting"]))

    # Fill n_questions from per-question data where missing
    pq_counts = defaultdict(int)
    for r in all_per_question:
        key = (r["model"], r["task"], r["eval_setting"])
        pq_counts[key] += 1

    for row in all_aggregate:
        if row["n_questions"] is None:
            key = (row["model"], row["task"], row["eval_setting"])
            if key in pq_counts:
                row["n_questions"] = pq_counts[key]

    agg_path = os.path.join(OUT_DIR, "wmdp_aggregated_results.csv")
    with open(agg_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "model", "task", "accuracy", "stderr",
            "source_branch", "n_questions", "eval_setting"
        ])
        writer.writeheader()
        for row in all_aggregate:
            row_out = dict(row)
            if row_out["stderr"] is not None:
                row_out["stderr"] = f"{row_out['stderr']:.10f}"
            else:
                row_out["stderr"] = ""
            row_out["accuracy"] = f"{row_out['accuracy']:.10f}"
            if row_out["n_questions"] is None:
                row_out["n_questions"] = ""
            writer.writerows([row_out])
    print(f"  Wrote {len(all_aggregate)} rows to {agg_path}")

    # ---- Response matrix ----
    matrix, question_ids = build_response_matrix(all_per_question)
    matrix_path = os.path.join(OUT_DIR, "wmdp_response_matrix.csv")

    if question_ids:
        with open(matrix_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["model"] + question_ids)
            for model_name in sorted(matrix.keys()):
                row = [model_name]
                for q_id in question_ids:
                    val = matrix[model_name].get(q_id, "")
                    row.append(val)
                writer.writerow(row)
        n_models = len(matrix)
        n_questions = len(question_ids)
        print(f"  Wrote {n_models} x {n_questions} response matrix to {matrix_path}")
    else:
        print("  WARNING: No data for response matrix (no 0-shot wmdp_bio records)")

    # ---- Summary stats for report ----
    print("\n=== Summary Statistics ===")

    # Unique models and tasks
    models_pq = set(r["model"] for r in all_per_question)
    tasks_pq = set(r["task"] for r in all_per_question)
    print(f"  Per-question: {len(models_pq)} models, {len(tasks_pq)} tasks")

    models_agg = set(r["model"] for r in all_aggregate)
    tasks_agg = set(r["task"] for r in all_aggregate)
    print(f"  Aggregated: {len(models_agg)} models, {len(tasks_agg)} tasks")

    # By source
    for branch in ["lm_eval_prompting", "evals_040425", "erasure"]:
        agg_count = sum(1 for r in all_aggregate if r["source_branch"] == branch)
        pq_count = sum(1 for r in all_per_question if r["source_branch"] == branch)
        print(f"  {branch}: {agg_count} agg rows, {pq_count} per-question rows")

    # By eval setting
    settings = set(r["eval_setting"] for r in all_per_question)
    print(f"  Eval settings: {sorted(settings)}")

    if question_ids:
        print(f"  Response matrix: {len(matrix)} models x {len(question_ids)} questions")

    # Return stats for report generation
    return {
        "n_per_question": len(all_per_question),
        "n_aggregate": len(all_aggregate),
        "models_pq": sorted(models_pq),
        "tasks_pq": sorted(tasks_pq),
        "models_agg": sorted(models_agg),
        "tasks_agg": sorted(tasks_agg),
        "n_matrix_models": len(matrix) if question_ids else 0,
        "n_matrix_questions": len(question_ids) if question_ids else 0,
        "settings": sorted(settings),
        "branches": ["lm_eval_prompting", "evals_040425", "erasure"],
    }


if __name__ == "__main__":
    stats = main()

    # Generate report
    report_path = os.path.join(OUT_DIR, "WMDP_DATA_REPORT.md")
    with open(report_path, "w") as f:
        f.write("# WMDP Data Compilation Report\n\n")
        f.write(f"Generated: 2026-03-18\n\n")

        f.write("## Overview\n\n")
        f.write("This dataset compiles WMDP (Weapons of Mass Destruction Proxy) benchmark evaluation data\n")
        f.write("from multiple branches of the `eval_for_unlearning` repository.\n\n")

        f.write("## Output Files\n\n")
        f.write("### 1. `wmdp_aggregated_results.csv`\n\n")
        f.write(f"- **Rows**: {stats['n_aggregate']} (model x task x eval_setting combinations)\n")
        f.write(f"- **Models**: {len(stats['models_agg'])}\n")
        f.write(f"- **Tasks**: {len(stats['tasks_agg'])}\n")
        f.write("- **Columns**: model, task, accuracy, stderr, source_branch, n_questions, eval_setting\n\n")

        f.write("### 2. `wmdp_per_question_results.csv`\n\n")
        f.write(f"- **Rows**: {stats['n_per_question']} (individual question responses)\n")
        f.write(f"- **Models**: {len(stats['models_pq'])}\n")
        f.write(f"- **Tasks**: {len(stats['tasks_pq'])}\n")
        f.write("- **Columns**: model, task, question_id, question_text, correct_answer, predicted_answer, is_correct, eval_setting, source_branch\n\n")

        f.write("### 3. `wmdp_response_matrix.csv`\n\n")
        f.write(f"- **Shape**: {stats['n_matrix_models']} models x {stats['n_matrix_questions']} questions\n")
        f.write("- **Filter**: 0-shot, wmdp_bio only (no rephrased/translated variants)\n")
        f.write("- **Values**: 1 (correct) or 0 (incorrect), empty if not evaluated\n\n")

        f.write("## Data Sources\n\n")
        f.write("| Branch | Description | Data Type |\n")
        f.write("|--------|-------------|----------|\n")
        f.write("| `lm_eval_prompting` | `.bin/eval_results.csv` | Aggregated accuracy per model x task |\n")
        f.write("| `evals_040425` | `output/wmdp/*/samples_*.jsonl`, `results/*/samples_*.jsonl`, `results_multiturn/*/samples_*.jsonl` | Per-question log-likelihood responses |\n")
        f.write("| `erasure` | `results/wmdp_*_run_results_.json`, `run_results_metadata.json` | Per-question pred vs gold answers |\n\n")

        f.write("## Eval Settings\n\n")
        for s in stats["settings"]:
            f.write(f"- `{s}`\n")
        f.write("\n")

        f.write("## Models (per-question data)\n\n")
        for m in stats["models_pq"]:
            f.write(f"- `{m}`\n")
        f.write("\n")

        f.write("## Tasks (per-question data)\n\n")
        for t in stats["tasks_pq"]:
            f.write(f"- `{t}`\n")
        f.write("\n")

        f.write("## Deduplication\n\n")
        f.write("When the same model x task x question_id x eval_setting appears in multiple files,\n")
        f.write("the latest file (by sort order, typically most recent timestamp) is kept.\n\n")
        f.write("For aggregated results, when the same model x task x eval_setting appears from\n")
        f.write("multiple sources, preference is given to entries with n_questions or stderr information.\n\n")

        f.write("## Notes\n\n")
        f.write("- Erasure branch prediction answers include newlines/empty strings for questions the model refused to answer.\n")
        f.write("- Response matrix only includes wmdp_bio (original, not rephrased) to avoid inflating the matrix with correlated variants.\n")
        f.write("- Some models appear under different naming conventions across branches (e.g., `cais__Zephyr_RMU` vs `Zephyr_RMU`).\n")
        f.write("- The `question_text` field may be empty for some erasure branch records where question metadata was not available.\n")

    print(f"\n  Wrote report to {report_path}")
    print("\nDone!")
