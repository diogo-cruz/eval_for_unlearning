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
model="baulab/elm-zephyr-7b-beta"
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


python3 inference.py --ckpt_dir $model --data_dir "data/wmdp/test/" --dataset_name "bio_questions"
python3 inference.py --ckpt_dir $model --data_dir "data/tinyMMLU/test/" --dataset_name "questions"