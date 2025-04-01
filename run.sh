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
# example below creates a log file
# lm_eval --model hf --model_args pretrained=HuggingFaceH4/zephyr-7b-beta --tasks wmdp --limit 10 --output output/wmdp/ --log_samples

# python3 -m eval.eval \
#   --model zephyr_7b_beta \
#   --tasks wmdp_bio wmdp_bio_rephrased_english_filler wmdp_bio_rephrased_hindi_filler wmdp_bio_rephrased_latin_filler wmdp_bio_rephrased_conversation wmdp_bio_rephrased_poem wmdp_bio_rephrased_replace_with_variables wmdp_bio_rephrased_technical_terms_removed_1 wmdp_bio_rephrased_translated_arabic wmdp_bio_rephrased_translated_bengali wmdp_bio_rephrased_translated_czech wmdp_bio_rephrased_translated_farsi wmdp_bio_rephrased_translated_french wmdp_bio_rephrased_translated_german wmdp_bio_rephrased_translated_hindi wmdp_bio_rephrased_translated_korean wmdp_bio_rephrased_translated_telugu wmdp_bio_rephrased_translated_turkish wmdp_bio_rephrased_translated_vietnamese \
#   --output output/wmdp_rephrased \
#   --log_samples

[ ! -f .env ] || export $(grep -v '^#' .env | xargs)

HF_TOKEN=$HF_TOKEN
# MODEL="mistral_7b_v0.1"
# MODEL="llama3_8b_instruct_elm"
# MODEL="llama3_8b_elm"
MODEL="llama3_8b"

python3 -m eval.eval --model $MODEL --tasks wmdp_bio --output output/wmdp --log_samples --hf_token $HF_TOKEN
python3 -m eval.eval --model $MODEL --output output/wmdp_rephrased --log_samples --hf_token $HF_TOKEN \
  --tasks wmdp_bio_rephrased_english_filler wmdp_bio_rephrased_hindi_filler wmdp_bio_rephrased_latin_filler wmdp_bio_rephrased_conversation wmdp_bio_rephrased_poem wmdp_bio_rephrased_replace_with_variables wmdp_bio_rephrased_technical_terms_removed_1 wmdp_bio_rephrased_translated_farsi  wmdp_bio_rephrased_translated_german wmdp_bio_rephrased_translated_korean