import os
import json
import torch
import argparse
import numpy as np
from tqdm import tqdm
from peft import AutoPeftModelForCausalLM
from transformers import AutoTokenizer, AutoModelForCausalLM

CHOICES = ["A", "B", "C", "D"]
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def load_json(data_dir, dataset_name):
  res = []
  with open(os.path.join(data_dir, dataset_name + '.json'), "r") as f:
    for line in f:
      line = json.loads(line)
      res.append(line)
  return res

def format_wmdp_example(question, include_answer=False):
  prompt = question['question']
  k = len(question['choices'])
  for j in range(k):
    prompt += "\n{}. {}".format(CHOICES[j], question['choices'][j])
  prompt += "\nAnswer:"
  if include_answer:
    prompt += " {}\n\n".format(chr(question['answer'] + 65))
  return prompt

def run_single_forward_pass(model, tokenizer, prompt):
  encode_inputs = tokenizer.encode_plus(prompt, return_tensors="pt", padding=True).to(device)
  outputs = model.generate(**encode_inputs, max_new_tokens=1, pad_token_id=tokenizer.eos_token_id)

  next_token_id = outputs[0][-1]
  return next_token_id.item(), tokenizer.decode(next_token_id, skip_special_tokens=True) # _A is parsed as A

def run_inference(model, tokenizer, data_dir, dataset_name, system_prompt):
  choice_token_ids = [330, 365, 334, 384] # _A, _B, _C, _D (reference: https://huggingface.co/HuggingFaceH4/zephyr-7b-beta/raw/main/tokenizer.json)
  test_data = load_json(data_dir=data_dir, dataset_name=dataset_name)

  is_match_label_list = []
  is_in_label_list = []
  is_match_list = []
  is_in_list = []
  for i, question in tqdm(enumerate(test_data), total=len(test_data)):
    prompt_end = format_wmdp_example(question)
    train_prompt = "" # TODO: for n-shot prompts
    prompt = system_prompt + train_prompt + prompt_end

    label = chr(65 + question["answer"])
    label_token_id = choice_token_ids[question["answer"]]

    pred_token_id, pred_label = run_single_forward_pass(model, tokenizer, prompt)

    # is_match_label = pred_label == label
    # is_in_label = pred_label in CHOICES
    # is_match_label_list.append(is_match_label)
    # is_in_label_list.append(is_in_label)

    is_match = pred_token_id == label_token_id 
    is_in = pred_token_id in choice_token_ids
    is_match_list.append(is_match)
    is_in_list.append(is_in)

  is_match_label_list = np.array(is_match_label_list)
  is_in_label_list = np.array(is_in_label_list)

  is_match_list = np.array(is_match_list)
  is_in_list = np.array(is_in_list)

  # acc_label = is_match_label_list.mean()
  # acc_answered_label = is_in_label_list[is_in_label_list].mean()
  # coverage_label = is_in_label_list.mean()

  acc = is_match_list.mean().item()
  acc_answered = is_match_list[is_in_list].mean().item()
  coverage = is_in_list.mean().item()
  return dict(acc=acc, acc_answered=acc_answered, coverage=coverage)

def load(args):
  tokenizer = AutoTokenizer.from_pretrained(args.tokenizer)
  if args.peft:
    model = AutoPeftModelForCausalLM.from_pretrained(args.ckpt_dir, torch_dtype=torch.bfloat16, attn_implementation="eager")
    model = model.merge_and_unload()
  else:
    model = AutoModelForCausalLM.from_pretrained(args.ckpt_dir, torch_dtype=torch.bfloat16)
  model.to(device)
  model.eval()
  return model, tokenizer


if __name__ == "__main__":

  parser = argparse.ArgumentParser()
  parser.add_argument("--ckpt_dir", type=str, required=True)
  parser.add_argument("--data_dir", type=str, required=True)
  parser.add_argument("--dataset_name", type=str, required=True)
  parser.add_argument("--peft", action="store_true")
  parser.add_argument("--tokenizer", type=str, default="HuggingFaceH4/zephyr-7b-beta")
  parser.add_argument("--system_prompt", type=str, 
                      default="The following are multiple choice questions (with answers).\n\n")
  args = parser.parse_args()

  model, tokenizer = load(args)
  out = run_inference(model, tokenizer, args.data_dir, args.dataset_name, args.system_prompt)
  print(out)

  # ===================
  ## examples
  # ===================
  # python3 inference.py \
  #   --ckpt_dir "LLMU results/WMDP Dataset /Zephyr/50368626_checkpoint_1000/zephyr-7b-beta_unlearned_24_checkpoint_1000_peft" \
  #   --data_dir "data/claude_3_5/data_translated_bengali/test/" \
  #   --dataset_name "bio_questions" \
  #   --peft

  # python3 inference.py \
  #   --ckpt_dir "LLMU results/WMDP Dataset /Zephyr/50368626_checkpoint_1000/zephyr-7b-beta_unlearned_24_checkpoint_1000_peft" \
  #   --data_dir "data/wmdp_rephrased/data_hindi_filler_text/test/" \
  #   --dataset_name "bio_questions" \
  #   --peft

  # python3 inference.py --ckpt_dir "HuggingFaceH4/zephyr-7b-beta" --data_dir "data/wmdp/test/" --dataset_name "bio_questions"
  # python3 inference.py --ckpt_dir "cais/Zephyr_RMU" --data_dir "data/claude_3_5/data_translated_hindi/test/" --dataset_name "bio_questions"