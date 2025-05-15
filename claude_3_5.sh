#!/bin/bash
set -e

SCRIPT="evaluation/rephrase_prompts_claude_3_5.py"

# Helper to run a job without logging
run_job() {
  NAME="$1"
  shift

  # Start the actual job
  echo "▶️ [$NAME] Starting at $(date)"
  stdbuf -oL -eL python3 "$SCRIPT" "$@"
  
  # Notify when job is complete
  echo "✅ [$NAME] Completed at $(date)"
}

# Rephrasing with translation
for lang in Hindi Bengali Arabic Czech French German Korean Vietnamese Turkish Telugu Farsi; do
  run_job "translating_to_language_${lang,,}" \
    --data "wmdp" \
    --task "bio" \
    --prompt_technique_name "translating_to_language" \
    --language "$lang"
done

# Other rephrasing techniques
for technique in \
  rephrase_as_conversation \
  rephrase_as_poem \
  removing_technical_terms_from_the_question \
  replacing_technical_terms_with_variables; do
  run_job "$technique" \
    --data "wmdp" \
    --task "bio" \
    --prompt_technique_name "$technique"
done

# # Filler text variants
# for lang in english latin hindi; do
#   run_job "filler_text_${lang,,}" \
#     --data "wmdp" \
#     --task "bio" \
#     --prompt_technique_name "filler_text" \
#     --language "$lang"
# done

echo -e "\n🎉 All jobs completed."
