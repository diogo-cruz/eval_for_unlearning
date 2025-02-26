# eval_for_unlearning


## Supported Evaluations

Currently supports:
- **LM-Eval Harness tasks**: tinyMMLU, WMDP (biomedical, cybersecurity, chemistry domains)

## Configs

- `eval/configs/models.yaml`: Model configurations including model paths, tokenizers, and precision settings
- `eval/configs/lm_eval.yaml`: LM-Eval Harness task configurations with metric paths and descriptions

## Setup

```bash
pip install -r eval/requirements.txt
```

## Usage

Basic usage:

```bash
# Evaluate a single model on a single task
python -m eval.eval --model llama3_tar_bio --tasks wmdp_bio

# Evaluate a model on multiple tasks
python -m eval.eval --model llama2_7b --tasks wmdp_chem tinyMMLU

# Use a Hugging Face token for gated models
python -m eval.eval --model llama2_7b --tasks tinyMMLU --hf_token "your_hf_token"

# Customize batch size and few-shot examples
python -m eval.eval --model llama3_tar_bio --tasks wmdp_bio --batch_size 8 --num_fewshot 2
```

## Adding New Models

Add new models to `eval/configs/models.yaml`:

```yaml
model_key:
  name: "huggingface/model-name"
  tokenizer: "huggingface/tokenizer-name"  # Optional, defaults to model name
  device_map: "auto"  # or specific device configuration
  precision: "bfloat16"  # or "float16"
```

## Adding New Tasks

Add new LM-Eval tasks to `eval/configs/lm_eval.yaml`:

```yaml
task_name:
  key_metric_path: ["results", "task_name", "metric_name"]
  description: "Description of the task"
```

## Structure

```
eval/
├── __init__.py
├── configs/
│   ├── models.yaml      # Model configurations
│   └── lm_eval.yaml     # Task configurations
├── evaluators/
│   ├── __init__.py
│   └── lm_eval.py       # LM-Eval Harness integration
├── eval.py              # Main evaluation script
├── utils.py             # Utility functions
└── requirements.txt     # Dependencies
```

