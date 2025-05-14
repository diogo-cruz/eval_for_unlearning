import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import io

# Enable LaTeX formatting
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
})

# Parse the CSV data
csv_data = """model,task,accuracy
Zephyr_7B_Beta,wmdp_bio,0.6465
Zephyr_7B_Beta,wmdp_bio_rephrased_english_filler,0.6379
Zephyr_7B_Beta,wmdp_bio_rephrased_hindi_filler,0.6308
Zephyr_7B_Beta,wmdp_bio_rephrased_latin_filler,0.6449
Zephyr_7B_Beta,wmdp_bio_rephrased_conversation,0.6434
Zephyr_7B_Beta,wmdp_bio_rephrased_poem,0.6517
Zephyr_7B_Beta,wmdp_bio_rephrased_replace_with_variables,0.6104
Zephyr_7B_Beta,wmdp_bio_rephrased_technical_terms_removed_1,0.5617
Zephyr_7B_Beta,wmdp_bio_rephrased_translated_farsi,0.4988
Zephyr_7B_Beta,wmdp_bio_rephrased_translated_german,0.6041
Zephyr_7B_Beta,wmdp_bio_rephrased_translated_korean,0.5538
Zephyr_7B_Beta,tinyMMLU,0.6244
Zephyr-7B-ELM,wmdp_bio,0.3016
Zephyr-7B-ELM,wmdp_bio_rephrased_english_filler,0.3519
Zephyr-7B-ELM,wmdp_bio_rephrased_hindi_filler,0.5507
Zephyr-7B-ELM,wmdp_bio_rephrased_latin_filler,0.3778
Zephyr-7B-ELM,wmdp_bio_rephrased_conversation,0.2977
Zephyr-7B-ELM,wmdp_bio_rephrased_poem,0.2868
Zephyr-7B-ELM,wmdp_bio_rephrased_replace_with_variables,0.3252
Zephyr-7B-ELM,wmdp_bio_rephrased_technical_terms_removed_1,0.3111
Zephyr-7B-ELM,wmdp_bio_rephrased_translated_farsi,0.3621
Zephyr-7B-ELM,wmdp_bio_rephrased_translated_german,0.304
Zephyr-7B-ELM,wmdp_bio_rephrased_translated_korean,0.3252
Zephyr-7B-ELM,tinyMMLU,0.6185
Mistral-7B-ELM,wmdp_bio,0.2891
Mistral-7B-ELM,wmdp_bio_rephrased_english_filler,0.3064
Mistral-7B-ELM,wmdp_bio_rephrased_hindi_filler,0.4721
Mistral-7B-ELM,wmdp_bio_rephrased_latin_filler,0.3032
Mistral-7B-ELM,wmdp_bio_rephrased_conversation,0.3001
Mistral-7B-ELM,wmdp_bio_rephrased_poem,0.3255
Mistral-7B-ELM,wmdp_bio_rephrased_replace_with_variables,0.3056
Mistral-7B-ELM,wmdp_bio_rephrased_technical_terms_removed_1,0.2875
Mistral-7B-ELM,wmdp_bio_rephrased_translated_farsi,0.2844
Mistral-7B-ELM,wmdp_bio_rephrased_translated_german,0.2875
Mistral-7B-ELM,wmdp_bio_rephrased_translated_korean,0.2954
Mistral-7B-ELM,tinyMMLU,0.5597
Mistral-7B-v0.1,wmdp_bio,0.674
Mistral-7B-v0.1,wmdp_bio_rephrased_english_filler,0.641
Mistral-7B-v0.1,wmdp_bio_rephrased_hindi_filler,0.6347
Mistral-7B-v0.1,wmdp_bio_rephrased_latin_filler,0.6606
Mistral-7B-v0.1,wmdp_bio_rephrased_conversation,0.6599
Mistral-7B-v0.1,wmdp_bio_rephrased_poem,0.6328
Mistral-7B-v0.1,wmdp_bio_rephrased_replace_with_variables,0.6308
Mistral-7B-v0.1,wmdp_bio_rephrased_technical_terms_removed_1,0.597
Mistral-7B-v0.1,wmdp_bio_rephrased_translated_farsi,0.502
Mistral-7B-v0.1,wmdp_bio_rephrased_translated_german,0.6174
Mistral-7B-v0.1,wmdp_bio_rephrased_translated_korean,0.5703
Mistral-7B-v0.1,tinyMMLU,0.6046
Llama3-8B-Instruct-ELM,wmdp_bio,0.3299
Llama3-8B-Instruct-ELM,wmdp_bio_rephrased_english_filler,0.3959
Llama3-8B-Instruct-ELM,wmdp_bio_rephrased_hindi_filler,0.5373
Llama3-8B-Instruct-ELM,wmdp_bio_rephrased_latin_filler,0.3582
Llama3-8B-Instruct-ELM,wmdp_bio_rephrased_conversation,0.3472
Llama3-8B-Instruct-ELM,wmdp_bio_rephrased_poem,0.3278
Llama3-8B-Instruct-ELM,wmdp_bio_rephrased_replace_with_variables,0.3378
Llama3-8B-Instruct-ELM,wmdp_bio_rephrased_technical_terms_removed_1,0.2985
Llama3-8B-Instruct-ELM,wmdp_bio_rephrased_translated_farsi,0.304
Llama3-8B-Instruct-ELM,wmdp_bio_rephrased_translated_german,0.3221
Llama3-8B-Instruct-ELM,wmdp_bio_rephrased_translated_korean,0.3472
Llama3-8B-Instruct-ELM,tinyMMLU,0.5741
Llama3-8B-ELM,wmdp_bio,0.3449
Llama3-8B-ELM,wmdp_bio_rephrased_english_filler,0.4077
Llama3-8B-ELM,wmdp_bio_rephrased_hindi_filler,0.5923
Llama3-8B-ELM,wmdp_bio_rephrased_latin_filler,0.3425
Llama3-8B-ELM,wmdp_bio_rephrased_conversation,0.4438
Llama3-8B-ELM,wmdp_bio_rephrased_poem,0.3381
Llama3-8B-ELM,wmdp_bio_rephrased_replace_with_variables,0.2938
Llama3-8B-ELM,wmdp_bio_rephrased_technical_terms_removed_1,0.2993
Llama3-8B-ELM,wmdp_bio_rephrased_translated_farsi,0.2946
Llama3-8B-ELM,wmdp_bio_rephrased_translated_german,0.3024
Llama3-8B-ELM,wmdp_bio_rephrased_translated_korean,0.2899
Llama3-8B-ELM,tinyMMLU,0.6004
Llama3-8B,wmdp_bio,0.7054
Llama3-8B,wmdp_bio_rephrased_english_filler,0.6929
Llama3-8B,wmdp_bio_rephrased_hindi_filler,0.7054
Llama3-8B,wmdp_bio_rephrased_latin_filler,0.7109
Llama3-8B,wmdp_bio_rephrased_conversation,0.6991
Llama3-8B,wmdp_bio_rephrased_poem,0.6556
Llama3-8B,wmdp_bio_rephrased_replace_with_variables,0.6591
Llama3-8B,wmdp_bio_rephrased_technical_terms_removed_1,0.6245
Llama3-8B,wmdp_bio_rephrased_translated_farsi,0.6394
Llama3-8B,wmdp_bio_rephrased_translated_german,0.6866
Llama3-8B,wmdp_bio_rephrased_translated_korean,0.6198
Llama3-8B,tinyMMLU,0.6427
Llama3-8B-Instruct,wmdp_bio,0.7086
Llama3-8B-Instruct,wmdp_bio_rephrased_english_filler,0.7054
Llama3-8B-Instruct,wmdp_bio_rephrased_hindi_filler,0.7235
Llama3-8B-Instruct,wmdp_bio_rephrased_latin_filler,0.7203
Llama3-8B-Instruct,wmdp_bio_rephrased_conversation,0.7117
Llama3-8B-Instruct,wmdp_bio_rephrased_poem,0.6801
Llama3-8B-Instruct,wmdp_bio_rephrased_replace_with_variables,0.663
Llama3-8B-Instruct,wmdp_bio_rephrased_technical_terms_removed_1,0.6127
Llama3-8B-Instruct,wmdp_bio_rephrased_translated_farsi,0.6528
Llama3-8B-Instruct,wmdp_bio_rephrased_translated_german,0.6591
Llama3-8B-Instruct,wmdp_bio_rephrased_translated_korean,0.6277
Llama3-8B-Instruct,tinyMMLU,0.5921"""

# Load data
df = pd.read_csv(io.StringIO(csv_data))

# Adjust accuracy
df['adjusted_accuracy'] = df['accuracy'] - 0.25
df['adjusted_accuracy'] = df['adjusted_accuracy'].clip(lower=0)

# Define model families with colorblind-friendly colors (Wong's palette)
model_families = [
    {'name': 'Zephyr', 'base': 'Zephyr_7B_Beta', 'elm': 'Zephyr-7B-ELM', 'color': '#0072B2'},
    {'name': 'Mistral', 'base': 'Mistral-7B-v0.1', 'elm': 'Mistral-7B-ELM', 'color': '#D55E00'},
    {'name': 'Llama3-8B', 'base': 'Llama3-8B', 'elm': 'Llama3-8B-ELM', 'color': '#009E73'},
    {'name': 'Llama3-8B-Instruct', 'base': 'Llama3-8B-Instruct', 'elm': 'Llama3-8B-Instruct-ELM', 'color': '#CC79A7'},
]

# Task styles with unique markers
task_styles = {
    'wmdp_bio': {
        'marker': 's', 'label': 'Base prompt', 'size': 180, 'highlight': True
    },
    'tinyMMLU': {
        'marker': '*', 'label': 'tinyMMLU', 'size': 180, 'highlight': True
    },
    'wmdp_bio_rephrased_english_filler': {'marker': 'o', 'label': 'Rephrased w/ English filler'},
    'wmdp_bio_rephrased_hindi_filler': {'marker': 'P', 'label': 'Rephrased w/ Hindi filler'},
    'wmdp_bio_rephrased_latin_filler': {'marker': 'X', 'label': 'Rephrased w/ Latin filler'},
    'wmdp_bio_rephrased_conversation': {'marker': 'D', 'label': 'Rephrased as conversation'},
    'wmdp_bio_rephrased_poem': {'marker': '^', 'label': 'Rephrased as poem'},
    'wmdp_bio_rephrased_replace_with_variables': {'marker': 'v', 'label': 'Replaced with variables'},
    'wmdp_bio_rephrased_technical_terms_removed_1': {'marker': 'p', 'label': 'Technical terms removed'},
    'wmdp_bio_rephrased_translated_farsi': {'marker': '<', 'label': 'Translated to Farsi'},
    'wmdp_bio_rephrased_translated_german': {'marker': 'd', 'label': 'Translated to German'},
    'wmdp_bio_rephrased_translated_korean': {'marker': '>', 'label': 'Translated to Korean'},    
}

# Create figure
plt.figure(figsize=(12, 10))
ax = plt.gca()

# Plot diagonal reference line
ax.plot([0, 1], [0, 1], 'k--', alpha=0.3)

# Plot data
for family in model_families:
    base_data = df[df['model'] == family['base']]
    elm_data = df[df['model'] == family['elm']]
    merged = pd.merge(base_data, elm_data, on='task', suffixes=('_base', '_elm'))
    
    # Plot points
    for _, row in merged.iterrows():
        task = row['task']
        if task in task_styles:
            style = task_styles[task]
            ax.scatter(
                row['adjusted_accuracy_base'],
                row['adjusted_accuracy_elm'],
                color=style.get('facecolor', family['color']),
                marker=style['marker'],
                s=style.get('size', 100),
                edgecolor=style.get('edgecolor', 'black'),
                linewidth=1.2 if style.get('highlight') else 0.5,
                alpha=0.9
            )


# Axis labels
ax.set_xlabel(r'Base model accuracy (adjusted)', fontsize=14)
ax.set_ylabel(r'Unlearned (ELM) model accuracy (adjusted)', fontsize=14)

# Axis limits
ax.set_xlim(0, 0.55)
ax.set_ylim(0, 0.55)

# Legends
# Model family legend
from matplotlib.lines import Line2D
model_legend = [
    Line2D([0], [0], marker='o', color=family['color'], label=family['name'],
           linestyle='', markersize=8) for family in model_families
]

# Task legend
task_legend = [
    Line2D([0], [0], marker=style['marker'], color='black', label=style['label'],
           linestyle='', markersize=8) for task, style in task_styles.items()
]

# Add legends
legend1 = ax.legend(handles=model_legend, title='Models', loc='upper left', fontsize=10, title_fontsize=11, bbox_to_anchor=(0, 1), handletextpad=1.5)
legend2 = ax.legend(handles=task_legend, title='Tasks', loc='upper left', fontsize=9, title_fontsize=11, bbox_to_anchor=(0, 0.85), handletextpad=1.5, labelspacing=1.2)
ax.add_artist(legend1)

# Grid
ax.grid(True, linestyle='--', alpha=0.3)

# Layout
plt.tight_layout()

# Save the plot with higher resolution
plt.savefig('model_performance_comparison_unified.pdf', bbox_inches='tight', dpi=300)

# Show the figure
plt.close()

# Return the paths to the generated images
print('Saved as: model_performance_comparison_unified.pdf')