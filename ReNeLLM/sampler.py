import os
import json
import math
import random
from datasets import load_dataset

def create_sample_dataset(dataset_name, subset_name="wmdp-bio", sample_percent=5, seed=42, output_file=None):
    """
    Creates a sample of the specified dataset and saves it as a simple JSON list file.
    
    Args:
        dataset_name (str): The name of the dataset on Hugging Face (e.g., "cais/wmdp")
        subset_name (str): The subset of the dataset to use (e.g., "test")
        sample_percent (float): Percentage of the dataset to sample (default: 5%)
        seed (int): Random seed for reproducibility
        output_file (str): Optional specific output file path
        
    Returns:
        str: Path to the saved sample file
    """
    # Set random seed for reproducibility
    random.seed(seed)
    
    # Create directory for saved samples if it doesn't exist
    sample_dir = './data'
    os.makedirs(sample_dir, exist_ok=True)
    
    # Create a default filename based on parameters if not specified
    if output_file is None:
        filename = f"{subset_name}_{sample_percent}_percent.json"
        file_path = os.path.join(sample_dir, filename)
    else:
        file_path = output_file
    
    # Load the full dataset
    print(f"Loading dataset: {dataset_name}, subset: {subset_name}")
    full_dataset = load_dataset(dataset_name, subset_name, split='test')
    
    # Calculate sample size based on percentage
    sample_size = math.ceil(len(full_dataset) * (sample_percent / 100))
    
    # Generate random indices for sampling
    random_indices = random.sample(range(len(full_dataset)), sample_size)
    
    # Select the sample based on these indices
    sample_dataset = full_dataset.select(random_indices)
    
    print(f"Created {sample_percent}% sample: {len(sample_dataset)} items from {len(full_dataset)} total")
    
    sample_list = []
    for idx, item in enumerate(sample_dataset):
        example = dict(item)
        example["original_dataset_index"] = random_indices[idx]
        sample_list.append(example)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(sample_list, f, ensure_ascii=False, indent=2)
    
    print(f"Saved sample to: {file_path}")
    
    return file_path

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Create a simple sample of a dataset')
    parser.add_argument('--dataset', type=str, default="cais/wmdp", help='Dataset name on Hugging Face')
    parser.add_argument('--subset', type=str, default="wmdp-bio", help='Dataset subset name')
    parser.add_argument('--percent', type=int, default=5, help='Percentage to sample')
    parser.add_argument('--output', type=str, default=None, help='Output file path')
    parser.add_argument('--seed', type=int, default=42)
    
    args = parser.parse_args()
    
    # Create and save the sample dataset
    sample_file_path = create_sample_dataset(
        args.dataset, 
        args.subset, 
        args.percent, 
        args.seed,
        args.output
    )
    
    print(f"Sample dataset ready at: {sample_file_path}")