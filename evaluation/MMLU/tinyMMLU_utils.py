from pathlib import Path

TASKS = [f.stem.replace("_test", "") for f in Path("data/tinyMMLU/test").glob("*.csv")]
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
  'virology',
]
OTHER_TASKS = [task for task in TASKS if task not in BIOLOGY_TASKS]