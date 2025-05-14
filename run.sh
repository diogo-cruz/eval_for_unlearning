#!/bin/bash
set -e 

if [ ! -d "lm-evaluation-harness" ]; then
  git clone --depth 1 https://github.com/EleutherAI/lm-evaluation-harness
  cd lm-evaluation-harness
  uv pip install -e .
  cd ..
fi

if [ ! -d "lm-evaluation-harness/lm_eval/tasks/wmdp_rephrased" ]; then
  echo "Copying wmdp_rephrased tasks to lm-evaluation-harness..."
  mkdir -p lm-evaluation-harness/lm_eval/tasks/wmdp_rephrased
  cp -r custom_tasks/wmdp_lm_eval_tasks/* lm-evaluation-harness/lm_eval/tasks/wmdp_rephrased
fi

# export LOGLEVEL=DEBUG




# models="models.txt"
# if [ ! -f "$models" ]; then
#   echo "Error: File $models not found"
#   exit 1
# fi

# while IFS= read -r model; do
#   # Skip empty lines and comments
#   [[ -z "$model" || "$model" =~ ^#.*$ ]] && continue

#   echo "Processing model: $model"
#   lm_eval --model hf --model_args pretrained=$model,dtype="bfloat16" \
#     --output ./results --log_sample \
#     --tasks tinyMMLU
#     # --tasks wmdp_bio,wmdp_bio_rephrased_english_filler,wmdp_bio_rephrased_hindi_filler,wmdp_bio_rephrased_latin_filler,wmdp_bio_rephrased_conversation,wmdp_bio_rephrased_poem,wmdp_bio_rephrased_replace_with_variables,wmdp_bio_rephrased_technical_terms_removed_1,wmdp_bio_rephrased_translated_farsi,wmdp_bio_rephrased_translated_german,wmdp_bio_rephrased_translated_korean

#   done < "$models"
# exit 1

# example for wmdp_rephrased tasks
# lm_eval --model hf --model_args pretrained=LLM-GAT/llama-3-8b-instruct-elm-checkpoint-8,dtype="bfloat16" \
#   --output ./results --log_sample \
#   --tasks wmdp_bio,wmdp_bio_rephrased_english_filler,wmdp_bio_rephrased_hindi_filler,wmdp_bio_rephrased_latin_filler,wmdp_bio_rephrased_conversation,wmdp_bio_rephrased_poem,wmdp_bio_rephrased_replace_with_variables,wmdp_bio_rephrased_technical_terms_removed_1,wmdp_bio_rephrased_translated_farsi,wmdp_bio_rephrased_translated_german,wmdp_bio_rephrased_translated_korean,tinyMMLU


# example for ReNeLLM tasks
# lm_eval --model hf --model_args pretrained=LLM-GAT/llama-3-8b-instruct-elm-checkpoint-8,dtype="bfloat16" \
# lm_eval --model hf --model_args pretrained=cais/Zephyr_RMU,dtype="bfloat16" \
#   --output ./results --log_sample \
#   --tasks wmdp_bio_renellm_addChar_full

# cp -r wmdp_bio_mmlu_tasks lm-evaluation-harness/lm_eval/tasks
# cp -r wmdp_bio_retain_tasks lm-evaluation-harness/lm_eval/tasks

# declare -a n_shots=(0 1 3 5 10 20)
# for n_shot in "${n_shots[@]}"; do
#   # lm_eval --model hf --model_args pretrained=HuggingFaceH4/zephyr-7b-beta,dtype="bfloat16" \
#   # lm_eval --model hf --model_args pretrained=LLM-GAT/llama-3-8b-instruct-elm-checkpoint-8,dtype="bfloat16" \
#   lm_eval --model hf --model_args pretrained=cais/Zephyr_RMU,dtype="bfloat16" \
#     --output "./results_cross_task/$n_shot-shot" \
#     --log_sample --tasks wmdp_bio_retain --num_fewshot $n_shot 
# done

# for "truly unlearning" models, need to set total_steps in adapter_config.json (e.g. 1000)
lm_eval --model hf \
  --model_args pretrained=HuggingFaceH4/zephyr-7b-beta,peft="./LLMU results/WMDP Dataset /Zephyr/50368626_checkpoint_1000/zephyr-7b-beta_unlearned_24_checkpoint_1000_peft",dtype="float16" \
  --tasks  wmdp_bio,wmdp_bio_rephrased_english_filler,wmdp_bio_rephrased_hindi_filler,wmdp_bio_rephrased_latin_filler,wmdp_bio_rephrased_conversation,wmdp_bio_rephrased_poem,wmdp_bio_rephrased_replace_with_variables,wmdp_bio_rephrased_technical_terms_removed_1,wmdp_bio_rephrased_translated_farsi,wmdp_bio_rephrased_translated_german,wmdp_bio_rephrased_translated_korean
  
  #tinyMMLU


### How to run erasure script
Run WMDP eval script:
```python
python3 knowledge_erasure/evaluation/wmdp/generate_wmdp_responses.py --ckpt_dir LLMU\ results/WMDP\ Dataset\ /Zephyr/50368626_checkpoint_1000/zephyr-7b-beta_unlearned_24_checkpoint_1000_peft/ --data_dir data/wmdp --peft_model --extra_info "llmu_wmdp_bio"
python3 knowledge_erasure/evaluation/wmdp/cal_wmdp_result.py --file_name "erasure_results/run_results_llmu_wmdp_bio.json"
```
Run WMDP eval scripts for rephrased tasks:
```python
python3 knowledge_erasure/evaluation/wmdp/generate_wmdp_responses_rephrasing.py --ckpt_dir LLMU\ results/WMDP\ Dataset\ /Zephyr/50368626_checkpoint_1000/zephyr-7b-beta_unlearned_24_checkpoint_1000_peft/ --data_dir data/wmdp_rephrased_copy --peft_model --extra_info "llmu_wmdp_bio_rephrased"
# python3 knowledge_erasure/evaluation/wmdp/generate_wmdp_responses_rephrasing.py --ckpt_dir LLMU\ results/Biology\ Dataset\ /Zephyr/48079515/ --data_dir data/wmdp_rephrased_copy --peft_model --extra_info "llmu_wmdp_bio_rephrased"
python3 knowledge_erasure/evaluation/wmdp/cal_wmdp_result_rephrasing.py --file_name "erasure_results/run_results_llmu_wmdp_bio_rephrased_rephrasing.json"
```

Run tinyMMLU eval script:
```python
python3 knowledge_erasure/evaluation/wmdp/generate_wmdp_responses.py --ckpt_dir LLMU\ results/WMDP\ Dataset\ /Zephyr/50368626_checkpoint_1000/zephyr-7b-beta_unlearned_24_checkpoint_1000_peft/ --data_dir data/wmdp --peft_model --extra_info "llmu_wmdp_bio"
```

# Run MMLU eval script:
# ```python
# python3 knowledge_erasure/evaluation/MMLU/generate_mmlu_responses.py --ckpt_dir LLMU\ results/WMDP\ Dataset\ /Zephyr/50368626_checkpoint_1000/zephyr-7b-beta_unlearned_24_checkpoint_1000_peft/ --data_dir data/MMLU --peft_model --extra_info "llmu_mmlu"
# ```