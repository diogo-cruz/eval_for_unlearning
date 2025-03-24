set -xe

## 0-shot
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
#   --data_dir "data/tinyMMLU" 

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

## 5-shot
### by default uses the dev set of subject being evaluated
# python3 ./evaluation/MMLU/generate_mmlu_responses.py \
#   --ckpt_dir "cais/Zephyr_RMU" \
#   --data_dir "data/MMLU" \
#   --ntrain 5

# mv "run_results_.json" "results/mmlu_5_shot_zephyr_rmu_run_results_.json"
# mv "run_breakpoint_.json" "results/mmlu_5_shot_zephyr_rmu_run_breakpoint_.json"

# python3 ./evaluation/MMLU/cal_mmlu_result.py \
#   --file_name "results/mmlu_5_shot_zephyr_rmu_run_results_.json"

# ACC-biology: 0.5555
# ACC-biology-answered: 0.5607
# Percentage-biology-answered: 0.8932
# -----------------
# ACC-other: 0.5792
# ACC-other-answered: 0.5841
# Percentage-other-answered: 0.9821
# -----------------
# ACC-all_subjects: 0.5750
# ACC-all_subjects-answered: 0.5800
# Percentage-all_subjects-answered: 0.9665

# python3 ./evaluation/MMLU/generate_mmlu_responses.py \
#   --ckpt_dir "HuggingFaceH4/zephyr-7b-beta" \
#   --data_dir "data/MMLU" \
#   --ntrain 5

# mv "run_results_.json" "results/mmlu_5_shot_zephyr_7b_beta_run_results_.json"
# mv "run_breakpoint_.json" "results/mmlu_5_shot_zephyr_7b_beta_run_breakpoint_.json"

# python3 ./evaluation/MMLU/cal_mmlu_result.py \
#   --file_name "results/mmlu_5_shot_zephyr_7b_beta_run_results_.json"

# ACC-biology: 0.6517
# ACC-biology-answered: 0.6545
# Percentage-biology-answered: 0.9958
# -----------------
# ACC-other: 0.6020
# ACC-other-answered: 0.6037
# Percentage-other-answered: 0.9972
# -----------------
# ACC-all_subjects: 0.6107
# ACC-all_subjects-answered: 0.6126
# Percentage-all_subjects-answered: 0.9970

## rephrasing + 0-shot
# python3 ./evaluation/MMLU/generate_mmlu_responses_rephrasing.py \
#   --ckpt_dir "HuggingFaceH4/zephyr-7b-beta" \
#   --data_dir "data/MMLU-rephrased" \

# mv "run_results_.json" "results/mmlu_rephrased_0_shot_zephyr_7b_beta_run_results_.json"
# mv "run_breakpoint_.json" "results/mmlu_rephrased_0_shot_zephyr_7b_beta_run_breakpoint_.json"


# python3 ./evaluation/wmdp/generate_wmdp_responses_rephrasing.py \
#   --ckpt_dir "cais/Zephyr_RMU" \
#   --data_dir "data/wmdp-rephrased" \

# mv "run_results__rephrasing.json" "results/wmdp_0_shot_zephyr_rmu_run_results__rephrasing.json"
# mv "run_breakpoint__rephrasing.json" "results/wmdp_0_shot_zephyr_rmu_run_breakpoint__rephrasing.json"

# python3 ./evaluation/wmdp/cal_wmdp_result_rephrasing.py \
#   --file_name "results/wmdp_0_shot_zephyr_rmu_run_results__rephrasing.json"

# ACC-biology: 0.1037
# ACC-biology-answered: 0.3367
# Percentage-biology-answered: 0.3079

# python3 ./evaluation/MMLU/generate_mmlu_responses_rephrasing.py \
#   --ckpt_dir "HuggingFaceH4/zephyr-7b-beta" \
#   --data_dir "data/MMLU-rephrased" \

# mv "run_results__rephrasing.json" "results/mmlu_0_shot_zephyr_7b_beta_run_results__rephrasing.json"
# mv "run_breakpoint__rephrasing.json" "results/mmlu_0_shot_zephyr_7b_beta_run_breakpoint__rephrasing.json"

# python3 ./evaluation/MMLU/cal_mmlu_result_rephrasing.py \
#   --file_name "results/mmlu_0_shot_zephyr_7b_beta_run_results__rephrasing.json"


# python3 ./evaluation/MMLU/generate_mmlu_responses_rephrasing.py \
#   --ckpt_dir "cais/Zephyr_RMU" \
#   --data_dir "data/MMLU-rephrased" \

# mv "run_results__rephrasing.json" "results/mmlu_0_shot_zephyr_rmu_run_results__rephrasing.json"
# mv "run_breakpoint__rephrasing.json" "results/mmlu_0_shot_zephyr_rmu_run_breakpoint__rephrasing.json"

# python3 ./evaluation/MMLU/cal_mmlu_result_rephrasing.py \
#   --file_name "results/mmlu_0_shot_zephyr_rmu_run_results__rephrasing.json"

## need to do below on both base and rmu
# python3 ./evaluation/wmdp/generate_wmdp_responses_rephrasing.py \
#   --ckpt_dir "HuggingFaceH4/zephyr-7b-beta" \
#   --data_dir "data/wmdp-rephrased" \

# mv "run_results__rephrasing.json" "results/wmdp_0_shot_zephyr_7b_beta_run_results__rephrasing.json"
# mv "run_breakpoint__rephrasing.json" "results/wmdp_0_shot_zephyr_7b_beta_run_breakpoint__rephrasing.json"

# python3 ./evaluation/wmdp/cal_wmdp_result_rephrasing.py \
#   --file_name "results/wmdp_0_shot_zephyr_7b_beta_run_results__rephrasing.json"

# python3 ./evaluation/wmdp/generate_wmdp_responses_rephrasing.py \
#   --ckpt_dir "cais/Zephyr_RMU" \
#   --data_dir "data/wmdp-rephrased" \

# mv "run_results__rephrasing.json" "results/wmdp_0_shot_zephyr_rmu_run_results__rephrasing.json"
# mv "run_breakpoint__rephrasing.json" "results/wmdp_0_shot_zephyr_rmu_run_breakpoint__rephrasing.json"

# python3 ./evaluation/wmdp/cal_wmdp_result_rephrasing.py \
#   --file_name "results/wmdp_0_shot_zephyr_rmu_run_results__rephrasing.json"

# ---
echo "Running eval for Zephyr_RMU on tinyMMLU..."
python3 ./evaluation/MMLU/generate_mmlu_responses.py \
  --ckpt_dir "cais/Zephyr_RMU" \
  --data_dir "data/tinyMMLU" \

mv "run_results_.json" "results/tinyMMLU_0_shot_zephyr_rmu_run_results_.json"
mv "run_breakpoint_.json" "results/tinyMMLU_0_shot_zephyr_rmu_run_breakpoint_.json"

python3 ./evaluation/MMLU/cal_mmlu_result.py \
  --file_name "results/tinyMMLU_0_shot_zephyr_rmu_run_results_.json"

# ACC-biology: 0.6100
# ACC-biology-answered: 0.6100
# Percentage-biology-answered: 0.9000
# -----------------
# ACC-other: 0.5660
# ACC-other-answered: 0.5938
# Percentage-other-answered: 0.9074
# -----------------
# ACC-all_subjects: 0.5756
# ACC-all_subjects-answered: 0.5973
# Percentage-all_subjects-answered: 0.9058

echo "Running eval for Zephyr_7b_beta on tinyMMLU..."
python3 ./evaluation/MMLU/generate_mmlu_responses.py \
  --ckpt_dir "HuggingFaceH4/zephyr-7b-beta" \
  --data_dir "data/tinyMMLU" \

mv "run_results_.json" "results/tinyMMLU_0_shot_zephyr_7b_beta_run_results_.json"
mv "run_breakpoint_.json" "results/tinyMMLU_0_shot_zephyr_7b_beta_run_breakpoint_.json"

python3 ./evaluation/MMLU/cal_mmlu_result.py \
  --file_name "results/tinyMMLU_0_shot_zephyr_7b_beta_run_results_.json"

# ACC-biology: 0.7300
# ACC-biology-answered: 0.7300
# Percentage-biology-answered: 1.0000
# -----------------
# ACC-other: 0.5383
# ACC-other-answered: 0.5660
# Percentage-other-answered: 0.9352
# -----------------
# ACC-all_subjects: 0.5799
# ACC-all_subjects-answered: 0.6017
# Percentage-all_subjects-answered: 0.9493


echo "Running eval for Zephyr_RMU on tinyMMLU-rephrased..."
python3 ./evaluation/MMLU/generate_mmlu_responses_rephrasing.py \
  --ckpt_dir "cais/Zephyr_RMU" \
  --data_dir "data/tinyMMLU-rephrased" \

mv "run_results_.json" "results/tinyMMLU_0_shot_zephyr_rmu_run_results__rephrased.json"
mv "run_breakpoint_.json" "results/tinyMMLU_0_shot_zephyr_rmu_run_breakpoint__rephrased.json"

python3 ./evaluation/MMLU/cal_mmlu_result_rephrasing.py \
  --file_name "results/tinyMMLU_0_shot_zephyr_rmu_run_results__rephrased.json"