import argparse
import json
import os
from os import path, sys
from pathlib import Path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import pandas as pd
from common.utils import gen_prompt, load, make_inference
from wmdp_utils import TASKS, format_wmdp_example


ROOT_DIR = "erasure_results"
Path(ROOT_DIR).mkdir(parents=True, exist_ok=True)


def main(args):

    run_results = {}

    if args.dev_task == "":
        output_breakpoint_name = f"{ROOT_DIR}/run_breakpoint_{args.extra_info}.json"
        output_filename = f"{ROOT_DIR}/run_results_{args.extra_info}.json"
    else:
        output_breakpoint_name = f"{ROOT_DIR}/run_breakpoint_{args.extra_info}_{args.dev_task}.json"
        output_filename = f"{ROOT_DIR}/run_results_{args.extra_info}_{args.dev_task}.json"
    if os.path.isfile(output_breakpoint_name):
        run_results = json.load(open(output_breakpoint_name))

    model, tokenizer = load(args.ckpt_dir, args.peft_model, args.tokenizer)

    generate_results_for_prompt(
        args,
        model,
        tokenizer,
        run_results,
        output_breakpoint_name
    )

    with open(output_filename, "w") as f:
        json.dump(run_results, f, ensure_ascii=False, indent=2)


def generate_results_for_prompt(
    args, model, tokenizer, run_results, output_breakpoint_name
):

    def load_df():

        return pd.read_csv(
            os.path.join(args.MMLU_dir, 'dev', args.dev_task + "_dev.csv"), header=None
        )[: args.ntrain]

    # def load_json(task):
    #     f = open(os.path.join(args.data_dir, task + '.json'))
    #     return json.load(f)

    def load_json(task):
        res = []
        with open(os.path.join(args.data_dir, task + '.json'), "r") as f:
            for line in f:
                line = json.loads(line)
                res.append(line)
        return res

    for task in TASKS:
        if (
            task in run_results
        ):
            print("Skipping %s ..." % task)
            continue
        print("Testing %s ..." % task)

        prompts = []
        labels = []

        test_data = load_json(task)
        dev_df = load_df() if args.dev_task != "" else None

        questions = [] 
        for question in test_data:

            k = args.ntrain
            prompt_end = format_wmdp_example(question)

            train_prompt = gen_prompt(
                dev_df, k
            ) if args.dev_task != "" else ""

            prompt = args.system_prompt + train_prompt + prompt_end

            label = chr(65 + question['answer'])

            prompts.append(prompt)
            labels.append(label)
            questions.append(question)

        pred_answers = make_inference(
            model, tokenizer, prompts
        )

        run_results[task] = {
            "questions": questions, "pred_answers": pred_answers, "gold_answers": labels}
        json.dump(run_results, open(output_breakpoint_name, "w"))


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--ckpt_dir", type=str, help="Path to the model")
    parser.add_argument("--peft_model", action="store_true",
                        help="Whether the model is a PEFT model")
    parser.add_argument("--data_dir", type=str, help="Path to wmdp dataset")
    parser.add_argument("--MMLU_dir", type=str,
                        help="Path to MMLU dataset for n-shot prompting")
    parser.add_argument("--extra_info", type=str, default="")
    parser.add_argument("--ntrain", type=int, default=0,
                        help="Number of examples to use for n-shot prompting")
    parser.add_argument("--tokenizer", type=str,
                        default="HuggingFaceH4/zephyr-7b-beta")
    parser.add_argument("--dev_task", type=str, default="",
                        help="MMLU task to be used for n-shot prompting (e.g. college_chemistry)")
    parser.add_argument("--system_prompt", type=str,
                        default="The following are multiple choice questions (with answers).\n\n")
    args = parser.parse_args()

    config = vars(args)
    print("====Config====")
    print("\n".join(f"{k}={v}" for k, v in config.items()))
    print("=====")

    main(args)
