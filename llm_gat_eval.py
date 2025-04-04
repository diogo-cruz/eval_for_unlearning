import subprocess
from itertools import product

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--output_dir", type=str, required=True)
args = parser.parse_args()

repo = "LLM-GAT"
models = ["graddiff", "elm", "pbj", "tar", "rr", "repnoise", "rmu", "rmu-lat"]
epochs = list(range(8,0,-1))

checkpoints = [f"{repo}/llama-3-8b-instruct-{model}-checkpoint-{epoch}" for model, epoch in product(models, epochs)]

tasks = [
  "wmdp_bio",
  "wmdp_bio_rephrased_english_filler",
  "wmdp_bio_rephrased_hindi_filler",
  "wmdp_bio_rephrased_latin_filler",
  "wmdp_bio_rephrased_conversation",
  "wmdp_bio_rephrased_poem",
  "wmdp_bio_rephrased_replace_with_variables",   
  "wmdp_bio_rephrased_technical_terms_removed_1",
  "wmdp_bio_rephrased_translated_farsi",
  "wmdp_bio_rephrased_translated_german",
  "wmdp_bio_rephrased_translated_korean",
  "tinyMMLU"
]

for checkpoint in checkpoints:
    print(f"Evaluating {checkpoint}")
    subprocess.run([
      "lm_eval", 
      "--model", "hf", 
      "--model_args", f"pretrained={checkpoint},dtype=bfloat16", 
      "--output", args.output_dir, 
      "--log_sample",
      "--tasks", ",".join(tasks),
    ])