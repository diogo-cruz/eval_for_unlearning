import json
import math
import torch
import numpy as np 
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("cais/Zephyr_RMU")
model = AutoModelForCausalLM.from_pretrained("cais/Zephyr_RMU", torch_dtype=torch.bfloat16, device_map="auto")

ans_match_list = []
order_match_list = []

target_token_list = [
  ["A", "B", "C", "D"], 
  ["a", "b", "c", "d"],
  ["i", "ii", "iii", "iv"],
  ["1", "2", "3", "4"],
]


for target_tokens in target_token_list:
  with open("results/cais__Zephyr_RMU/0-shot/samples_wmdp_bio_2025-04-23T02-05-13.989610.jsonl") as f:
    lines = f.readlines()
    for line in tqdm(lines):
      line = json.loads(line)
      args = line["arguments"]
      resps = line["filtered_resps"]
      answer = line["target"]

      context = args["gen_args_1"]["arg_0"]
      # print(context)
        
      tokens = tokenizer(context, return_tensors="pt").to(model.device)
      output = model(**tokens, return_dict=True)
      next_token_logits = output.logits[:, -1, :]
      next_token = next_token_logits.argmax(dim=-1)

      target_ids = tokenizer.convert_tokens_to_ids(target_tokens)
      # print(target_ids)

      logprobs = next_token_logits.log_softmax(dim=-1)
      target_logprobs = []
      for token, token_id in zip(target_tokens, target_ids):
        logit = next_token_logits[0, token_id].item()
        logprob = logprobs[0, token_id].item()
        # print(f"Token: {token}, Logit: {logit}, Logprob: {logprob}")
        target_logprobs.append(logprob)

      target_answer = target_logprobs.index(max(target_logprobs))
      target_orders = sorted(range(len(target_logprobs)), reverse=True, key=target_logprobs.__getitem__)
      # print(target_logprobs)
      # print(target_answer)
      # print(target_orders)

      resps = [float(r[0]) for r in resps]
      resp_answer = resps.index(max(resps))
      resp_orders = sorted(range(len(resps)), reverse=True, key=resps.__getitem__)
      # print(resps)
      # print(resp_answer)
      # print(resp_orders)

      # print(answer)

      # metrics
      # ans_match = target_answer == int(answer)
      ans_match = target_answer == resp_answer
      order_match = target_orders == resp_orders

      ans_match_list.append(ans_match)
      order_match_list.append(order_match)


      if not ans_match:
        print(context)
        print(target_logprobs)
        print(resps)
        break



  print(target_tokens)
  print(f"ans_match: {np.mean(ans_match_list)}, order_match: {np.mean(order_match_list)}")