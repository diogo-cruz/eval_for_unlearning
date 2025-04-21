import time
import json
import os
import argparse
import random
from datasets import load_dataset

# from utils.llm_completion_utils import claudeCompletion
# from utils.prompt_rewrite_utils import shortenSentence, misrewriteSentence, changeOrder, addChar, languageMix, styleChange
from rewrite import shortenSentence, misrewriteSentence, changeOrder, addChar, languageMix, styleChange
# from utils.scenario_nest_utils import SCENARIOS
# from utils.harmful_classification_utils import harmful_classification

def load_sample_dataset(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Sample dataset file not found: {file_path}")
    
    print(f"Loading sample dataset from: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        sample_dataset = json.load(f)
    
    print(f"Loaded sample dataset with {len(sample_dataset)} items")
    return sample_dataset

def main(args):
    # data = data_reader(args.data_path)
    data = load_sample_dataset(args.sample_path)
    
    if args.prompt is not None:
        data = [{"question": args.prompt}]

    operations = [shortenSentence, misrewriteSentence, changeOrder, addChar, languageMix, styleChange]
    # scenarios = SCENARIOS

    # Create a separate dataset for each operation
    for op_idx, operation in enumerate(operations):
        op_name = operation.__name__
        print(f"\n\n======== Processing operation: {op_name} ({op_idx+1}/{len(operations)}) ========\n")
        
        # Create a new dataset for this operation while preserving all original fields
        new_dataset = []

        for idx, item in enumerate(data):            
            harm_behavior = item["question"]
            temp_harm_behavior = harm_behavior

            if not os.path.exists('./results/renellm/temp'):
                os.makedirs('./results/renellm/temp')

            # save the results for every 10 samples 
            if idx != 0 and idx % 10 == 0:
                # file_name = f"./results/renellm/temp/{args.save_suffix}_{idx}.json"
                file_name = f"./results/renellm/temp/{op_name}_{args.save_suffix}_{idx}.json"
                with open(file_name, "w", encoding="utf-8") as f:
                    json.dump(new_dataset, f, ensure_ascii=False, indent=4)
                print(f"\nThe temporary file has been saved to: {os.path.abspath(file_name)}\n")

            # loop_count = 0
            
            # while True:
            print(
            "\n################################\n"
            f"Operation: {op_name}\n"
            f"Current Data: {idx+1}/{len(data)}, {harm_behavior}\n"
            # f"Current Iteration Round: {loop_count+1}/{args.iter_max}\n"
            "################################\n")

            # Apply only the current operation
            print(f"******* Start idx {idx} Prompt Rewriting with {op_name}! *******")
            rewritten_prompt = operation(args, harm_behavior)
            print(f"Rewritten prompt: {rewritten_prompt}\n")
            print(f"******* Prompt idx {idx} Rewriting Done! *******\n")

            new_item = item.copy()
            new_item["question"] = rewritten_prompt
            new_item["original_question"] = temp_harm_behavior
            new_dataset.append(new_item)

            # loop_count += 1
            print(f"\n******* Processing for idx {idx} Complete *******\n")
            
            # break  # Remove the original while loop

        # Save the complete dataset for this operation
        if not os.path.exists('./results/renellm/rewritten'):
            os.makedirs('./results/renellm/rewritten')

        # file_name = f"./results/renellm/rewritten/rewritten_prompts_{args.save_suffix}.json"
        file_name = f"./results/renellm/rewritten/{op_name}_{args.save_suffix}.json"
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(new_dataset, f, ensure_ascii=False, indent=4)

        print(f"\nThe rewritten dataset for {op_name} has been saved to:\n{os.path.abspath(file_name)}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--prompt', type=str, default=None)
    parser.add_argument('--rewrite_model', type=str, default="gemini-2.0-flash-lite",
                        choices=["gpt-3.5-turbo", "gpt-4", "gemini-2.0-flash-lite"])
    parser.add_argument('--attack_model', type=str, default="anthropic.claude-v2",
                        choices=["anthropic.claude-v2", "gpt-4"])
    # parser.add_argument('--iter_max', type=int, default=20)
    parser.add_argument("--max_tokens", type=int, default=3584)
    parser.add_argument('--temperature', type=float, default=0)
    parser.add_argument('--round_sleep', type=int, default=1)
    parser.add_argument('--fail_sleep', type=int, default=1)
    parser.add_argument('--retry_times', type=int, default=1000)
    parser.add_argument('--save_suffix', type=str, default='')
    # parser.add_argument("--gpt_api_key", required=True, type=str, default=None)
    parser.add_argument("--gpt_base_url", type=str, default=None)
    # parser.add_argument("--claude_api_key", required=True, type=str, default=None)
    parser.add_argument("--claude_base_url", type=str, default=None)
    parser.add_argument("--gemini_api_key", required=True, type=str, default=None)
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--sample_path', type=str, default=None, help='Path to a pre-sampled dataset file')

    args = parser.parse_args()
    random.seed(args.seed)
    main(args)

    # python renellm.py --gemini_api_key AIzaSyCN-C_Psa8d9rShNN5AT72o6i968Ie8oIw --sample_path ./data/wmdp-bio_5_percent.json