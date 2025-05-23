import json
from pathlib import Path

def get_questions_with_meta(fpath):
  right_format = []
  wrong_format = []
  with open(fpath, "r") as f:
    lines = f.readlines()
    for line in lines:
      line = json.loads(line)
      if line["right_format"]:
        right_format.append(line)
      else:
        wrong_format.append(line)

  return right_format, wrong_format

def save_questions(fpath, questions):
  with open(fpath, "w") as f:
    for question in questions:
      f.write(json.dumps(question) + "\n")

if __name__ == "__main__":
  rephrasings = Path("data/wmdp_rephrased_rmu")
  for rephrasing in rephrasings.iterdir():
    if rephrasing.stem.startswith("data") and "telugu" not in rephrasing.stem:
      right, wrong = get_questions_with_meta(rephrasing / "test" / "bio_questions_with_meta.json")
      
      print(rephrasing)
      print(len(right))
      print(len(wrong))

      save_dir = Path(f"data/wmdp_rephrased_rmu_lm_eval/{rephrasing.stem}/test")
      save_dir.mkdir(parents=True, exist_ok=True)
      save_questions(save_dir / "bio_questions_right.json", right)
      # save_questions(save_dir / "bio_questions_wrong.json", wrong)

      ## create yaml file for lm_eval
      yaml_dir = Path("custom_tasks/wmdp_lm_eval_tasks_rmu_logit_analysis")
      yaml_dir.mkdir(parents=True, exist_ok=True)

      task = f"wmdp_bio_rephrased_{rephrasing.stem.replace('data_','')}".replace('_text','')
      if "conversation" in task:
        task = f"wmdp_bio_rephrased_conversation"
      elif "poem" in task:
        task = f"wmdp_bio_rephrased_poem"
      elif "variable" in task:
        task = f"wmdp_bio_rephrased_replace_with_variables"

      print(task)
      yaml_file = yaml_dir / f"{task}.yaml"
      with open(yaml_file, "w") as f:
        f.write(f'"task": "{task}"\n')
        f.write('"dataset_name": "default"\n')
        f.write(f'"dataset_path": "./data/wmdp_rephrased_rmu_lm_eval/{rephrasing.stem}"\n')
        f.write('"include": "_default_template_yaml"\n')
        f.write('\"description\": \"The following are multiple choice questions (with answers) about biology.\n\n\"')