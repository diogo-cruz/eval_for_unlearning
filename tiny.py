from datasets import load_dataset

ds = load_dataset("tinyBenchmarks/tinyMMLU", split="test")
print(ds)

ds.to_json("tinyMMLU.json")