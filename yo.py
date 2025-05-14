import json
import unicodedata

data = []
with open("data/wmdp_rephrased_copy/data_translated_bengali/test/bio_questions.json", "r") as f:
  lines = f.readlines()
  for line in lines:
    line = json.loads(line)
    # print(line["question"])
    # print(unicodedata.normalize('NFC', line["question"]))
    # break

    data.append(line)

with open("bio_questions.json", "w", encoding="utf-8") as f:
  for line in data:
    f.write(json.dumps(line, ensure_ascii=False) + "\n")