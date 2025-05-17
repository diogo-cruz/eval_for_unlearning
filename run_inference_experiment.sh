set -xe

# python3 inference.py --ckpt_dir "cais/Zephyr_RMU" --data_dir "data/wmdp_rephrased/data_english_filler_text/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir "cais/Zephyr_RMU" --data_dir "data/wmdp_rephrased/data_latin_filler_text/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir "cais/Zephyr_RMU" --data_dir "data/wmdp_rephrased/data_hindi_filler_text/test/" --dataset_name "bio_questions"

# python3 inference.py --ckpt_dir "cais/Zephyr_RMU" --data_dir "data/wmdp_rephrased/data_rephrased_conversation/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir "cais/Zephyr_RMU" --data_dir "data/wmdp_rephrased/data_rephrased_poem/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir "cais/Zephyr_RMU" --data_dir "data/wmdp_rephrased/data_replaced_with_variables/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir "cais/Zephyr_RMU" --data_dir "data/wmdp_rephrased/data_technical_terms_removed_1/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir "cais/Zephyr_RMU" --data_dir "data/wmdp_rephrased/data_translated_arabic/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir "cais/Zephyr_RMU" --data_dir "data/wmdp_rephrased/data_translated_bengali/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir "cais/Zephyr_RMU" --data_dir "data/wmdp_rephrased/data_translated_czech/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir "cais/Zephyr_RMU" --data_dir "data/wmdp_rephrased/data_translated_farsi/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir "cais/Zephyr_RMU" --data_dir "data/wmdp_rephrased/data_translated_french/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir "cais/Zephyr_RMU" --data_dir "data/wmdp_rephrased/data_translated_german/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir "cais/Zephyr_RMU" --data_dir "data/wmdp_rephrased/data_translated_hindi/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir "cais/Zephyr_RMU" --data_dir "data/wmdp_rephrased/data_translated_korean/test/" --dataset_name "bio_questions"

# python3 inference.py --ckpt_dir "cais/Zephyr_RMU" --data_dir "data/wmdp_rephrased/data_translated_telugu/test/" --dataset_name "bio_questions"

# python3 inference.py --ckpt_dir "cais/Zephyr_RMU" --data_dir "data/wmdp_rephrased/data_translated_turkish/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir "cais/Zephyr_RMU" --data_dir "data/wmdp_rephrased/data_translated_vietnamese/test/" --dataset_name "bio_questions"


# python3 inference.py --ckpt_dir "cais/Zephyr_RMU" --data_dir "data/claude_3_5/data_translated_bengali/test/" --dataset_name "bio_questions"

# python3 inference.py --ckpt_dir "cais/Zephyr_RMU" --data_dir "data/tinyMMLU/test/" --dataset_name "questions"
# python3 inference.py --ckpt_dir "HuggingFaceH4/zephyr-7b-beta" --data_dir "data/tinyMMLU/test/" --dataset_name "questions"
# python3 inference.py --ckpt_dir "HuggingFaceH4/zephyr-7b-beta" --data_dir "data/wmdp/test/" --dataset_name "bio_questions"


## ELM
# model="baulab/elm-zephyr-7b-beta"
# python3 inference.py --ckpt_dir $model --data_dir "data/wmdp_rephrased/data_english_filler_text/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir $model --data_dir "data/wmdp_rephrased/data_latin_filler_text/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir $model --data_dir "data/wmdp_rephrased/data_hindi_filler_text/test/" --dataset_name "bio_questions"

# python3 inference.py --ckpt_dir $model --data_dir "data/wmdp_rephrased/data_rephrased_conversation/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir $model --data_dir "data/wmdp_rephrased/data_rephrased_poem/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir $model --data_dir "data/wmdp_rephrased/data_replaced_with_variables/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir $model --data_dir "data/wmdp_rephrased/data_technical_terms_removed_1/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir $model --data_dir "data/wmdp_rephrased/data_translated_arabic/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir $model --data_dir "data/wmdp_rephrased/data_translated_bengali/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir $model --data_dir "data/wmdp_rephrased/data_translated_czech/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir $model --data_dir "data/wmdp_rephrased/data_translated_farsi/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir $model --data_dir "data/wmdp_rephrased/data_translated_french/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir $model --data_dir "data/wmdp_rephrased/data_translated_german/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir $model --data_dir "data/wmdp_rephrased/data_translated_hindi/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir $model --data_dir "data/wmdp_rephrased/data_translated_korean/test/" --dataset_name "bio_questions"

# python3 inference.py --ckpt_dir "cais/Zephyr_RMU" --data_dir "data/wmdp_rephrased/data_translated_telugu/test/" --dataset_name "bio_questions"

# python3 inference.py --ckpt_dir $model --data_dir "data/wmdp_rephrased/data_translated_turkish/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir $model --data_dir "data/wmdp_rephrased/data_translated_vietnamese/test/" --dataset_name "bio_questions"


# python3 inference.py --ckpt_dir $model --data_dir "data/wmdp/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir $model --data_dir "data/tinyMMLU/test/" --dataset_name "questions"


# python3 inference.py --ckpt_dir "cais/Zephyr_RMU" --data_dir "data/wmdp_rephrased_rmu/data_english_filler_text/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir "cais/Zephyr_RMU" --data_dir "data/wmdp_rephrased_rmu/data_latin_filler_text/test/" --dataset_name "bio_questions"
# python3 inference.py --ckpt_dir "cais/Zephyr_RMU" --data_dir "data/wmdp_rephrased_rmu/data_replaced_with_variables/test/" --dataset_name "bio_questions"



# lm_eval --model hf \
#   --model_args pretrained=cais/Zephyr_RMU,dtype="bfloat16" \
#   --tasks wmdp_bio_rephrased_english_filler,wmdp_bio_rephrased_hindi_filler,wmdp_bio_rephrased_latin_filler,wmdp_bio_rephrased_conversation,wmdp_bio_rephrased_poem,wmdp_bio_rephrased_replace_with_variables,wmdp_bio_rephrased_technical_terms_removed_1,wmdp_bio_rephrased_translated_arabic,wmdp_bio_rephrased_translated_bengali,wmdp_bio_rephrased_translated_czech,wmdp_bio_rephrased_translated_farsi,wmdp_bio_rephrased_translated_german,wmdp_bio_rephrased_translated_hindi,wmdp_bio_rephrased_translated_korean,wmdp_bio_rephrased_translated_turkish,wmdp_bio_rephrased_translated_vietnamese,wmdp_bio_rephrased_translated_french

lm_eval --model hf \
  --model_args pretrained=cais/Zephyr_RMU,dtype="bfloat16" \
  --tasks wmdp_bio 