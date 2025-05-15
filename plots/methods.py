import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('./unlearning_method_comparison.csv')

# Adjust accuracy
df['adjusted_accuracy'] = df['accuracy'] - 0.25
df['adjusted_accuracy'] = df['adjusted_accuracy'].clip(lower=0)

# Define base model
base_model = 'Llama3-8B-Instruct'

# Get all models (i.e., unlearning methods) excluding the base
methods = df['model'].unique().tolist()
methods = [m for m in methods if m != base_model]

# Assign color-blind friendly colors (Wong + gray)
colors = [
    '#E69F00', '#56B4E9', '#009E73', '#F0E442',
    '#0072B2', '#D55E00', '#CC79A7', '#999999'
]
assert len(methods) <= len(colors), "Too many methods for available colors"

method_colors = dict(zip(methods, colors))

# Task marker styles
task_styles = {
    'wmdp_bio': {'marker': 's', 'label': 'Base prompt', 'size': 180, 'highlight': True},
    'tinyMMLU': {'marker': '*', 'label': 'tinyMMLU', 'size': 180, 'highlight': True},
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

# Plot
plt.figure(figsize=(12, 10))
ax = plt.gca()

# Diagonal line
ax.plot([-.01, 1], [-.01, 1], 'k--', alpha=0.3)

# Base model data
base_df = df[df['model'] == base_model][['task', 'adjusted_accuracy']].rename(columns={'adjusted_accuracy': 'base_accuracy'})

# Plot each unlearning method
for method in methods:
    method_df = df[df['model'] == method][['task', 'adjusted_accuracy']]
    merged = pd.merge(base_df, method_df, on='task')
    
    for _, row in merged.iterrows():
        task = row['task']
        if task in task_styles:
            style = task_styles[task]
            ax.scatter(
                row['base_accuracy'],
                row['adjusted_accuracy'],
                color=method_colors[method],
                marker=style['marker'],
                s=style.get('size', 100),
                edgecolor='black',
                linewidth=1.2 if style.get('highlight') else 0.5,
                alpha=0.9
            )

# Labels and limits
ax.set_xlabel(r'Base model accuracy (adjusted)', fontsize=14)
ax.set_ylabel(r'Unlearned model accuracy (adjusted)', fontsize=14)
ax.set_xlim(-.01, 0.5)
ax.set_ylim(-.01, 0.5)

# Legends
from matplotlib.lines import Line2D

method_legend = [
    Line2D([0], [0], marker='o', color=color, label=method,
           linestyle='', markersize=8) for method, color in method_colors.items()
]

task_legend = [
    Line2D([0], [0], marker=style['marker'], color='black', label=style['label'],
           linestyle='', markersize=8) for task, style in task_styles.items()
]

legend1 = ax.legend(handles=method_legend, title='Unlearning Method', loc='upper left', fontsize=10, title_fontsize=11, bbox_to_anchor=(0, 1), handletextpad=1.5)
legend2 = ax.legend(handles=task_legend, title='Tasks', loc='upper left', fontsize=9, title_fontsize=11, bbox_to_anchor=(0, 0.7), handletextpad=1.5, labelspacing=1.2)
ax.add_artist(legend1)

# Grid and layout
ax.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()

# Save
plt.savefig('unlearning_methods_comparison.pdf', bbox_inches='tight', dpi=300)
plt.close()

print('Saved as: unlearning_methods_comparison.pdf')