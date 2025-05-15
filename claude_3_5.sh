#!/bin/bash
set -xe

# Rephrasing with different languages
for lang in Hindi Bengali Arabic Czech French German Korean Vietnamese Turkish Telugu Farsi; do
  python3 evaluation/rephrase_prompts_claude_3_5.py --task "bio" --prompt_technique_name "translating_to_language" --language "$lang" &
done

# Standard prompt techniques (no language)
python3 evaluation/rephrase_prompts_claude_3_5.py --task "bio" --prompt_technique_name "rephrase_as_conversation" &
python3 evaluation/rephrase_prompts_claude_3_5.py --task "bio" --prompt_technique_name "rephrase_as_poem" &
python3 evaluation/rephrase_prompts_claude_3_5.py --task "bio" --prompt_technique_name "removing_technical_terms_from_the_question" &
python3 evaluation/rephrase_prompts_claude_3_5.py --task "bio" --prompt_technique_name "replacing_technical_terms_with_variables" &

# Filler text variants
python3 evaluation/rephrase_prompts_claude_3_5.py --task "bio" --prompt_technique_name "filler_text" --language "english" &
python3 evaluation/rephrase_prompts_claude_3_5.py --task "bio" --prompt_technique_name "filler_text" --language "latin" &
python3 evaluation/rephrase_prompts_claude_3_5.py --task "bio" --prompt_technique_name "filler_text" --language "hindi" &

wait
