import datasets
from functools import lru_cache


BIOLOGY_TASKS = [
  'anatomy',
  'clinical_knowledge',
  'college_biology',
  'college_medicine',
  'high_school_biology',
  'human_aging',
  'medical_genetics',
  'nutrition',
  'professional_medicine',
  'virology'
]

@lru_cache()
def load_tinymmlu_dataset():
  return datasets.load_dataset("tinyBenchmarks/tinyMMLU", split="dev")

@lru_cache()
def load_mmlu_dataset():
  return datasets.load_dataset("cais/mmlu", "all", split="dev")

def list_fewshot_examples():
  # ds = load_tinymmlu_dataset()
  ds = load_mmlu_dataset()
  ds = ds.filter(lambda x: x["subject"] in BIOLOGY_TASKS)
  return list(ds)