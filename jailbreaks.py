import pandas as pd
import random
import os
import json
from datasets import load_dataset

def process_dataset(excel_path, subset_name, output_path, sample_percentage=5):
    """
    Process a Hugging Face dataset with subsets.
    For each HF row, select a random Excel row, replace "[INSERT PRlsOMPT HERE]" in the Excel text
    with the HF question, and use that as the new question in the dataset.
    
    Args:
        excel_path: Path to the Excel file
        subset_name: The subset name to use from the cais/wmdp dataset
        output_path: Path to save the output JSON file
        column_name: Column name in the Excel file containing the text to extract (default: "text")
        sample_percentage: Percentage of the HF dataset to use (default: 5%)
    """
    # Load the Excel file
    df = pd.read_excel(excel_path)
    print(f"Loaded Excel file with {len(df)} rows")
    
    # Load the Hugging Face dataset with specific subset
    dataset = load_dataset("cais/wmdp", subset_name, split='test')
    print(f"Loaded Hugging Face dataset 'cais/wmdp/{subset_name}' test split with {len(dataset)} rows")
    
    # Take only 5% of the dataset
    sample_size = max(1, int(len(dataset) * sample_percentage / 100))
    indices = random.sample(range(len(dataset)), sample_size)
    dataset = dataset.select(indices)
    print(f"Sampled {len(dataset)} rows ({sample_percentage}% of original data)")
    
    # Create a list to hold the new data
    new_data = []
    
    # Process each example in the dataset
    for example in dataset:
        # Get the original HF question
        original_question = example['question']
        column_name = 'text'
        
        # Replace the placeholder in the Excel text with the HF question
        excel_text = ''
        while "[INSERT PROMPT HERE]" not in excel_text:
            # Select a random row from Excel
            random_row = df.sample(1).iloc[0]
            excel_text = random_row[column_name]
        new_question = excel_text.replace("[INSERT PROMPT HERE]", original_question)
        
        # Create a new example with the modified question
        new_example = dict(example)
        new_example['question'] = new_question
        
        new_data.append(new_example)
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    
    # Save as JSON
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False, indent=2)
    
    print(f"Saved dataset to {output_path}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Process Excel and Hugging Face datasets with subsets")
    parser.add_argument("--subset", required=True, help="Subset name from cais/wmdp dataset")
    parser.add_argument("--output", required=True, help="Path to save the output CSV file")
    parser.add_argument("--percentage", type=int, default=5, help="Percentage of dataset to use (default: 5)")
    
    args = parser.parse_args()
    
    process_dataset(
        './jailbreak-prompt.xlsx',
        args.subset,
        args.output,
        args.percentage
    )

    # python jailbreaks.py --subset wmdp-bio --output wmdp_rephrased/78_templates/bio_questions.json