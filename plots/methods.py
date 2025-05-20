import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D

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

# Read CSV from file
df = pd.read_csv('unlearning_method_comparison.csv')

# Define method name mapping
method_name_map = {
    'tar': 'TAR',
    'graddiff': 'GradDiff',
    'repnoise': 'RepNoise',
    'elm': 'ELM',
    'rmu-lat': 'RMU+LAT',
    'rmu': 'RMU',
    'pbj': 'PBJ',
    'rr': 'RR'
}

# Extract base model data
base_model_data = df[df['model'] == 'Llama3-8B-Instruct']

# Process unlearning models data
unlearning_models = []
for method_key, method_name in method_name_map.items():
    model_name = f"LLM-GAT__llama-3-8b-instruct-{method_key}-checkpoint-8"
    if model_name in df['model'].values:
        unlearning_models.append({
            'name': method_name,
            'model': model_name,
            'color': None  # Will be assigned later
        })

# Wong's colorblind-friendly palette
colors = [
    '#882255',  # Burgundy
    '#56B4E9',  # Sky Blue
    '#E69F00',  # Orange
    '#009E73',  # Teal
    '#332288',  # Indigo
    '#AA7700',  # Dark Gold
    '#555555',  # Dark Gray
    '#CC79A7',  # Violet
]

# Assign colors to models
for i, model in enumerate(unlearning_models):
    model['color'] = colors[i % len(colors)]

# Define task styles
task_styles = {
    'wmdp_bio': {'marker': 's', 'label': 'Base prompt', 'size': 150, 'highlight': False},
    'tinyMMLU': {'marker': '*', 'label': 'tinyMMLU', 'size': 200, 'highlight': False},
    'wmdp_bio_rephrased_english_filler': {'marker': 'o', 'label': 'Filler text', 'size': 150, 'highlight': False},
    'wmdp_bio_rephrased_hindi_filler': {'marker': 'o', 'label': 'Filler text', 'size': 150, 'highlight': False},
    'wmdp_bio_rephrased_latin_filler': {'marker': 'o', 'label': 'Filler text', 'size': 150, 'highlight': False},
    'wmdp_bio_rephrased_conversation': {'marker': '^', 'label': 'Rephrased as conversation', 'size': 150, 'highlight': False},
    'wmdp_bio_rephrased_poem': {'marker': 'v', 'label': 'Rephrased as poem', 'size': 150, 'highlight': False},
    'wmdp_bio_rephrased_replace_with_variables': {'marker': 'P', 'label': 'Replaced with variables', 'size': 150, 'highlight': False},
    'wmdp_bio_rephrased_technical_terms_removed_1': {'marker': 'X', 'label': 'Technical terms removed', 'size': 150, 'highlight': False},
    'wmdp_bio_rephrased_translated_farsi': {'marker': 'd', 'label': 'Translated', 'size': 150, 'highlight': False},
    'wmdp_bio_rephrased_translated_german': {'marker': 'd', 'label': 'Translated', 'size': 150, 'highlight': False},
    'wmdp_bio_rephrased_translated_korean': {'marker': 'd', 'label': 'Translated', 'size': 150, 'highlight': False},
}
for style in task_styles.values():
    style['size'] = style['size'] / 3

# Define filled tasks
filled_tasks = {
    'wmdp_bio',
    'tinyMMLU',
}

# Create figure with space for stacked legends and plot
fig = plt.figure(figsize=(5.4, 6))

# Create a gridspec layout with space for legends above
# gs = fig.add_gridspec(3, 1, height_ratios=[1, 1, 6])
# task_legend_ax = fig.add_subplot(gs[0])
# method_legend_ax = fig.add_subplot(gs[1])
# ax = fig.add_subplot(gs[2])
gs = fig.add_gridspec(2, 1, height_ratios=[1, 4])
task_legend_ax = fig.add_subplot(gs[0])
ax = fig.add_subplot(gs[1])
method_legend_ax = fig.add_subplot(gs[1])

# Hide the legend axes frames
task_legend_ax.axis('off')
method_legend_ax.axis('off')
plt.subplots_adjust(hspace=0.03)  # tighten vertical spacing

adjustment_factor = 0.25

# Plot points
for model in unlearning_models:
    model_data = df[df['model'] == model['model']]
    
    for _, model_row in model_data.iterrows():
        task = model_row['task']
        if task not in task_styles:
            continue
            
        # Find corresponding base model accuracy for this task
        base_row = base_model_data[base_model_data['task'] == task]
        if len(base_row) == 0:
            continue
            
        base_accuracy = base_row['accuracy'].values[0] - adjustment_factor
        model_accuracy = model_row['accuracy'] - adjustment_factor
        
        # Skip if adjusted accuracy is negative
        if base_accuracy <= 0 or model_accuracy <= 0:
            continue
            
        style = task_styles[task]
        is_filled = task in filled_tasks
        is_highlight = style.get('highlight', False)
        
        facecolor = model['color'] if is_filled else 'none'
        edgecolor = 'black' if is_highlight else model['color']
        linewidth = 1
        
        # Add scatter point
        ax.scatter(
            base_accuracy,
            model_accuracy,
            facecolor=facecolor,
            edgecolor=edgecolor,
            marker=style['marker'],
            s=style['size'],
            linewidth=linewidth,
            alpha=0.9,
            zorder=5 if is_highlight else 4
        )

# Add diagonal reference line
ax.plot([-.01, 1], [-.01, 1], 'k--', alpha=0.3)

# Set labels and title
ax.set_xlabel('Base Model (Llama3-8B-Instruct) Accuracy (Adjusted)')
ax.set_ylabel('Unlearned Model Accuracy (Adjusted)')

# Set axis limits to 0.75 for both axes
ax.set_xlim(-.01, 0.5)
ax.set_ylim(-.01, 0.5)

# Add grid
ax.grid(True, linestyle='--', alpha=0.3)

# Create model legend
model_legend_handles = [
    Line2D([0], [0], marker='o', color=model['color'], label=model['name'],
           linestyle='', markersize=8) for model in unlearning_models
]

# Create task legend with priority for tinyMMLU
task_legend_handles = []

# First add tinyMMLU to legend
tinyMMLU_style = task_styles['tinyMMLU']
task_legend_handles.append(
    Line2D(
        [0], [0],
        marker=tinyMMLU_style['marker'],
        markerfacecolor='#999999' if 'tinyMMLU' in filled_tasks else 'none',
        markeredgecolor='black' if tinyMMLU_style.get('highlight', False) else '#999999',
        markeredgewidth=1.5,
        linestyle='',
        markersize=10,
        label=tinyMMLU_style['label']
    )
)

# Add all other task styles to legend
seen_labels = {tinyMMLU_style['label']}  # Initialize with tinyMMLU already added
for key, style in task_styles.items():
    if key == 'tinyMMLU':  # Skip tinyMMLU as it's already added
        continue
        
    label = style['label']
    if label not in seen_labels:
        seen_labels.add(label)
        is_highlight = style.get('highlight', False)
        
        # Use proper styling for legend items
        facecolor = 'none'  # Most markers are not filled
        if key in filled_tasks:
            facecolor = '#999999'  # Use gray for filled markers in legend
        
        edgecolor = 'black' if is_highlight else '#999999'
        linewidth = 1.5
        
        task_legend_handles.append(
            Line2D(
                [0], [0],
                marker=style['marker'],
                markerfacecolor=facecolor,
                markeredgecolor=edgecolor,
                markeredgewidth=linewidth,
                linestyle='',
                markersize=10,
                label=label
            )
        )

# Add legends with Tasks on top and Unlearning Methods below
task_legend = task_legend_ax.legend(
    handles=task_legend_handles,
    title='Tasks',
    loc='lower right',
    ncol=2,
    frameon=True,
    columnspacing=0.5,      # Reduce column gap
    handletextpad=0.3,      # Reduce gap between marker and label
    handlelength=1.2,       # Shorter marker length
    borderaxespad=0.2       # Reduce padding to axes
)

method_legend = method_legend_ax.legend(
    handles=model_legend_handles,
    title='Unlearning Methods',
    loc='upper left',
    ncol=2,
    frameon=True,
    columnspacing=0.5,
    handletextpad=0.3,
    handlelength=1.2,
    borderaxespad=0.2,
    # bbox_to_anchor=(-.1, 0),  # x = 0 (left), y > 1 = above plot
)


# Save figure as PDF
# plt.tight_layout()
plt.savefig('unlearning_methods_comparison.pdf', bbox_inches='tight', dpi=300)
plt.close()

print('Visualization saved as: unlearning_methods_comparison.pdf')