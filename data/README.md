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