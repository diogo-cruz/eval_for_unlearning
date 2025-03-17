import os
import re
import json
from pathlib import Path
from tqdm import tqdm
from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

PROMPT_PATH = Path(__file__).parent / "prompts"
DATA_PATH = Path(__file__).parent.parent.parent / "data"

def _load_prompt_settings() -> dict:
  with open(PROMPT_PATH / "settings.json", "r") as f:
    return json.load(f)

def get_prompt_technique_names() -> list[str]:
  return list(_load_prompt_settings().keys())

def load_prompt_settings(prompt_technique_name: str) -> dict:
  return _load_prompt_settings()[prompt_technique_name]

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
  for i, line in tqdm(enumerate(lines)):
    question = line["question"]
    if verbose: print("original question:", question)
    rephrased_question = generate_rephrased_prompt(prompt_technique_name, question, **kwargs)
    if verbose: print("rephrased question:", rephrased_question)
    
    ## overwrite the question
    lines[i]["question"] = rephrased_question
    lines[i]["original_question"] = question

  wmdp_rephrased_data_dir = DATA_PATH / "wmdp-rephrased"
  Path(wmdp_rephrased_data_dir).mkdir(parents=True, exist_ok=True)
  with open(wmdp_rephrased_data_dir / f"{task}_questions_{prompt_technique_name}.json", "w") as f:
    for line in lines:
      f.write(json.dumps(line) + "\n")


if __name__ == "__main__":
  rephrase_settings = get_prompt_technique_names()
  generate_rephrased_wmdp_data(task="bio", prompt_technique_name="translating_to_language", language="Korean")
  # for prompt_technique_name in rephrase_settings:
  #   print(f"Generating rephrases for {prompt_technique_name}")
  #   generate_rephrased_wmdp_data(task="bio", prompt_technique_name=prompt_technique_name) 