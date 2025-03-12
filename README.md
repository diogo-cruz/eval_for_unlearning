# eval_for_unlearning

[Original project proposal](https://docs.google.com/document/d/1yEJBxb2VlDS6fXd9ImUNrtmfQlSOgRqmLnJ4BjGhfJI/edit?usp=sharing)

[Project notes](https://docs.google.com/document/d/1A2cGQmdcoHTeGyQdph_G7dugGvsadflqtrCxaHd1_2Y/edit?usp=sharing)


### How to run WMDP evals
First download the WMDP data:

```bash
python3 dataset.py
```

Run WMDP eval scripts (0-shot):
```bash
python3 ./evaluation/wmdp/generate_wmdp_responses.py \
  --ckpt_dir "cais/Zephyr_RMU" \
  --data_dir "." 

python3 ./evaluation/wmdp/cal_wmdp_result.py \
  --file_name "run_results_.json"
```

Run WMDP eval scripts (5-shot on MMLU/college_biology):
```bash
python3 ./evaluation/wmdp/generate_wmdp_responses.py \
  --ckpt_dir "cais/Zephyr_RMU" \
  --data_dir "." \
  --MMLU_dir "./data/MMLU" \
  --dev_task "college_biology" \
  --ntrain 5

python3 ./evaluation/wmdp/cal_wmdp_result.py \
  --file_name "run_results__college_biologydev.json"
```

Run WMDP eval scripts (rephrasing): (wip)

### Experiment Results
|                | ACC-biology | ACC-biology-answered | %-biology-answered | ACC-cyber | ACC-cyber-answered | %-cyber-answered |
| WMDP/0-shot    | 0.1461      | 0.3891               | 0.3755             | 0.1042    | 0.3913             | 0.2662           |
| WMDP/5-shot    | 0.2129      | 0.3358               | 0.6339             | 0.2058    | 0.3626             | 0.5677           |
| WMDP/rephrase  | N/A         | N/A                  | N/A                | N/A       | N/A                | N/A              |

** WMDP/5-shot used MMLU/college_biology data as the few-shot prompts