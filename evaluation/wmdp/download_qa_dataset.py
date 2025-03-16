from datasets import load_dataset

ds = load_dataset("cais/wmdp", "wmdp-bio")
ds["test"].to_json("data/wmdp/bio_questions.json")

ds = load_dataset("cais/wmdp", "wmdp-chem")
ds["test"].to_json("data/wmdp/chem_questions.json")

ds = load_dataset("cais/wmdp", "wmdp-cyber")
ds["test"].to_json("data/wmdp/cyber_questions.json")
