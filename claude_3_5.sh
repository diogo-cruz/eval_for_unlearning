#!/bin/bash
set -xe

LOG_DIR="logs"
mkdir -p "$LOG_DIR"

SCRIPT="evaluation/rephrase_prompts_claude_3_5.py"

# Translating to various languages
for lang in Hindi Bengali Arabic Czech French German Korean Vietnamese Turkish Telugu Farsi; do
  LOG_FILE="$LOG_DIR/rephrase_translating_to_language_${lang,,}.log"
  python3 "$SCRIPT" \
    --data "wmdp" \
    --task "bio" \
    --prompt_technique_name "translating_to_language" \
    --language "$lang" > "$LOG_FILE" 2>&1 &
done

# Standard prompt techniques (no language)
for technique in \
  rephrase_as_conversation \
  rephrase_as_poem \
  removing_technical_terms_from_the_question \
  replacing_technical_terms_with_variables; do
  LOG_FILE="$LOG_DIR/rephrase_${technique}.log"
  python3 "$SCRIPT" \
    --data "wmdp" \
    --task "bio" \
    --prompt_technique_name "$technique" > "$LOG_FILE" 2>&1 &
done

# Filler text variants
for lang in english latin hindi; do
  LOG_FILE="$LOG_DIR/rephrase_filler_text_${lang,,}.log"
  python3 "$SCRIPT" \
    --data "wmdp" \
    --task "bio" \
    --prompt_technique_name "filler_text" \
    --language "$lang" > "$LOG_FILE" 2>&1 &
done

wait

# --- Error Detection ---
echo "✅ All jobs completed. Checking for errors..."

FAIL_COUNT=0

for log in logs/*.log; do
  if grep -Ei "error|exception|traceback" "$log" > /dev/null; then
    echo "❌ Potential error in: $log"
    FAIL_COUNT=$((FAIL_COUNT+1))
  elif ! tail -n 1 "$log" | grep -q "Finished" && ! tail -n 20 "$log" | grep -q "rephrased question"; then
    echo "⚠️  Log might be incomplete or crashed silently: $log"
    FAIL_COUNT=$((FAIL_COUNT+1))
  else
    echo "✅ No errors found in: $log"
  fi
done

if [ "$FAIL_COUNT" -gt 0 ]; then
  echo "❗ $FAIL_COUNT log(s) contain errors or warnings."
else
  echo "🎉 All processes completed successfully!"
fi
