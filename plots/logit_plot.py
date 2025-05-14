import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Table 1 data
methods_table1 = [
    '0-shot_Zephyr_base', '0-shot_Zephyr_RMU', 'rephrased_as_conversation', 'rephrased_as_poem', 'technical_terms_removed',
    'replaced_with_variables', 'translated_arabic', 'translated_bengali', 'translated_czech',
    'translated_farsi', 'translated_french', 'translated_german', 'translated_hindi',
    'translated_korean', 'translated_turkish', 'translated_telugu', 'translated_vietnamese'
]

biology_accuracy_table1 = [
    0.663, 0.146, 0.094, 0.130, 0.123, 0.123, 0.151, 0.148, 0.123,
    0.148, 0.126, 0.116, 0.162 , 0.104, 0.112, 0.149, 0.125
]

accuracy_answered_table1 = [
    0.665, 0.389, 0.405, 0.434, 0.395, 0.367, 0.364, 0.346, 0.400,
    0.357, 0.422, 0.365, 0.315, 0.337, 0.355, 0.307, 0.349
]

# Table 2 data
methods_table2 = [
    '0-shot_Zephyr_base', '0-shot_Zephyr_RMU', 'english_filler', 'latin_filler', 'hindi_filler',
    'rephrased_as_conversation', 'rephrased_as_poem', 'technical_terms_removed',
    'replaced_with_variables', 'translated_arabic', 'translated_bengali', 'translated_czech',
    'translated_farsi', 'translated_french', 'translated_german', 'translated_hindi',
    'translated_korean', 'translated_turkish', 'translated_telugu', 'translated_vietnamese', '0-shot_tinyMMLU'
]

biology_accuracy_table2 = [
    0.647, 0.307, 0.314, 0.342, 0.301,
    0.304, 0.322, 0.307, 0.282, 0.309, 0.262, 0.291,
    0.302, 0.303, 0.292, 0.290, 0.295, 0.286, 0.270, 0.272, 0.608
]

# Find common methods
common_methods = sorted(set(methods_table1) & set(methods_table2))

# Ensure baseline is first
common_methods.remove('0-shot_Zephyr_base')
common_methods = ['0-shot_Zephyr_base'] + common_methods

# Build dictionaries
table1_bio = dict(zip(methods_table1, biology_accuracy_table1))
table1_acc_ans = dict(zip(methods_table1, accuracy_answered_table1))
table2_bio = {}
for m, val in zip(methods_table2, biology_accuracy_table2):
    if m in common_methods and m not in table2_bio:
        table2_bio[m] = val

# Prepare data
bio1 = [table1_bio[m] for m in common_methods]
acc_ans1 = [table1_acc_ans[m] for m in common_methods]
bio2 = [table2_bio[m] for m in common_methods]

x = np.arange(len(common_methods))
width = 0.25

# Plotting
plt.figure(figsize=(16, 8))

# Actual bars
# Plotting
plt.figure(figsize=(16, 8))

# Bar drawing loop
for i, method in enumerate(common_methods):
    is_base = (method == '0-shot_Zephyr_base')

    # Only Zephyr Base gets hatching and outline
    hatch = '//' if is_base else None
    edge = 'black' if is_base else None

    plt.bar(x[i] - width, bio1[i], width=width, color='blue', edgecolor=edge, hatch=hatch)
    plt.bar(x[i], acc_ans1[i], width=width, color='green', edgecolor=edge, hatch=hatch)
    plt.bar(x[i] + width, bio2[i], width=width, color='red', edgecolor=edge, hatch=hatch)


# Custom legend patches
legend_elements = [
    Patch(facecolor='blue', label='All Prompts'),
    Patch(facecolor='green', label='Answered Prompts'),
    Patch(facecolor='red', label='Logits'),
    Patch(facecolor='white', edgecolor='black', hatch='//', label='Zephyr Base Model'),
    Patch(facecolor='white', edgecolor='black', label='Zephyr RMU')  # No hatch
]

plt.xlabel('Task', fontsize=14)
plt.ylabel('Accuracy', fontsize=14)
plt.title('Accuracy by Evaluation Method', fontsize=16)
plt.xticks(x, common_methods, rotation=45, ha='right')
plt.legend(handles=legend_elements)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Save and show
plt.savefig("grouped_accuracy_comparison_highlighted_baseline_rmu.png", dpi=300)
plt.show()
