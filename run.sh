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

# =================================================================================================
# =================================================================================================
# =================================================================================================
# =================================================================================================
# =================================================================================================
# =================================================================================================
# echo "Running eval for Zephyr_RMU on tinyMMLU..."
# python3 ./evaluation/MMLU/generate_mmlu_responses.py \
#   --ckpt_dir "cais/Zephyr_RMU" \
#   --data_dir "data/tinyMMLU" \

# mv "run_results_.json" "results/tinyMMLU_0_shot_zephyr_rmu_run_results_.json"
# mv "run_breakpoint_.json" "results/tinyMMLU_0_shot_zephyr_rmu_run_breakpoint_.json"

# python3 ./evaluation/MMLU/cal_mmlu_result.py \
#   --file_name "results/tinyMMLU_0_shot_zephyr_rmu_run_results_.json"

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

# echo "Running eval for Zephyr_7b_beta on tinyMMLU..."
# python3 ./evaluation/MMLU/generate_mmlu_responses.py \
#   --ckpt_dir "HuggingFaceH4/zephyr-7b-beta" \
#   --data_dir "data/tinyMMLU" \

# mv "run_results_.json" "results/tinyMMLU_0_shot_zephyr_7b_beta_run_results_.json"
# mv "run_breakpoint_.json" "results/tinyMMLU_0_shot_zephyr_7b_beta_run_breakpoint_.json"

# python3 ./evaluation/MMLU/cal_mmlu_result.py \
#   --file_name "results/tinyMMLU_0_shot_zephyr_7b_beta_run_results_.json"

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

python3 ./evaluation/MMLU/cal_mmlu_result_rephrasing.py \
  --file_name "run_results__rephrasing.json"

mv "run_results__rephrasing.json" "results/tinyMMLU_0_shot_zephyr_rmu_run_results__rephrased.json"
mv "run_breakpoint__rephrasing.json" "results/tinyMMLU_0_shot_zephyr_rmu_run_breakpoint__rephrased.json"

Printing results from: data_translated_french
ACC-biology: 0.5150
ACC-biology-answered: 0.5150
Percentage-biology-answered: 0.9000
-----------------
ACC-other: 0.5915
ACC-other-answered: 0.5915
Percentage-other-answered: 1.0000
-----------------
ACC-all_subjects: 0.5749
ACC-all_subjects-answered: 0.5749
Percentage-all_subjects-answered: 0.9783
-----------------
Printing results from: data_translated_german
ACC-biology: 0.4817
ACC-biology-answered: 0.4817
Percentage-biology-answered: 0.9000
-----------------
ACC-other: 0.6563
ACC-other-answered: 0.6725
Percentage-other-answered: 0.9792
-----------------
ACC-all_subjects: 0.6183
ACC-all_subjects-answered: 0.6310
Percentage-all_subjects-answered: 0.9620
-----------------
Printing results from: data_translated_hindi
ACC-biology: 0.4067
ACC-biology-answered: 0.4400
Percentage-biology-answered: 0.9667
-----------------
ACC-other: 0.3438
ACC-other-answered: 0.3438
Percentage-other-answered: 0.9861
-----------------
ACC-all_subjects: 0.3575
ACC-all_subjects-answered: 0.3647
Percentage-all_subjects-answered: 0.9819
-----------------
Printing results from: data_translated_korean
ACC-biology: 0.4367
ACC-biology-answered: 0.4367
Percentage-biology-answered: 0.9000
-----------------
ACC-other: 0.5768
ACC-other-answered: 0.5768
Percentage-other-answered: 0.9722
-----------------
ACC-all_subjects: 0.5463
ACC-all_subjects-answered: 0.5463
Percentage-all_subjects-answered: 0.9565
-----------------
Printing results from: data_translated_arabic
ACC-biology: 0.3483
ACC-biology-answered: 0.3483
Percentage-biology-answered: 1.0000
-----------------
ACC-other: 0.4688
ACC-other-answered: 0.4688
Percentage-other-answered: 0.9861
-----------------
ACC-all_subjects: 0.4426
ACC-all_subjects-answered: 0.4426
Percentage-all_subjects-answered: 0.9891
-----------------
Printing results from: data_translated_czech
ACC-biology: 0.3400
ACC-biology-answered: 0.3400
Percentage-biology-answered: 1.0000
-----------------
ACC-other: 0.5807
ACC-other-answered: 0.5807
Percentage-other-answered: 0.9722
-----------------
ACC-all_subjects: 0.5283
ACC-all_subjects-answered: 0.5283
Percentage-all_subjects-answered: 0.9783
-----------------
Printing results from: data_translated_bengali
ACC-biology: 0.2483
ACC-biology-answered: 0.2483
Percentage-biology-answered: 0.9000
-----------------
ACC-other: 0.3744
ACC-other-answered: 0.3744
Percentage-other-answered: 1.0000
-----------------
ACC-all_subjects: 0.3470
ACC-all_subjects-answered: 0.3470
Percentage-all_subjects-answered: 0.9783
-----------------
Printing results from: data_translated_vietnamese
ACC-biology: 0.2783
ACC-biology-answered: 0.2783
Percentage-biology-answered: 0.8000
-----------------
ACC-other: 0.5385
ACC-other-answered: 0.5385
Percentage-other-answered: 0.9583
-----------------
ACC-all_subjects: 0.4819
ACC-all_subjects-answered: 0.4819
Percentage-all_subjects-answered: 0.9239
-----------------
Printing results from: data_translated_turkish
ACC-biology: 0.2667
ACC-biology-answered: 0.2667
Percentage-biology-answered: 1.0000
-----------------
ACC-other: 0.5290
ACC-other-answered: 0.5313
Percentage-other-answered: 0.9792
-----------------
ACC-all_subjects: 0.4720
ACC-all_subjects-answered: 0.4738
Percentage-all_subjects-answered: 0.9837
-----------------
Printing results from: data_translated_telugu
ACC-biology: 0.4533
ACC-biology-answered: 0.4533
Percentage-biology-answered: 1.0000
-----------------
ACC-other: 0.3202
ACC-other-answered: 0.3202
Percentage-other-answered: 0.9861
-----------------
ACC-all_subjects: 0.3491
ACC-all_subjects-answered: 0.3491
Percentage-all_subjects-answered: 0.9891
-----------------
Printing results from: data_translated_farsi
ACC-biology: 0.2733
ACC-biology-answered: 0.2733
Percentage-biology-answered: 1.0000
-----------------
ACC-other: 0.4600
ACC-other-answered: 0.4600
Percentage-other-answered: 0.9861
-----------------
ACC-all_subjects: 0.4194
ACC-all_subjects-answered: 0.4194
Percentage-all_subjects-answered: 0.9891