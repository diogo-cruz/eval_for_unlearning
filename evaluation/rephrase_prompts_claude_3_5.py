import os
import re
import json
import pandas as pd
from tqdm import tqdm
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

PROMPT_PATH = Path(__file__).parent / "prompts"
DATA_PATH = Path(__file__).parent.parent / "data"

def _load_prompt_settings() -> dict:
  setting_file = "settings_claude_3_5.json"
  with open(PROMPT_PATH / setting_file, "r") as f:
    return json.load(f)

def get_prompt_technique_names() -> list[str]:
  return list(_load_prompt_settings().keys())

def load_prompt_settings(prompt_technique_name: str) -> dict:
  return _load_prompt_settings()[prompt_technique_name]

SAVE_DIR_MAPPING = {}
for prompt_technique_name in _load_prompt_settings():
  if prompt_technique_name == "rephrase_as_conversation":
    SAVE_DIR_MAPPING[prompt_technique_name] = "data_rephrased_conversation"
  elif prompt_technique_name == "rephrase_as_poem":
    SAVE_DIR_MAPPING[prompt_technique_name] = "data_rephrased_poem"
  elif prompt_technique_name == "removing_technical_terms_from_the_question":
    SAVE_DIR_MAPPING[prompt_technique_name] = "data_technical_terms_removed_1"
  elif prompt_technique_name == "removing_technical_terms_from_both_the_question_and_the_choices":
    SAVE_DIR_MAPPING[prompt_technique_name] = "data_technical_terms_removed_2"
  elif prompt_technique_name == "translating_to_language":
    SAVE_DIR_MAPPING[prompt_technique_name] = "data_translated_"
  elif prompt_technique_name == "replacing_technical_terms_with_variables":
    SAVE_DIR_MAPPING[prompt_technique_name] = "data_replaced_with_variables"
  else:
    raise ValueError(f"Invalid prompt technique name: {prompt_technique_name}")


def load_prompt(prompt_technique_name: str) -> str:
  prompt_path = PROMPT_PATH / f"{prompt_technique_name}"
  with open(prompt_path, "r") as f:
    return f.read().strip()

def load_wmdp_data(task: str) -> list[dict]:
  res = []
  with open(DATA_PATH / "wmdp" / f"{task}_questions.json", "r") as f:
    for line in f:
      line = json.loads(line)
      res.append(line)
  return res

def load_tiny_mmlu_data(subject: str, split: str) -> list[dict]:
  assert split in ["dev", "test"], f"invalid split: {split}"
  res = pd.read_csv(DATA_PATH / "tinyMMLU" / split / f"{subject}_{split}.csv", header=None)
  return res

def extract_tags(text):
  pattern = r'<([^>]+)>'
  matches = re.findall(pattern, text)
  return matches

def generate_rephrased_prompt(prompt_technique_name: str, question: str, **kwargs):
  # assert "model" in kwargs, f"model not in kwargs: {kwargs}"
  # assert "max_tokens" in kwargs, f"max_tokens not in kwargs: {kwargs}"
  # assert "temperature" in kwargs, f"temperature not in kwargs: {kwargs}"

  prompt = load_prompt(prompt_technique_name)
  prompt = prompt.replace("<question>", question)
  tags = extract_tags(prompt)
  for tag in tags:
    if tag == "question": continue
    assert tag in kwargs, f"tag {tag} not in kwargs: {kwargs}"
    prompt = prompt.replace(f"<{tag}>", kwargs[tag])

  try:
    client = Anthropic()
    settings = load_prompt_settings(prompt_technique_name)
    if "languages" in settings:
      assert kwargs["language"] in settings["languages"], f"invalid language: {kwargs['language']}"
      del settings["languages"]

    message = client.messages.create(
      messages=[{"role": "user", "content": prompt}],
      **settings
    )
    return message.content[0].text
  except Exception as e:
    print(f"An error occurred: {e}")

def generate_rephrased_wmdp_data(task: str, prompt_technique_name: str, verbose: bool = False, **kwargs):
  assert task in ["bio", "cyber"], f"invalid task: {task}"

  lines = load_wmdp_data(task)
  for i, line in tqdm(enumerate(lines), total=len(lines)):
    question = line["question"]
    if verbose: print("original question:", question)
    rephrased_question = generate_rephrased_prompt(prompt_technique_name, question, **kwargs)
    if verbose: print("rephrased question:", rephrased_question)
    
    ## overwrite the question
    lines[i]["question"] = rephrased_question
    lines[i]["original_question"] = question

    if i == 0:
      print(question)
      print(rephrased_question)

  ## save the original questions
  wmdp_rephrased_data_dir = DATA_PATH / "wmdp-rephrased" / 'claude_3_5'
  print(f'saving to {wmdp_rephrased_data_dir}')
  Path(wmdp_rephrased_data_dir).mkdir(parents=True, exist_ok=True)
  
  filename = f"{task}_questions_{prompt_technique_name}"
  if "language" in kwargs:
      filename += f"_{kwargs['language'].lower()}"
  filename += ".json"

  with open(wmdp_rephrased_data_dir / filename, "w") as f:
    for line in lines:
      f.write(json.dumps(line) + "\n")

def generate_rephrased_tiny_mmlu_data(subject: str, prompt_technique_name: str, split: str, verbose: bool = False, **kwargs):
  assert split in ["dev", "test"], f"invalid split: {split}"
  lines = load_tiny_mmlu_data(subject=subject, split=split)
  for i, line in tqdm(lines.iterrows(), total=len(lines)):
    question = line[0]
    if verbose: print("original question:", question)
    rephrased_question = generate_rephrased_prompt(prompt_technique_name, question, **kwargs)
    if verbose: print("rephrased question:", rephrased_question)

    ## overwrite the question
    lines.loc[i,0] = rephrased_question

    if i == 0:
      print(question)
      print(rephrased_question)

  ## save the original questions
  tiny_mmlu_rephrased_data_dir = DATA_PATH / "tinyMMLU-rephrased" / SAVE_DIR_MAPPING[prompt_technique_name]
  if "language" in kwargs:
    tiny_mmlu_rephrased_data_dir = tiny_mmlu_rephrased_data_dir.parent / (tiny_mmlu_rephrased_data_dir.name + kwargs["language"].lower()) / split
  else:
    tiny_mmlu_rephrased_data_dir /= split
  Path(tiny_mmlu_rephrased_data_dir).mkdir(parents=True, exist_ok=True)

  lines.to_csv(tiny_mmlu_rephrased_data_dir / f"{subject}_{split}.csv", header=False, index=False)

def generate_rephrased_filler_text_mmlu(subject: str, language: str, split: str, verbose: bool = False):
  with open(PROMPT_PATH / f"{language.lower()}_filler_text", "r") as f:
    filler_text = f.read().strip() + "\n\n"

  lines = pd.read_csv(DATA_PATH / "tinyMMLU"/ split / f"{subject}_{split}.csv", header=None)
  lines[0] = filler_text + lines[0] 

  save_dir = DATA_PATH / "tinyMMLU-rephrased" / f"data_{language.lower()}_filler_text" / split
  save_dir.mkdir(parents=True, exist_ok=True)
  lines.to_csv(save_dir / f"{subject}_{split}.csv", header=False, index=False)  

def generate_rephrased_filler_text_wmdp(task: str, language: str,verbose: bool = False):
  with open(PROMPT_PATH / f"{language.lower()}_filler_text", "r") as f:
    filler_text = f.read().strip() + "\n\n"

  with open(DATA_PATH / "wmdp" / f"{task}_questions.json", "r") as f:
    lines = f.readlines()
    lines = [json.loads(line) for line in lines]
  
  for line in lines:
    line["question"] = filler_text + line["question"]

  save_dir = DATA_PATH / "wmdp-rephrased" / 'claude_3_5' / f"data_{language.lower()}_filler_text"
  print(f'saving to {save_dir}')
  save_dir.mkdir(parents=True, exist_ok=True)
  with open(save_dir / f"{task}_questions.json", "w") as f:
    for line in lines:
      f.write(json.dumps(line) + "\n")

if __name__ == "__main__":
  
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument("--data", type=str, required=True)
  parser.add_argument("--task", type=str, choices=["bio", "cyber"])
  parser.add_argument("--prompt_technique_name", type=str, required=True)
  parser.add_argument("--language", type=str)
  parser.add_argument("--split", type=str, choices=["dev", "test"])
  args = parser.parse_args()

  print(f"Generating rephrases for {args.prompt_technique_name}")
  
  if args.data == "wmdp":
    if args.task is None: raise ValueError("task is required for wmdp data")
    if args.split == "dev": raise ValueError("dev split is not supported for wmdp data")
    if args.language:
      if args.prompt_technique_name.startswith("filler_"):
        generate_rephrased_filler_text_wmdp(task=args.task, language=args.language)
      else:
        generate_rephrased_wmdp_data(task=args.task, prompt_technique_name=args.prompt_technique_name, language=args.language) 
    else:
      generate_rephrased_wmdp_data(task=args.task, prompt_technique_name=args.prompt_technique_name) 
  elif args.data == "tinyMMLU":
    from MMLU.tinyMMLU_utils import TASKS
    for subject in TASKS:
      if args.language:
        if args.prompt_technique_name.startswith("filler_"):
          generate_rephrased_filler_text_mmlu(subject=subject, language=args.language, split=args.split)
        else:
          generate_rephrased_tiny_mmlu_data(subject=subject, prompt_technique_name=args.prompt_technique_name, split=args.split, language=args.language)
      else:
        generate_rephrased_tiny_mmlu_data(subject=subject, prompt_technique_name=args.prompt_technique_name, split=args.split)
  else:
    raise ValueError(f"Invalid data argument: {args.data}")
