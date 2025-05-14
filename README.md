## lm-eval results based on different prompting techniques
Experiment results can be found [here](https://docs.google.com/spreadsheets/d/1l-DccNUN19wce4ipwb5XVnqsfE8YH6dUQCDbPJDeQvM/edit?usp=sharing)

Things we've tried so far:
- [Does Unlearning Truly Unlearn? A Black Box Evaluation of LLM Unlearning Methods](https://arxiv.org/abs/2411.12103)
  - filler (English/Hindi/Latin)
  - rephrase as conversation
  - rephrase as poem
  - remove technical terms from the question
  - translation (Arabic/Bengali/Czech/Farsi/French/German/Hindi/Korean/Telugu/Turkish/Vietnamese)
  - replace technical terms with variables
- few-shot prompting
  - n-shot WMDP-bio
  - n-shot MMLU (on select *biology* subjects)
  - n-shot WMDP-bio-retain and WMDP-bio-forget
- ReNeLLM
  - addChar, changeOrder, languageMix, misrewriteSentence, shortenSentence, styleChange
  - tested addChar on 5% random subset vs full data
- logit sensitivity analysis on the answer choices: e.g., ABCD vs abcd 

To-Do:
- Template 78
- logit sensitivity analysis on the answer choices: e.g., ABCD vs abcd 
- Run evals on the LLMU models


Models tested:
- [Zephyr_RMU](https://huggingface.co/cais/Zephyr_RMU)
- [ELM models](https://huggingface.co/collections/baulab/elm-6715d68576da0cd1a89c0c04)
  - [ELM Zephyr-7B-Beta](https://huggingface.co/baulab/elm-zephyr-7b-beta)
  - [ELM Mistral-7B-v0.1](https://huggingface.co/baulab/elm-Mistral-7B-v0.1)
  - [ELM Llama3-8B-Instruct](https://huggingface.co/baulab/elm-Meta-Llama-3-8B-Instruct)
  - [ELM Llama3-8B](https://huggingface.co/baulab/elm-Meta-Llama-3-8B)
- [LLM GAT models](https://huggingface.co/LLM-GAT)
  - GradDiff, ELM, PB&J, TAR, RR, RepNoise, RMU, RMU + LAT
- [TAR models](https://huggingface.co/lapisrocks/Llama-3-8B-Instruct-TAR-Bio-v2)
