import json
from pathlib import Path

samples = Path("results/cais__Zephyr_RMU").glob("**/samples*.jsonl")
for sample in samples:
  if "10-shot" not in str(sample):
    continue 

  print(sample)
  with open(sample, "r") as f:
    lines = f.readlines()
    for line in lines:
      line = json.loads(line)
      doc = line["doc"]
      print(doc["question"])
      print(doc["answer"])
      print(doc["choices"])

      args = line["arguments"]
      for _, arg in args.items():
        print(arg["arg_0"])
        print(arg["arg_1"])
        print("===")
      break