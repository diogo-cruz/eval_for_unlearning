# How to run
Not the most streamlined, but it does the trick :)
### Setup
- runpod A40 with ~35G volume? not sure how much is necessary but at some point the volume ran out
- can't run on Colab unless you quantize the model, but I didn't want to risk affecting accuracy

### Notebook: probe/wmdp_bio_full.ipynb
Coding
- define model_path based on what model is probed
- it shouldn't need changing, but I like sanity check that num_heads is correct - left a note in the notebook
- for running cyber and rephrasings, you will need to update the dataset and maybe split loading. might be easier to start with cyber but haven't looked

Running
- run first cell in probe/wmdp_bio_full.ipynb
- kernel will restart after installation
- run cell 2 onward
- rename the results directory (or update the script to handle this) and push

# Results
- only really need to look at "accuracy_summary.csv" in "full" directories 
- "full" indicates all layers results; I initially ran things on intermittent layers just to get an initial look at results in "initial" directories.

# Extra Notes on Results
- Llama ELM showed an increase in accuracy toward the end, by Zephyr didn't - might be an interesting result if there's time
    - I believe this is because Llama is a more capable model than Zephyr
    - One thing to note is how I use the config.json from the base model in `config_path = "HuggingFaceH4/zephyr-7b-beta"` rather than Zephyr ELM
        - the reason I don't think this is the reason is because we are getting random chance accuracy as you would expect from an unlearned model. If the base weights were used, you would get closer to the much higher base accuracy.
        - this is because you need to reference a config that has the parameters used in the script. The ELM one is just an adapter model with no config.json - it adapts from the base model config. See more details here:     https://github.com/center-for-humans-and-machines/transformer-heads/tree/main?tab=readme-ov-file#more-custom-loss-functions-and-models and here https://github.com/center-for-humans-and-machines/transformer-heads/tree/main?tab=readme-ov-file#can-my-transformer-architecture-be-supported

# Reference
- notebook is based on https://github.com/center-for-humans-and-machines/transformer-heads/blob/main/notebooks/gpt2/text_classification_linear_probe.ipynb
    - see https://github.com/center-for-humans-and-machines/transformer-heads/tree/main and https://github.com/center-for-humans-and-machines/transformer-heads/blob/main/notebooks/gpt2/linear_probe.ipynb for more info