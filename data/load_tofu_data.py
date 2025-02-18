from datasets import Dataset, load_dataset

import random

def convert_tofu_dataset_to_mc(dataset, seed=42):
  """Convert the TOFU dataset to a multiple choice dataset.
  
  Args:
    dataset: The TOFU dataset to convert.
    seed: The seed for the random number generator.
  Yields:
    A dictionary with the following keys:
      - "answer": The index of the correct choice.
      - "question": The question.
      - "choices": A list of the choices.
  """
  random.seed(seed)
  for idx, data in enumerate(dataset):
    # The WMDP dataset uses 4 choices for multiple choice, so we do the same for TOFU.
    num_choices = 4
    perturbed_answer_idx = random.sample(range(0, len(data["perturbed_answer"])), num_choices - 1)

    # We use the paraphrased answer instead of the original answer when possible
    # because the paraphrased answer is formatted the same as the
    # perturbed choices. However, the `world_facts_perturbed` and
    # `real_authors_perturbed` datasets do not have paraphrased answers, so
    # we use the original answer in those cases.
    correct_answer = data["paraphrased_answer"] if "paraphrased_answer" in data else data["answer"]
    choices = [correct_answer]
    for i in perturbed_answer_idx:
      choices.append(data["perturbed_answer"][i])
    random.shuffle(choices)

    # We identify the answer with the index of the choice in the choices list for
    # consistency with the WMDP dataset.
    answer_idx = choices.index(correct_answer)
    
    new_data_dict = {
      "answer": answer_idx,
      "question": data["question"],
      "choices": choices,
    }
    yield new_data_dict


def main():
  # The TOFU dataset has 3 different levels of forgetting: 1%, 5%, and 10%.
  tofu = [
    ("locuslab/TOFU", "forget01_perturbed"),
    ("locuslab/TOFU", "forget05_perturbed"),
    ("locuslab/TOFU", "forget10_perturbed"),

    ("locuslab/TOFU", "real_authors_perturbed"),
    ("locuslab/TOFU", "retain_perturbed"),
    ("locuslab/TOFU", "world_facts_perturbed"),
  ]

  for name, subset in tofu:
    tofu_dataset = load_dataset(name, subset, split="train")
    mc_tofu_dataset = Dataset.from_generator(convert_tofu_dataset_to_mc, gen_kwargs={"dataset": tofu_dataset})
    print(f'\n\nThe following is a sample row from {subset}:')
    print(mc_tofu_dataset[0], '\n\n')

  dataset = load_dataset("locuslab/TOFU", "forget10_perturbed", split="train")  
  author = "Hsiao Yun-Hwa"
  starter = dataset.filter(lambda row: author in row['question'])
  starter_mc = Dataset.from_generator(convert_tofu_dataset_to_mc, gen_kwargs={"dataset": starter})
  
  print(f'Created a starter dataset of length {len(starter_mc)}. Here is a sample:')
  print(starter_mc[0])

if __name__ == "__main__":
  main()
