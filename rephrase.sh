set -e 

PYTHONPATH="."

python3 evaluation/rephrase_prompts.py --data "tinyMMLU" --prompt_technique_name "translating_to_language" --language "Arabic"
python3 evaluation/rephrase_prompts.py --data "tinyMMLU" --prompt_technique_name "translating_to_language" --language "Czech"
python3 evaluation/rephrase_prompts.py --data "tinyMMLU" --prompt_technique_name "translating_to_language" --language "French"
python3 evaluation/rephrase_prompts.py --data "tinyMMLU" --prompt_technique_name "translating_to_language" --language "German"
python3 evaluation/rephrase_prompts.py --data "tinyMMLU" --prompt_technique_name "translating_to_language" --language "Hindi"
python3 evaluation/rephrase_prompts.py --data "tinyMMLU" --prompt_technique_name "translating_to_language" --language "Korean"
python3 evaluation/rephrase_prompts.py --data "tinyMMLU" --prompt_technique_name "translating_to_language" --language "Bengali"
python3 evaluation/rephrase_prompts.py --data "tinyMMLU" --prompt_technique_name "translating_to_language" --language "Vietnamese"
python3 evaluation/rephrase_prompts.py --data "tinyMMLU" --prompt_technique_name "translating_to_language" --language "Turkish"
python3 evaluation/rephrase_prompts.py --data "tinyMMLU" --prompt_technique_name "translating_to_language" --language "Telugu"
python3 evaluation/rephrase_prompts.py --data "tinyMMLU" --prompt_technique_name "translating_to_language" --language "Farsi"

