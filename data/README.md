# WMDP
<!-- add example data points -->
## QA

This benchmark tests the model for hazardous knowledge via multiple-choice questions on biosecurity, chemistry, and cybersecurity topics. 

Fields
- "answer": integer indicating index of correct answer in "choices" field
- "question": string of the multiple-choice prompt
- "choices": array of options to the multiple-choice question

Subsets
- wmdp-bio: 1,273 biosecurity prompts
- wmdp-chem: 408 chemistry prompts
- wmdp-cyber: 1,987 cybersecurity prompts

## Corpora
These corpora can be used to determine a distribution that approximates the WMDP QA information, which can be useful for unlearning algorithms. A "retain" corpus is information that should be maintained in the model after unlearning, and the "forget" corpus is information that should be removed. 

The only field is the "text" of the given excerpt. 

- bio
    - sourced from relevant papers in PubMed used for questions in WMDP-Bio
    - retain-corpus: 60.9k rows
    - forget-corpus: awaiting approval

- cyber
    - sourced from a search for relevant text on GitHub
    - retain-corpus: 4.47k rows
    - forget-corpus: 1k rows

## Auxiliary MMLU Corpora

This corpora is for unlearning general rather than hazardous knowledge. It also only has "text" field.

- economics
    - sourced from high school microeconomics and macroeconomics textbooks
    - 5.39k rows
- law
    - sourced from international and professional law textbooks
    - 1.91k rows
- physics
    - sourced from high school and college physics textbooks
    - 1.59k rows

# TOFU
[Huggingface Dataset](https://huggingface.co/datasets/locuslab/TOFU)

This dataset contains question-answer pairs based on autobiographies of 200 fictional authors generated using GPT-4. The `load_tofu_data.py` script converts this dataset into a multiple choice dataset with the same format as the WMDP dataset.

Fields
- "answer": integer indicating index of correct answer in "choices" field
- "question": string of the multiple-choice prompt
- "choices": array of options to the multiple-choice question

Available forget sets
- forget01_perturbed: Forgetting 1% of the original dataset, all entries correspond to a single author. 40 rows.
- forget05_perturbed: Forgetting 5% of the original dataset, all entries correspond to a single author. 200 rows.
- forget10_perturbed: Forgetting 10% of the original dataset, all entries correspond to a single author. 400 rows.

Available retain sets
- real_authors_perturbed: A dataset of real authors' autobiographies. 100 rows.
- retain_perturbed: A subset of the original dataset of fictional authors to be retained. 400 rows.
- world_facts_perturbed: A dataset of world facts. 117 rows.