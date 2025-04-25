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
  cp -r wmdp_lm_eval_tasks/* lm-evaluation-harness/lm_eval/tasks/wmdp_rephrased
fi

export LOGLEVEL=DEBUG

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
lm_eval --model hf --model_args pretrained=cais/Zephyr_RMU,dtype="bfloat16" \
  --output ./results --log_sample \
  --tasks wmdp_bio_renellm_addChar_full