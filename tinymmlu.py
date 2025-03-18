from pathlib import Path
from datasets import load_dataset

dataset = load_dataset("tinyBenchmarks/tinyMMLU")

for split, ds in dataset.items():
  print(split)
  folder = Path(f"data/tinyMMLU/{split}")
  folder.mkdir(parents=True, exist_ok=True)

  print(ds["subject"])
  print(ds.to_pandas()["subject"].value_counts())

  print(ds.filter(lambda x: x.get("subject") == "abstract_algebra"))

  # for row in ds:
  #   print(row)
  #   break
  
  break
  # ds.to_csv(folder / f"tinyMMLU.csv")


import pandas as pd
# ds = pd.read_csv("data/tinyMMLU/dev/tinyMMLU.csv")
# print(ds.iloc[0])


df = pd.read_csv("data/MMLU/dev/abstract_algebra_dev.csv")
print(df)