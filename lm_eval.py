import json

with open("bio_questions_with_meta.json", "r") as f:
  lines = f.readlines()
  right_format = []
  wrong_format = []
  for line in lines:
    line = json.loads(line)
    if line["right_format"]:
      right_format.append(line)
    else:
      wrong_format.append(line)

print(len(right_format))
print(len(wrong_format))
