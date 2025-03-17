# eval_for_unlearning

[Original project proposal](https://docs.google.com/document/d/1yEJBxb2VlDS6fXd9ImUNrtmfQlSOgRqmLnJ4BjGhfJI/edit?usp=sharing)

[Project notes](https://docs.google.com/document/d/1A2cGQmdcoHTeGyQdph_G7dugGvsadflqtrCxaHd1_2Y/edit?usp=sharing)

### TODO
[ ] rephrase_prompts.py -> save folder structure


### How to run WMDP evals
Run WMDP eval scripts (0-shot):
```bash
python3 ./evaluation/wmdp/generate_wmdp_responses.py \
  --ckpt_dir "cais/Zephyr_RMU" \
  --data_dir "data/wmdp" 

python3 ./evaluation/wmdp/cal_wmdp_result.py \
  --file_name "run_results_.json"
```

Run WMDP eval scripts (5-shot on MMLU/college_biology):
```bash
python3 ./evaluation/wmdp/generate_wmdp_responses.py \
  --ckpt_dir "cais/Zephyr_RMU" \
  --data_dir "." \
  --MMLU_dir "data/MMLU" \
  --dev_task "college_biology" \
  --ntrain 5

python3 ./evaluation/wmdp/cal_wmdp_result.py \
  --file_name "run_results__college_biologydev.json"
```

Run WMDP eval scripts (rephrasing): 
```bash
WIP
```

See results folder for experiment results.

### Experiment Results
| | ACC-biology | ACC-biology-answered | %-biology-answered | ACC-cyber | ACC-cyber-answered | %-cyber-answered | ACC-other | ACC-other-answered | %-other-answered | ACC-all_subjects | ACC-all_subjects-answered | %-all_subjects-answered |
|----------------|-------------|---------------------|-------------------|-----------|-------------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|
| MMLU/0-shot (RMU) | 0.5882 | 0.6316 | 0.9251 | N/A | N/A | N/A | 0.5720 | 0.5940 | 0.9627 | 0.5749 | 0.6006 | 0.9561 |
| MMLU/0-shot (base) | 0.6448 | 0.6505 | 0.9913 | N/A | N/A | N/A | 0.5769 | 0.5943 | 0.9704 | 0.5888 | 0.6041 | 0.9741 | 
| WMDP/0-shot (RMU) | 0.1461 | 0.3891 | 0.3755 | 0.1042 | 0.3913 | 0.2662 | N/A | N/A | N/A | N/A | N/A | N/A |  
| WMDP/0-shot (base) | 0.6630 | 0.6651 | 0.9969 | 0.4197 | 0.4360 | 0.9628 | N/A | N/A | N/A | N/A | N/A | N/A | 
| MMLU/5-shot (RMU) | 0.5555 | 0.5607 | 0.8932 | N/A | N/A | N/A | 0.5782 | 0.5841 | 0.9821 | 0.5750 | 0.5800 | 0.9665 |
| MMLU/5-shot (base) | 0.6517 | 0.6545 | 0.9958 | N/A | N/A | N/A | 0.6020 | 0.6037 | 0.9972 | 0.6107 | 0.6126 | 0.9970 |
| WMDP/5-shot (RMU) | 0.2129 | 0.3358 | 0.6339 | 0.2058 | 0.3626 | 0.5677 | N/A |  N/A | N/A | N/A | N/A | N/A |
| WMDP/translated_korean | 0.1037 | 0.3367 | 0.3079 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |

** RMU = Zephyr-RMU
** base = Zephyr-7b-beta
** WMDP/5-shot (RMU) used MMLU/college_biology data as the few-shot prompts