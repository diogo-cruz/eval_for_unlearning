# eval_for_unlearning

[Original project proposal](https://docs.google.com/document/d/1yEJBxb2VlDS6fXd9ImUNrtmfQlSOgRqmLnJ4BjGhfJI/edit?usp=sharing)

[Project notes](https://docs.google.com/document/d/1A2cGQmdcoHTeGyQdph_G7dugGvsadflqtrCxaHd1_2Y/edit?usp=sharing)

### TODO
- [ ] rephrase_prompts.py -> save folder structure


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
python3 ./evaluation/wmdp/generate_wmdp_responses_rephrasing.py \
  --ckpt_dir "cais/Zephyr_RMU" \
  --data_dir "data/wmdp-rephrased" \

python3 ./evaluation/wmdp/cal_wmdp_result_rephrasing.py \
  --file_name "results/wmdp_0_shot_zephyr_rmu_run_results__rephrasing.json"# 
```

See results folder for experiment results.

### Experiment Results
| Dataset | ACC-biology | ACC-biology-answered | %-biology-answered |
|----------------|-------------|---------------------|--|
| MMLU/0-shot (RMU) | 0.5882 | 0.6316 | 0.9251 |
| MMLU/0-shot (base) | 0.6448 | 0.6505 | 0.9913 |
| WMDP/0-shot (RMU) | 0.1461 | 0.3891 | 0.3755 |
| WMDP/0-shot (base) | 0.6630 | 0.6651 | 0.9969 |
| MMLU/5-shot (RMU) | 0.5555 | 0.5607 | 0.8932 | 
| MMLU/5-shot (base) | 0.6517 | 0.6545 | 0.9958 |
| WMDP/5-shot (RMU) | 0.2129 | 0.3358 | 0.6339 | 
| MMLU/0-shot/data_latin_filler_text (base) | 0.6314 | 0.6343 | 0.9955 |
| MMLU/0-shot/data_english_filler_text (base) | 0.5889 | 0.5999 | 0.9806 |
| MMLU/0-shot/data_hindi_filler_text (base) | 0.6015 | 0.6082 | 0.9893 |
| MMLU/0-shot/data_rephrased_conversation (base) | 0.6374 | 0.6421 | 0.9924 |
| MMLU/0-shot/data_rephrased_poem (base) | 0.5491 | 0.5519 | 0.9950 |
| MMLU/0-shot/data_technical_terms_removed_1 (base) | 0.5495 | 0.5642 | 0.9730 |
| MMLU/0-shot/data_technical_terms_removed_2 (base) | 0.4380 | 0.4440 | 0.9868 |
| MMLU/0-shot/data_translated_french (base) | 0.5188 | 0.5202 | 0.9973 |
| MMLU/0-shot/data_translated_german (base) | 0.5204 | 0.5229 | 0.9952 |
| MMLU/0-shot/data_translated_hindi (base) | 0.3173 | 0.3184 | 0.9966 |
| MMLU/0-shot/data_translated_korean (base) | 0.3765 | 0.3765 | 1.0000 |
| MMLU/0-shot/data_translated_arabic (base) | 0.3161 | 0.3163 | 0.9996 |
| MMLU/0-shot/data_translated_czech (base) | 0.4768 | 0.4768 | 1.0000 |
| MMLU/0-shot/data_translated_bengali (base) | 0.3002 | 0.3008 | 0.9981 |
| MMLU/0-shot/data_translated_vietnamese (base) | 0.3968 | 0.3979 | 0.9970 |
| MMLU/0-shot/data_translated_turkish (base) | 0.3947 | 0.3962 | 0.9961 |
| MMLU/0-shot/data_translated_telugu (base) | 0.3111 | 0.3120 | 0.9974 |
| MMLU/0-shot/data_translated_farsi (base) | 0.3356 | 0.3358 | 0.9994 |

| WMDP/translated_korean | 0.1037 | 0.3367 | 0.3079 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |

Notes:
- RMU = Zephyr-RMU
- base = Zephyr-7b-beta
- WMDP/5-shot (RMU) used MMLU/college_biology data as the few-shot prompts