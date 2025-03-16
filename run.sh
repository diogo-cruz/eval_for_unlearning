# python3 ./evaluation/wmdp/generate_wmdp_responses.py \
#   --ckpt_dir "cais/Zephyr_RMU" \
#   --data_dir "." 

# python3 ./evaluation/wmdp/cal_wmdp_result.py \
#   --file_name "run_results_.json"

# already recorded..
# ACC-biology: 0.1461
# ACC-biology-answered: 0.3891
# Percentage-biology-answered: 0.3755
# -----------------
# ACC-cyber: 0.1042
# ACC-cyber-answered: 0.3913
# Percentage-cyber-answered: 0.2662

# python3 ./evaluation/wmdp/generate_wmdp_responses.py \
#   --ckpt_dir "HuggingFaceH4/zephyr-7b-beta" \
#   --data_dir "."

# python3 ./evaluation/wmdp/cal_wmdp_result.py \
#   --file_name "run_results_.json"

# ACC-biology: 0.6630
# ACC-biology-answered: 0.6651
# Percentage-biology-answered: 0.9969
# -----------------
# ACC-cyber: 0.4197
# ACC-cyber-answered: 0.4360
# Percentage-cyber-answered: 0.9628

# python3 ./evaluation/MMLU/generate_mmlu_responses.py \
#   --ckpt_dir "cais/Zephyr_RMU" \
#   --data_dir "data/MMLU"

# python3 ./evaluation/MMLU/cal_mmlu_result.py \
#   --file_name "run_results_.json"

# ACC-biology: 0.5882
# ACC-biology-answered: 0.6316
# Percentage-biology-answered: 0.9251
# -----------------
# ACC-other: 0.5720
# ACC-other-answered: 0.5940
# Percentage-other-answered: 0.9627
# -----------------
# ACC-all_subjects: 0.5749
# ACC-all_subjects-answered: 0.6006
# Percentage-all_subjects-answered: 0.9561

# python3 ./evaluation/MMLU/generate_mmlu_responses.py \
#   --ckpt_dir "HuggingFaceH4/zephyr-7b-beta" \
#   --data_dir "data/MMLU"

# python3 ./evaluation/MMLU/cal_mmlu_result.py \
#   --file_name "run_results_.json"

# ACC-biology: 0.6448
# ACC-biology-answered: 0.6505
# Percentage-biology-answered: 0.9913
# -----------------
# ACC-other: 0.5769
# ACC-other-answered: 0.5943
# Percentage-other-answered: 0.9704
# -----------------
# ACC-all_subjects: 0.5888
# ACC-all_subjects-answered: 0.6041
# Percentage-all_subjects-answered: 0.9741