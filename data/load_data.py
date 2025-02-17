from huggingface_hub import snapshot_download
import getpass
import os

from datasets import load_dataset

# def download_data(subset, save_path):
#     """
#     Download a specific subset of a Hugging Face dataset and save it to disk.
#     """
#     print(f"Downloading subset '{subset}'...")
#     try:
#         # Load the specified subset of the dataset
#         dataset = load_dataset("locuslab/TOFU", subset, split="train")

#         cache_dir="/state/partition1/user/" + getpass.getuser() + "/hug"
#         print(os.path.join(cache_dir, save_path))
#         # Save the subset to the specified path
#         dataset.save_to_disk(os.path.join(cache_dir, save_path))

#         print(f"subset '{subset}' saved successfully at '{save_path}'!")
#     except Exception as e:
#         print(f"Error downloading subset: {e}")

if __name__ == "__main__":

    # for dataset, split, path in [("cais/wmdp", "wmdp-bio"),
    #     ("cais/wmdp", "wmdp-chem"),
    #     ("cais/wmdp", "wmdp-chem"),
    #     ("cais/wmdp-corpora", "bio-retain-corpus"),
    #     ("cais/wmdp-corpora", "cyber-forget-corpus"),
    #     ("cais/wmdp-corpora", "cyber-retain-corpus"),
    #     ("cais/wmdp-mmlu-auxiliary-corpora", "economics-corpus"),
    #     ("cais/wmdp-mmlu-auxiliary-corpora", "law-corpus"),
    #     ("cais/wmdp-mmlu-auxiliary-corpora", "physics-corpus")]:
    #     # download_data(subset, path)

    wmdp = [
        ("cais/wmdp", "wmdp-bio"),
        ("cais/wmdp", "wmdp-chem"),
        ("cais/wmdp", "wmdp-cyber"),
        
        ("cais/wmdp-corpora", "bio-retain-corpus"),
        ("cais/wmdp-corpora", "cyber-forget-corpus"),
        ("cais/wmdp-corpora", "cyber-retain-corpus"),
        
        ("cais/wmdp-mmlu-auxiliary-corpora", "economics-corpus"),
        ("cais/wmdp-mmlu-auxiliary-corpora", "law-corpus"),
        ("cais/wmdp-mmlu-auxiliary-corpora", "physics-corpus"),
    ]

    for name, subset in wmdp:
        split = 'test' if name == "cais/wmdp" else 'train'
        ds = load_dataset(name, subset, split=split)
        print(f'The following is a sample row from {subset}:')
        print(ds[0])