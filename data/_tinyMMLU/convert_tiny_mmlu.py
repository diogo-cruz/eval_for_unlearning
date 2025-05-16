import pandas as pd
import re
import os

def convert_choices(choices_str):
    # Extract choices from NumPy array string format ['0' '1' '2' '3']
    choices = re.findall(r"'([^']*)'", choices_str)
    # Ensure we have exactly 4 choices
    if len(choices) != 4:
        print(f"Warning: Found {len(choices)} choices instead of 4")
        print(f"Choices string: {choices_str}")
    return choices

def convert_answer(answer):
    # Convert numeric index to letter (0->A, 1->B, 2->C, 3->D)
    return chr(65 + int(answer))


if __name__ == "__main__":
  types = ["dev", "test"]  

  for type in types:
    # Read the input file
    df = pd.read_csv(f"data/_tinyMMLU/{type}/tinyMMLU.csv")

    # Convert choices and answer columns
    choices_list = df["choices"].apply(convert_choices)
    df["answer"] = df["answer"].apply(convert_answer)

    # Create new DataFrame with the correct format
    new_df = pd.DataFrame({
        "question": df["question"],
        '0': [c[0] if len(c) > 0 else '' for c in choices_list],
        '1': [c[1] if len(c) > 1 else '' for c in choices_list],
        '2': [c[2] if len(c) > 2 else '' for c in choices_list],
        '3': [c[3] if len(c) > 3 else '' for c in choices_list],
        'answer': df['answer']
    })

    # Add subject column from original DataFrame
    new_df["subject"] = df["subject"]

    # Group by subject and save separate files
    for subject, subject_df in new_df.groupby('subject'):
        # Clean subject name (remove spaces, lowercase)
        clean_subject = subject.lower().replace(' ', '_')
        
        # Remove subject column before saving
        output_df = subject_df.drop('subject', axis=1)
        
        # Save to subject-specific file
        output_path = f'data/tinyMMLU/{type}/{clean_subject}_{type}.csv'
        output_df.to_csv(output_path, index=False, header=False)
        print(f"Created {output_path} with {len(output_df)} questions") 
