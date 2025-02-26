from lm_eval import simple_evaluate
from lm_eval.models.huggingface import HFLM


def evaluate_lm_eval(model, tokenizer, tasks, task_config, batch_size=4, num_fewshot=0):
    """Run evaluations using lm-eval-harness."""
    lm_model = HFLM(model, tokenizer=tokenizer, batch_size=batch_size)
    eval_results = {}

    for task in tasks:
        task_results = simple_evaluate(
            model=lm_model, tasks=[task], num_fewshot=num_fewshot
        )

        # Follow the metric path to get the result
        metric_path = task_config["tasks"][task]["key_metric_path"]
        result = task_results
        for key in metric_path:
            result = result[key]

        eval_results[task] = result

    return eval_results
