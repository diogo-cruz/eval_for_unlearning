import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mpl

# Enable LaTeX rendering with necessary packages
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "text.latex.preamble": r"\usepackage{amsmath}\usepackage{amssymb}"
})

# Read the CSV file
df = pd.read_csv('multi.csv')

# Filter data to include only MMLU and WMDP-bio with user-assistant format
mmlu_data = df[df['fewshot_dataset'] == 'MMLU']
wmdp_bio_data = df[(df['fewshot_dataset'] == 'WMDP-bio') & (df['note'] == 'user-assistant format')]

plt.figure(figsize=(10, 8))

# Colorblind-friendly colors by model
model_colors = {
    'Zephyr_beta': '#0072B2',     # Blue
    'Zephyr_RMU': '#D55E00',      # Vermillion
    'LLM-GAT/ELM-8': '#009E73'    # Bluish green
}


# Markers by dataset
dataset_markers = {
    'MMLU': 'o',       # circle
    'WMDP-bio': 's'    # square
}

# Linestyles for better distinction (optional)
dataset_linestyles = {
    'MMLU': '-',
    'WMDP-bio': '--'
}

# Plot
for model in ['Zephyr_beta', 'Zephyr_RMU', 'LLM-GAT/ELM-8']:
    for dataset_name, dataset in [('MMLU', mmlu_data), ('WMDP-bio', wmdp_bio_data)]:
        model_data = dataset[dataset['Model'] == model].sort_values(by='n-shot')
        label = f"{model} ({dataset_name})"
        plt.plot(
            model_data['n-shot'], 
            model_data['WMDP-bio accuracy'], 
            label=label,
            color=model_colors[model],
            marker=dataset_markers[dataset_name],
            linestyle=dataset_linestyles[dataset_name],
            linewidth=2,
            markersize=8
        )

# Labels and styling
plt.xlabel(r"\textbf{$n$-shot}", fontsize=14)
plt.ylabel(r"\textbf{Accuracy}", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
# plt.legend(fontsize=12, loc='best')
plt.xticks([0, 1, 3, 5, 10, 20])
plt.ylim(0.2, 0.7)

from matplotlib.lines import Line2D

# --- Colorblind-friendly model legend ---
model_legend_elements = [
    Line2D([0], [0], color='#0072B2', lw=3, label='Zephyr\\_beta'),
    Line2D([0], [0], color='#D55E00', lw=3, label='Zephyr\\_RMU'),
    Line2D([0], [0], color='#009E73', lw=3, label='LLM-GAT/ELM-8')
]

# --- Dataset legend (marker/linestyle) ---
dataset_legend_elements = [
    Line2D([0], [0], color='black', marker='o', linestyle='-', label='MMLU', markersize=8),
    Line2D([0], [0], color='black', marker='s', linestyle='--', label='WMDP-bio', markersize=8)
]

# Place model legend (top one)
model_legend = plt.legend(handles=model_legend_elements, title='Model',
                          loc='center right', bbox_to_anchor=(1.0, 0.6),
                          fontsize=11, title_fontsize=12, frameon=True)

# Place dataset legend (just below the first)
dataset_legend = plt.legend(handles=dataset_legend_elements, title='Context Dataset',
                            loc='center right', bbox_to_anchor=(1.0, 0.45),
                            fontsize=11, title_fontsize=12, frameon=True)

# Add the model legend back manually so both are shown
plt.gca().add_artist(model_legend)

# Final layout
plt.tight_layout()
plt.subplots_adjust(bottom=0.15)
plt.savefig('multi_shot_performance.pdf', bbox_inches='tight')

print("Figure saved as 'multi_shot_performance.pdf'")
# plt.show()
