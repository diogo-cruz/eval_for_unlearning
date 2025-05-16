# I haven't checked how much this has cost so far - might be a good idea before running more things
# Done
- filler hindi, english, latin
- hindi and bengali translation

# Running Instructions
- claude_3_5.sh
- you'll want to comment out what's already been run
- uses the updated version of evaluation/rephrase_prompts.py - called evaluation/rephrase_prompts_claude_3_5.py
    - uses the new evaluation/prompts/settings_claude_3_5.json file for model choice
    - other changes include handling rate limits and some minor changes to the save path
- theres a prompt that shows up at the end saying the logs folder isn't found - probably a problem with the claude_3_5.sh file if you want to fix that, but not necessary - things will still run

# Data
in data/wmdp-rephrased/claude_3_5