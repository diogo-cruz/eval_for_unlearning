import pandas as pd
import os
import json
from datasets import load_dataset

def process_dataset_per_template(excel_path, subset_name, output_dir, sample_percentage=5):
    """
    For each row in the Excel prompt template, create a dataset where each WMDP question is inserted
    into the template. Output one JSON file per template.

    Args:
        excel_path: Path to the Excel file
        subset_name: The subset name to use from the cais/wmdp dataset
        output_dir: Directory to save the output JSON files
        sample_percentage: Percentage of the HF dataset to use (default: 5%)
    """
    # Load the Excel file
    df = pd.read_excel(excel_path)
    print(f"Loaded Excel file with {len(df)} prompt templates")
    
    # Load the Hugging Face dataset
    dataset = load_dataset("cais/wmdp", subset_name, split='test')
    print(f"Loaded HF dataset 'cais/wmdp/{subset_name}' with {len(dataset)} rows")
    
    # Sample the dataset
    sample_size = max(1, int(len(dataset) * sample_percentage / 100))
    dataset = dataset.shuffle(seed=42).select(range(sample_size))
    print(f"Sampled {len(dataset)} rows ({sample_percentage}%)")

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Process each prompt in the Excel file
    for _, row in df.iterrows():
        template = row.get("text", "")
        id = row.get("id")
        if "[INSERT PROMPT HERE]" not in template:
            print(f"Skipping template {id} - missing placeholder.")
            continue

        modified_data = []

        for example in dataset:
            original_question = example["question"]
            new_question = template.replace("[INSERT PROMPT HERE]", original_question)

            new_example = dict(example)
            new_example["question"] = new_question
            modified_data.append(new_example)

        output_path = os.path.join(output_dir, f"{subset_name}_template_{id}.json")
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(modified_data, f, ensure_ascii=False, indent=2)

        print(f"Saved template {id} dataset to {output_path}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Create a dataset per Excel prompt template")
    parser.add_argument("--subset", required=True, help="Subset name from cais/wmdp dataset")
    parser.add_argument("--output_dir", required=True, help="Directory to save the JSON files")
    parser.add_argument("--percentage", type=int, default=5, help="Percentage of dataset to use (default: 5)")

    args = parser.parse_args()

    process_dataset_per_template(
        './jailbreak-prompt.xlsx',
        args.subset,
        args.output_dir,
        args.percentage
    )

# python jailbreaks.py --subset wmdp-bio --output ../wmdp_rephrased/data_78_templates/ --percentage 2