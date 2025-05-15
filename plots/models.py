import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import io
from matplotlib.lines import Line2D

# Enable LaTeX formatting and configure larger fonts
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "font.size": 18,
    "axes.titlesize": 24,
    "axes.labelsize": 24,
    "xtick.labelsize": 16,
    "ytick.labelsize": 16,
    "legend.fontsize": 18
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

df = pd.read_csv(io.StringIO(csv_data))

# Adjust accuracy
df['adjusted_accuracy'] = df['accuracy'] - 0.25
df['adjusted_accuracy'] = df['adjusted_accuracy'].clip(lower=0)

# Define model families with colorblind-friendly colors
model_families = [
    {'name': 'Zephyr', 'base': 'Zephyr_7B_Beta', 'elm': 'Zephyr-7B-ELM', 'color': '#0072B2'},
    {'name': 'Mistral', 'base': 'Mistral-7B-v0.1', 'elm': 'Mistral-7B-ELM', 'color': '#D55E00'},
    {'name': 'Llama3-8B', 'base': 'Llama3-8B', 'elm': 'Llama3-8B-ELM', 'color': '#009E73'},
    {'name': 'Llama3-8B-Instruct', 'base': 'Llama3-8B-Instruct', 'elm': 'Llama3-8B-Instruct-ELM', 'color': '#CC79A7'},
]

# Define task styles
task_styles = {
    'wmdp_bio': {
        'marker': 's', 'label': 'Base prompt', 'size': 240, 'highlight': False
    },
    'tinyMMLU': {
        'marker': '*', 'label': 'tinyMMLU', 'size': 300, 'highlight': False
    },
    'wmdp_bio_rephrased_english_filler': {
        'marker': 'o', 'label': 'Filler text', 'size': 160, 'highlight': False
    },
    'wmdp_bio_rephrased_hindi_filler': {
        'marker': 'o', 'label': 'Filler text', 'size': 160, 'highlight': True
    },
    'wmdp_bio_rephrased_latin_filler': {
        'marker': 'o', 'label': 'Filler text', 'size': 160, 'highlight': False
    },
    'wmdp_bio_rephrased_conversation': {
        'marker': '^', 'label': 'Rephrased as conversation', 'size': 160, 'highlight': False
    },
    'wmdp_bio_rephrased_poem': {
        'marker': 'v', 'label': 'Rephrased as poem', 'size': 160, 'highlight': False
    },
    'wmdp_bio_rephrased_replace_with_variables': {
        'marker': 'P', 'label': 'Replaced with variables', 'size': 160, 'highlight': False
    },
    'wmdp_bio_rephrased_technical_terms_removed_1': {
        'marker': 'X', 'label': 'Technical terms removed', 'size': 160, 'highlight': False
    },
    'wmdp_bio_rephrased_translated_farsi': {
        'marker': 'd', 'label': 'Translated', 'size': 160, 'highlight': False
    },
    'wmdp_bio_rephrased_translated_german': {
        'marker': 'd', 'label': 'Translated', 'size': 160, 'highlight': False
    },
    'wmdp_bio_rephrased_translated_korean': {
        'marker': 'd', 'label': 'Translated', 'size': 160, 'highlight': False
    },
}

# Create figure
plt.figure(figsize=(12, 10))
ax = plt.gca()

# Diagonal reference line
ax.plot([0, 1], [0, 1], 'k--', alpha=0.3)

# Plot points
for family in model_families:
    base_data = df[df['model'] == family['base']]
    elm_data = df[df['model'] == family['elm']]
    merged = pd.merge(base_data, elm_data, on='task', suffixes=('_base', '_elm'))

    for _, row in merged.iterrows():
        task = row['task']
        if task in task_styles:
            style = task_styles[task]

            edge_color = "#999999"
            highlight_edge = 'black'
            ax.scatter(
                row['adjusted_accuracy_base'],
                row['adjusted_accuracy_elm'],
                color=family['color'],
                marker=style['marker'],
                s=style.get('size', 100),
                edgecolor=highlight_edge if style.get('highlight', False) else edge_color,
                linewidth=2.5 if style.get('highlight', False) else 1.0,
                alpha=0.9,
                zorder=5 if style.get('highlight', False) else 4
            )

            # Annotate Hindi filler points
            if task == 'wmdp_bio_rephrased_hindi_filler':
                ax.text(
                    row['adjusted_accuracy_base'] + 0.007,
                    row['adjusted_accuracy_elm'] + 0.005,
                    'Hindi filler text',
                    fontsize=16,
                    alpha=0.85
                )


# Axis labels
ax.set_xlabel(r'Base model accuracy (adjusted)')
ax.set_ylabel(r'Unlearned (ELM) model accuracy (adjusted)')
ax.set_xlim(0, 0.55)
ax.set_ylim(0, 0.55)

# Model family legend
model_legend = [
    Line2D([0], [0], marker='o', color=family['color'], label=family['name'],
           linestyle='', markersize=14) for family in model_families
]

# De-duplicate task legend entries
task_seen = set()
task_legend = []
for key, style in task_styles.items():
    if style['label'] not in task_seen:
        task_seen.add(style['label'])
        task_legend.append( 
            Line2D(
                [0], [0],
                marker=style['marker'],
                markerfacecolor=edge_color,
                markeredgecolor=edge_color,
                label=style['label'],
                linestyle='',
                markersize=14
            )
        )


# Extra legend for highlighted Hindi filler
highlight_legend = Line2D(
    [0], [0], marker='o', color=highlight_edge, markerfacecolor='white',
    markeredgewidth=3, markersize=12, linestyle='', label='Knowledge retrieval'
)

# Add legends
legend1 = ax.legend(handles=model_legend, title='Models', loc='upper left', bbox_to_anchor=(0, 1))
legend2 = ax.legend(handles=task_legend + [highlight_legend], title='Tasks', loc='upper left', bbox_to_anchor=(0, 0.78))
ax.add_artist(legend1)

# Grid and layout
ax.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.savefig('model_performance_comparison.pdf', bbox_inches='tight', dpi=300)
plt.close()

print('Saved as: model_performance_comparison.pdf')
