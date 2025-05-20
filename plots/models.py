import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D

# # Adjusted font sizes
# plt.rcParams.update({
#     "text.usetex": True,
#     "font.family": "serif",
#     "font.serif": ["Computer Modern Roman"],
#     "font.size": 34,
#     "axes.titlesize": 40,
#     "axes.labelsize": 40,
#     "xtick.labelsize": 26,
#     "ytick.labelsize": 26,
#     "legend.fontsize": 32
# })

# Adjusted font sizes for better readability
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "font.size": 12,
    "axes.titlesize": 14,
    "axes.labelsize": 14,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
    "legend.fontsize": 12
})

# Read CSV from external file
df = pd.read_csv('models.csv')

# Adjust accuracy
df['adjusted_accuracy'] = df['accuracy'] - 0.25
df['adjusted_accuracy'] = df['adjusted_accuracy'].clip(lower=0)

# Define model families
model_families = [
    {'name': 'Zephyr', 'base': 'Zephyr_7B_Beta', 'elm': 'Zephyr-7B-ELM', 'color': '#0072B2'},
    {'name': 'Mistral', 'base': 'Mistral-7B-v0.1', 'elm': 'Mistral-7B-ELM', 'color': '#D55E00'},
    {'name': 'Llama3-8B', 'base': 'Llama3-8B', 'elm': 'Llama3-8B-ELM', 'color': '#009E73'},
    {'name': 'Llama3-8B-Instruct', 'base': 'Llama3-8B-Instruct', 'elm': 'Llama3-8B-Instruct-ELM', 'color': '#CC79A7'},
]

task_styles = {
    'wmdp_bio': {'marker': 's', 'label': 'Base prompt', 'size': 300, 'highlight': False},
    'tinyMMLU': {'marker': '*', 'label': 'tinyMMLU', 'size': 375, 'highlight': False},
    'wmdp_bio_rephrased_english_filler': {'marker': 'o', 'label': 'Filler text', 'size': 200, 'highlight': False},
    'wmdp_bio_rephrased_hindi_filler': {'marker': 'o', 'label': 'Filler text', 'size': 200, 'highlight': True},
    'wmdp_bio_rephrased_latin_filler': {'marker': 'o', 'label': 'Filler text', 'size': 200, 'highlight': False},
    'wmdp_bio_rephrased_conversation': {'marker': '^', 'label': 'Rephrased as conversation', 'size': 200, 'highlight': False},
    'wmdp_bio_rephrased_poem': {'marker': 'v', 'label': 'Rephrased as poem', 'size': 200, 'highlight': False},
    'wmdp_bio_rephrased_replace_with_variables': {'marker': 'P', 'label': 'Replaced with variables', 'size': 200, 'highlight': False},
    'wmdp_bio_rephrased_technical_terms_removed_1': {'marker': 'X', 'label': 'Technical terms removed', 'size': 200, 'highlight': False},
    'wmdp_bio_rephrased_translated_farsi': {'marker': 'd', 'label': 'Translated', 'size': 200, 'highlight': False},
    'wmdp_bio_rephrased_translated_german': {'marker': 'd', 'label': 'Translated', 'size': 200, 'highlight': False},
    'wmdp_bio_rephrased_translated_korean': {'marker': 'd', 'label': 'Translated', 'size': 200, 'highlight': False},
}
for style in task_styles.values():
    style['size'] = style['size'] / 3

# Define filled tasks
filled_tasks = {
    'wmdp_bio',
    'tinyMMLU',
    'wmdp_bio_rephrased_english_filler',
    'wmdp_bio_rephrased_hindi_filler'
}

# Create figure with additional space at the top for the task legend
# fig = plt.figure(figsize=(15, 15))
fig = plt.figure(figsize=(5, 6))

# # Add the main plot with enough space at the top for the legend
# # This uses a percentage of the figure - bottom 80%, leaving 20% at top for legend
# main_ax = plt.axes([0.1, 0.1, 0.8, 0.8])

gs = fig.add_gridspec(2, 1, height_ratios=[1, 4])
task_legend_ax = fig.add_subplot(gs[0])
main_ax = fig.add_subplot(gs[1])
model_legend_ax = fig.add_subplot(gs[1])

# Hide the legend axes frames
task_legend_ax.axis('off')
model_legend_ax.axis('off')
plt.subplots_adjust(hspace=0.03)  # tighten vertical spacing

# Diagonal reference line
main_ax.plot([0, 1], [0, 1], 'k--', alpha=0.3)

# Plot points
for family in model_families:
    base_data = df[df['model'] == family['base']]
    elm_data = df[df['model'] == family['elm']]
    merged = pd.merge(base_data, elm_data, on='task', suffixes=('_base', '_elm'))

    for _, row in merged.iterrows():
        task = row['task']
        if task not in task_styles:
            continue

        style = task_styles[task]
        is_filled = task in filled_tasks
        is_highlight = style.get('highlight', False)

        facecolor = family['color'] if is_filled else 'none'
        edgecolor = 'black' if is_highlight else family['color']
        linewidth = 2 if is_highlight else 1

        main_ax.scatter(
            row['adjusted_accuracy_base'],
            row['adjusted_accuracy_elm'],
            facecolor=facecolor,
            edgecolor=edgecolor,
            marker=style['marker'],
            s=style.get('size', 100),
            linewidth=linewidth,
            alpha=0.9,
            zorder=5 if is_highlight else 4
        )

        if task == 'wmdp_bio_rephrased_hindi_filler':
            if family['name'] == 'Zephyr':
                main_ax.text(
                row['adjusted_accuracy_base'] + 0.006,
                row['adjusted_accuracy_elm'] + 0.01,
                'Hindi filler',
                fontsize=11,
                alpha=0.85
            )
            else:
                main_ax.text(
                    row['adjusted_accuracy_base'] + 0.011,
                    row['adjusted_accuracy_elm'] + 0.003,
                    'Hindi filler',
                    fontsize=11,
                    alpha=0.85
                )

# Axis labels
main_ax.set_xlabel(r'Base Model Accuracy (Adjusted)')
main_ax.set_ylabel(r'Unlearned (ELM) Model Accuracy (Adjusted)')
main_ax.set_xlim(0, 0.6)
main_ax.set_ylim(0, 0.6)

# Grid
main_ax.grid(True, linestyle='--', alpha=0.3)

# Model family legend - Keep in original position
model_legend = [
    Line2D([0], [0], marker='o', color=family['color'], label=family['name'],
           linestyle='', markersize=8) for family in model_families
]

# Task legend (preserve order and uniqueness)
ordered_tasks = [
    'tinyMMLU',
    'wmdp_bio',
    'wmdp_bio_rephrased_english_filler',
    'wmdp_bio_rephrased_hindi_filler',
    'wmdp_bio_rephrased_latin_filler'
]
seen_labels = set()
task_legend = []

# Helper to add a legend entry from a task key
def add_task_legend_entry(task_key, label_override=None):
    style = task_styles[task_key]
    label = label_override if label_override else style['label']
    if label in seen_labels:
        return
    seen_labels.add(label)
    is_highlight = style.get('highlight', False)
    facecolor = 'white' if is_highlight else '#999999'
    edgecolor = 'black' if is_highlight else '#999999'
    linewidth = 2.5 if is_highlight else 1.5

    task_legend.append(
        Line2D(
            [0], [0],
            marker=style['marker'],
            markerfacecolor=facecolor if not is_highlight else 'white',
            markeredgecolor=edgecolor,
            markeredgewidth=linewidth,
            linestyle='',
            markersize=10,
            label=label
        )
    )

# Add legend items in the requested order
add_task_legend_entry('tinyMMLU')  # MMLU
add_task_legend_entry('wmdp_bio')  # Base prompt
add_task_legend_entry('wmdp_bio_rephrased_hindi_filler', label_override='Knowledge retrieval')  # Highlighted
add_task_legend_entry('wmdp_bio_rephrased_english_filler')  # Filler text

# Add remaining task types not already seen
for task_key, style in task_styles.items():
    label = 'Knowledge retrieval' if task_key == 'wmdp_bio_rephrased_hindi_filler' else style['label']
    if label not in seen_labels:
        task_legend.append(
            Line2D(
                [0], [0],
                marker=style['marker'],
                markerfacecolor='none',
                markeredgecolor='#999999',
                markeredgewidth=1.5,
                linestyle='',
                markersize=10,
                label=label
            )
        )
        seen_labels.add(label)

legend1 = model_legend_ax.legend(
    handles=model_legend, 
    title='Models', 
    loc='upper left',
    # bbox_to_anchor=(0.0, 1),  
    columnspacing=0.5,
    handletextpad=0.3,
    handlelength=1.2,
    borderaxespad=0.2,
)

legend2 = task_legend_ax.legend(
    handles=task_legend,
    title='Tasks',
    loc='lower right',
    ncol=2,
    frameon=True,
    columnspacing=0.5,      # Reduce column gap
    handletextpad=0.3,      # Reduce gap between marker and label
    handlelength=1.2,       # Shorter marker length
    borderaxespad=0.2 
)

# Save figure
plt.savefig('model_performance_comparison.pdf', bbox_inches='tight', dpi=300)
plt.show()

print('Saved as: model_performance_comparison.pdf')