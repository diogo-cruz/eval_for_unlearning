import os
import pandas as pd 
from datasets import load_dataset

ds = load_dataset("cais/wmdp", "wmdp-bio")
ds["test"].to_json("bio_questions.json")

ds = load_dataset("cais/wmdp", "wmdp-chem")
ds["test"].to_json("chem_questions.json")

ds = load_dataset("cais/wmdp", "wmdp-cyber")
ds["test"].to_json("cyber_questions.json")
