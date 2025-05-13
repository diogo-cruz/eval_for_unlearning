# Answered vs Non-Answered Prompts

The script assumes you re-ran the results using generate_wmdp_responses_metadata(_rephrasing).py, which saves the prompts in the results for use in evaluation/wmdp/cal_wmdp_result_metadata.py. 

You can likely just map the old "run_results" files in ./results to the prompts in wmdp-bio as well - seems like order is maintained. Just a matter of doing the same check that was originally in evaluation/wmdp/cal_wmdp_result.py lines 28-29.

## WMDP-bio
```
python3 ./evaluation/wmdp/generate_wmdp_responses_metadata.py \
  --ckpt_dir "cais/Zephyr_RMU" \
  --data_dir "data/wmdp" \
  --extra_info "metadata"
```
Output in run_results_metadata.json

```
python3 ./evaluation/wmdp/cal_wmdp_result_metadata.py \
  --file_name "run_results_metadata.json"
```

See output in results/wmdp_0_shot_zephyr_rmu_metadata_results.json.

## Rephrasing (just Hindi filler)
- Updated evaluation.common.utils data_directory_list to just have hindi filler

```
python3 ./evaluation/wmdp/generate_wmdp_responses_metadata_rephrasing.py \
  --ckpt_dir "cais/Zephyr_RMU" \
  --data_dir "data/wmdp-rephrased" \
  --extra_info "metadata"
```

Output in run_results_metadata_rephrasing.json

```
python3 ./evaluation/wmdp/cal_wmdp_result_metadata_rephrasing.py \
  --file_name "run_results_metadata_rephrasing.json"
```

See output in results/data_hindi_filler_text_zephyr_rmu_metadata_results.json.

## Output Structure
- "questions" are the wmdp entries
- "prompts" is the full prompt given to the model
- "non_system_prompts" do not include the system prompt but include other context