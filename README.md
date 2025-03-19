# eval_for_unlearning

[Original project proposal](https://docs.google.com/document/d/1yEJBxb2VlDS6fXd9ImUNrtmfQlSOgRqmLnJ4BjGhfJI/edit?usp=sharing)

[Project notes](https://docs.google.com/document/d/1A2cGQmdcoHTeGyQdph_G7dugGvsadflqtrCxaHd1_2Y/edit?usp=sharing)

### TODO
- [ ] rephrase_prompts.py -> save folder structure
- [ ] generate_prompts > asyncio

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
| mmlu/0-shot/data_latin_filler_text (RMU)           | 0.5859      | 0.6140               | 0.9400             |
| mmlu/0-shot/data_english_filler_text (RMU)         | 0.5416      | 0.5868               | 0.9130             |
| mmlu/0-shot/data_hindi_filler_text (RMU)           | 0.5578      | 0.5991               | 0.9271             |
| mmlu/0-shot/data_rephrased_conversation (RMU)      | 0.5842      | 0.6326               | 0.9122             |
| mmlu/0-shot/data_rephrased_poem (RMU)              | 0.5128      | 0.5443               | 0.9328             |
| mmlu/0-shot/data_technical_terms_removed_1 (RMU)   | 0.5145      | 0.5616               | 0.9061             |
| mmlu/0-shot/data_technical_terms_removed_2 (RMU)   | 0.4031      | 0.4369               | 0.9171             |
| mmlu/0-shot/data_translated_french (RMU)           | 0.4815      | 0.5162               | 0.9221             |
| mmlu/0-shot/data_translated_german (RMU)           | 0.4924      | 0.5218               | 0.9318             |
| mmlu/0-shot/data_translated_hindi (RMU)            | 0.3107      | 0.3127               | 0.9936             |
| mmlu/0-shot/data_translated_korean (RMU)           | 0.3495      | 0.3787               | 0.9230             |
| mmlu/0-shot/data_translated_arabic (RMU)           | 0.3140      | 0.3213               | 0.9751             |
| mmlu/0-shot/data_translated_czech (RMU)            | 0.4351      | 0.4601               | 0.9333             |
| mmlu/0-shot/data_translated_bengali (RMU)          | 0.2984      | 0.3039               | 0.9743             |
| mmlu/0-shot/data_translated_vietnamese (RMU)       | 0.3753      | 0.4000               | 0.9335             |
| mmlu/0-shot/data_translated_turkish (RMU)          | 0.3665      | 0.3894               | 0.9370             |
| mmlu/0-shot/data_translated_telugu (RMU)           | 0.3038      | 0.3051               | 0.9952             |
| mmlu/0-shot/data_translated_farsi (RMU)            | 0.3034      | 0.3121               | 0.9721             |
| wmdp/0-shot/data_rephrased_conversation (base)    | 0.6410      | 0.6451               | 0.9937                       |
| wmdp/0-shot/data_rephrased_poem (base)            | 0.6501      | 0.6553               | 0.9921                       |
| wmdp/0-shot/data_technical_terms_removed_1 (base) | 0.5821      | 0.5862               | 0.9929                       |
| wmdp/0-shot/data_replaced_with_variables (base)   | 0.6072      | 0.6087               | 0.9976                       |
| wmdp/0-shot/data_translated_french (base)         | 0.6200      | 0.6209               | 0.9984                       |
| wmdp/0-shot/data_translated_german (base)         | 0.6017      | 0.6027               | 0.9984                       |
| wmdp/0-shot/data_translated_hindi (base)          | 0.4674      | 0.4707               | 0.9929                       |
| wmdp/0-shot/data_translated_arabic (base)         | 0.4831      | 0.4843               | 0.9976                       |
| wmdp/0-shot/data_translated_czech (base)          | 0.5907      | 0.5917               | 0.9984                       |
| wmdp/0-shot/data_translated_bengali (base)        | 0.4721      | 0.4732               | 0.9976                       |
| wmdp/0-shot/data_translated_vietnamese (base)     | 0.5294      | 0.5303               | 0.9983                       |
| wmdp/0-shot/data_translated_turkish (base)        | 0.5577      | 0.5582               | 0.9992                       |
| wmdp/0-shot/data_translated_telugu (base)         | 0.4446      | 0.4457               | 0.9976                       |
| wmdp/0-shot/data_translated_farsi (base)          | 0.4957      | 0.4961               | 0.9992                       |
| wmdp/0-shot/data_translated_korean (base)         | 0.5428      | 0.5428               | 1.0000                       |
| wmdp/0-shot/data_rephrased_conversation (RMU)    | 0.0935      | 0.4048               | 0.2310                       |
| wmdp/0-shot/data_rephrased_poem (RMU)            | 0.1300      | 0.4342               | 0.2994                       |
| wmdp/0-shot/data_technical_terms_removed_1 (RMU) | 0.1225      | 0.3949               | 0.3103                       |
| wmdp/0-shot/data_replaced_with_variables (RMU)   | 0.1233      | 0.3668               | 0.3362                       |
| wmdp/0-shot/data_translated_french (RMU)         | 0.1259      | 0.4218               | 0.2985                       |
| wmdp/0-shot/data_translated_german (RMU)         | 0.1163      | 0.3654               | 0.3181                       |
| wmdp/0-shot/data_translated_hindi (RMU)          | 0.1618      | 0.3145               | 0.5145                       |
| wmdp/0-shot/data_translated_arabic (RMU)         | 0.1508      | 0.3636               | 0.4148                       |
| wmdp/0-shot/data_translated_czech (RMU)          | 0.1225      | 0.4000               | 0.3064                       |
| wmdp/0-shot/data_translated_bengali (RMU)        | 0.1477      | 0.3456               | 0.4273                       |
| wmdp/0-shot/data_translated_vietnamese (RMU)     | 0.1253      | 0.3492               | 0.3589                       |
| wmdp/0-shot/data_translated_turkish (RMU)        | 0.1123      | 0.3548               | 0.3166                       |
| wmdp/0-shot/data_translated_telugu (RMU)         | 0.1485      | 0.3073               | 0.4831                       |
| wmdp/0-shot/data_translated_farsi (RMU)          | 0.1477      | 0.3574               | 0.4132                       |
| wmdp/0-shot/data_translated_korean (RMU)         | 0.1037      | 0.3367               | 0.3079                       |

Notes:
- RMU = Zephyr-RMU
- base = Zephyr-7b-beta
- WMDP/5-shot (RMU) used MMLU/college_biology data as the few-shot prompts