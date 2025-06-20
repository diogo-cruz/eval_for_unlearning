{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red131\green0\blue165;\red245\green245\blue245;\red0\green0\blue0;
\red15\green112\blue1;\red144\green1\blue18;\red0\green0\blue255;\red19\green85\blue52;\red31\green99\blue128;
\red86\green65\blue25;\red0\green0\blue109;}
{\*\expandedcolortbl;;\cssrgb\c59216\c13725\c70588;\cssrgb\c96863\c96863\c96863;\cssrgb\c0\c0\c0;
\cssrgb\c0\c50196\c0;\cssrgb\c63922\c8235\c8235;\cssrgb\c0\c0\c100000;\cssrgb\c6667\c40000\c26667;\cssrgb\c14510\c46275\c57647;
\cssrgb\c41569\c32157\c12941;\cssrgb\c0\c6275\c50196;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf0 \strokec4  matplotlib.pyplot \cf2 \strokec2 as\cf0 \strokec4  plt\cb1 \
\cf2 \cb3 \strokec2 import\cf0 \strokec4  numpy \cf2 \strokec2 as\cf0 \strokec4  np\cb1 \
\cf2 \cb3 \strokec2 import\cf0 \strokec4  pandas \cf2 \strokec2 as\cf0 \strokec4  pd\cb1 \
\cf2 \cb3 \strokec2 from\cf0 \strokec4  matplotlib.lines \cf2 \strokec2 import\cf0 \strokec4  Line2D\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Adjusted font sizes for better readability\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 plt.rcParams.update(\{\cb1 \
\cb3     \cf6 \strokec6 "text.usetex"\cf0 \strokec4 : \cf7 \strokec7 False\cf0 \strokec4 ,\cb1 \
\cb3     \cf6 \strokec6 "font.family"\cf0 \strokec4 : \cf6 \strokec6 "serif"\cf0 \strokec4 ,\cb1 \
\cb3     \cf6 \strokec6 "font.serif"\cf0 \strokec4 : [\cf6 \strokec6 "Computer Modern Roman"\cf0 \strokec4 ],\cb1 \
\cb3     \cf6 \strokec6 "font.size"\cf0 \strokec4 : \cf8 \strokec8 12\cf0 \strokec4 ,\cb1 \
\cb3     \cf6 \strokec6 "axes.titlesize"\cf0 \strokec4 : \cf8 \strokec8 14\cf0 \strokec4 ,\cb1 \
\cb3     \cf6 \strokec6 "axes.labelsize"\cf0 \strokec4 : \cf8 \strokec8 14\cf0 \strokec4 ,\cb1 \
\cb3     \cf6 \strokec6 "xtick.labelsize"\cf0 \strokec4 : \cf8 \strokec8 12\cf0 \strokec4 ,\cb1 \
\cb3     \cf6 \strokec6 "ytick.labelsize"\cf0 \strokec4 : \cf8 \strokec8 12\cf0 \strokec4 ,\cb1 \
\cb3     \cf6 \strokec6 "legend.fontsize"\cf0 \strokec4 : \cf8 \strokec8 12\cf0 \cb1 \strokec4 \
\cb3 \})\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Read CSV from external file\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 df = pd.read_csv(\cf6 \strokec6 'models.csv'\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Adjust accuracy\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 df[\cf6 \strokec6 'adjusted_accuracy'\cf0 \strokec4 ] = df[\cf6 \strokec6 'accuracy'\cf0 \strokec4 ] - \cf8 \strokec8 0.25\cf0 \cb1 \strokec4 \
\cb3 df[\cf6 \strokec6 'adjusted_accuracy'\cf0 \strokec4 ] = df[\cf6 \strokec6 'adjusted_accuracy'\cf0 \strokec4 ].clip(lower=\cf8 \strokec8 0\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Define model families\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 model_families = [\cb1 \
\cb3     \{\cf6 \strokec6 'name'\cf0 \strokec4 : \cf6 \strokec6 'Zephyr'\cf0 \strokec4 , \cf6 \strokec6 'base'\cf0 \strokec4 : \cf6 \strokec6 'Zephyr_7B_Beta'\cf0 \strokec4 , \cf6 \strokec6 'elm'\cf0 \strokec4 : \cf6 \strokec6 'Zephyr-7B-ELM'\cf0 \strokec4 , \cf6 \strokec6 'color'\cf0 \strokec4 : \cf6 \strokec6 '#0072B2'\cf0 \strokec4 \},\cb1 \
\cb3     \{\cf6 \strokec6 'name'\cf0 \strokec4 : \cf6 \strokec6 'Mistral'\cf0 \strokec4 , \cf6 \strokec6 'base'\cf0 \strokec4 : \cf6 \strokec6 'Mistral-7B-v0.1'\cf0 \strokec4 , \cf6 \strokec6 'elm'\cf0 \strokec4 : \cf6 \strokec6 'Mistral-7B-ELM'\cf0 \strokec4 , \cf6 \strokec6 'color'\cf0 \strokec4 : \cf6 \strokec6 '#D55E00'\cf0 \strokec4 \},\cb1 \
\cb3     \{\cf6 \strokec6 'name'\cf0 \strokec4 : \cf6 \strokec6 'Llama3-8B'\cf0 \strokec4 , \cf6 \strokec6 'base'\cf0 \strokec4 : \cf6 \strokec6 'Llama3-8B'\cf0 \strokec4 , \cf6 \strokec6 'elm'\cf0 \strokec4 : \cf6 \strokec6 'Llama3-8B-ELM'\cf0 \strokec4 , \cf6 \strokec6 'color'\cf0 \strokec4 : \cf6 \strokec6 '#009E73'\cf0 \strokec4 \},\cb1 \
\cb3     \{\cf6 \strokec6 'name'\cf0 \strokec4 : \cf6 \strokec6 'Llama3-8B-Instruct'\cf0 \strokec4 , \cf6 \strokec6 'base'\cf0 \strokec4 : \cf6 \strokec6 'Llama3-8B-Instruct'\cf0 \strokec4 , \cf6 \strokec6 'elm'\cf0 \strokec4 : \cf6 \strokec6 'Llama3-8B-Instruct-ELM'\cf0 \strokec4 , \cf6 \strokec6 'color'\cf0 \strokec4 : \cf6 \strokec6 '#CC79A7'\cf0 \strokec4 \},\cb1 \
\cb3 ]\cb1 \
\
\cb3 task_styles = \{\cb1 \
\cb3     \cf6 \strokec6 'wmdp_bio'\cf0 \strokec4 : \{\cf6 \strokec6 'marker'\cf0 \strokec4 : \cf6 \strokec6 's'\cf0 \strokec4 , \cf6 \strokec6 'label'\cf0 \strokec4 : \cf6 \strokec6 'Base prompt'\cf0 \strokec4 , \cf6 \strokec6 'size'\cf0 \strokec4 : \cf8 \strokec8 300\cf0 \strokec4 , \cf6 \strokec6 'highlight'\cf0 \strokec4 : \cf7 \strokec7 False\cf0 \strokec4 \},\cb1 \
\cb3     \cf6 \strokec6 'tinyMMLU'\cf0 \strokec4 : \{\cf6 \strokec6 'marker'\cf0 \strokec4 : \cf6 \strokec6 '*'\cf0 \strokec4 , \cf6 \strokec6 'label'\cf0 \strokec4 : \cf6 \strokec6 'tinyMMLU'\cf0 \strokec4 , \cf6 \strokec6 'size'\cf0 \strokec4 : \cf8 \strokec8 375\cf0 \strokec4 , \cf6 \strokec6 'highlight'\cf0 \strokec4 : \cf7 \strokec7 False\cf0 \strokec4 \},\cb1 \
\cb3     \cf6 \strokec6 'wmdp_bio_rephrased_english_filler'\cf0 \strokec4 : \{\cf6 \strokec6 'marker'\cf0 \strokec4 : \cf6 \strokec6 'o'\cf0 \strokec4 , \cf6 \strokec6 'label'\cf0 \strokec4 : \cf6 \strokec6 'Filler text'\cf0 \strokec4 , \cf6 \strokec6 'size'\cf0 \strokec4 : \cf8 \strokec8 200\cf0 \strokec4 , \cf6 \strokec6 'highlight'\cf0 \strokec4 : \cf7 \strokec7 False\cf0 \strokec4 \},\cb1 \
\cb3     \cf6 \strokec6 'wmdp_bio_rephrased_hindi_filler'\cf0 \strokec4 : \{\cf6 \strokec6 'marker'\cf0 \strokec4 : \cf6 \strokec6 'o'\cf0 \strokec4 , \cf6 \strokec6 'label'\cf0 \strokec4 : \cf6 \strokec6 'Filler text'\cf0 \strokec4 , \cf6 \strokec6 'size'\cf0 \strokec4 : \cf8 \strokec8 200\cf0 \strokec4 , \cf6 \strokec6 'highlight'\cf0 \strokec4 : \cf7 \strokec7 True\cf0 \strokec4 \},\cb1 \
\cb3     \cf6 \strokec6 'wmdp_bio_rephrased_latin_filler'\cf0 \strokec4 : \{\cf6 \strokec6 'marker'\cf0 \strokec4 : \cf6 \strokec6 'o'\cf0 \strokec4 , \cf6 \strokec6 'label'\cf0 \strokec4 : \cf6 \strokec6 'Filler text'\cf0 \strokec4 , \cf6 \strokec6 'size'\cf0 \strokec4 : \cf8 \strokec8 200\cf0 \strokec4 , \cf6 \strokec6 'highlight'\cf0 \strokec4 : \cf7 \strokec7 False\cf0 \strokec4 \},\cb1 \
\cb3     \cf6 \strokec6 'wmdp_bio_rephrased_conversation'\cf0 \strokec4 : \{\cf6 \strokec6 'marker'\cf0 \strokec4 : \cf6 \strokec6 '^'\cf0 \strokec4 , \cf6 \strokec6 'label'\cf0 \strokec4 : \cf6 \strokec6 'Rephrased as conversation'\cf0 \strokec4 , \cf6 \strokec6 'size'\cf0 \strokec4 : \cf8 \strokec8 200\cf0 \strokec4 , \cf6 \strokec6 'highlight'\cf0 \strokec4 : \cf7 \strokec7 False\cf0 \strokec4 \},\cb1 \
\cb3     \cf6 \strokec6 'wmdp_bio_rephrased_poem'\cf0 \strokec4 : \{\cf6 \strokec6 'marker'\cf0 \strokec4 : \cf6 \strokec6 'v'\cf0 \strokec4 , \cf6 \strokec6 'label'\cf0 \strokec4 : \cf6 \strokec6 'Rephrased as poem'\cf0 \strokec4 , \cf6 \strokec6 'size'\cf0 \strokec4 : \cf8 \strokec8 200\cf0 \strokec4 , \cf6 \strokec6 'highlight'\cf0 \strokec4 : \cf7 \strokec7 False\cf0 \strokec4 \},\cb1 \
\cb3     \cf6 \strokec6 'wmdp_bio_rephrased_replace_with_variables'\cf0 \strokec4 : \{\cf6 \strokec6 'marker'\cf0 \strokec4 : \cf6 \strokec6 'P'\cf0 \strokec4 , \cf6 \strokec6 'label'\cf0 \strokec4 : \cf6 \strokec6 'Replaced with variables'\cf0 \strokec4 , \cf6 \strokec6 'size'\cf0 \strokec4 : \cf8 \strokec8 200\cf0 \strokec4 , \cf6 \strokec6 'highlight'\cf0 \strokec4 : \cf7 \strokec7 False\cf0 \strokec4 \},\cb1 \
\cb3     \cf6 \strokec6 'wmdp_bio_rephrased_technical_terms_removed_1'\cf0 \strokec4 : \{\cf6 \strokec6 'marker'\cf0 \strokec4 : \cf6 \strokec6 'X'\cf0 \strokec4 , \cf6 \strokec6 'label'\cf0 \strokec4 : \cf6 \strokec6 'Technical terms removed'\cf0 \strokec4 , \cf6 \strokec6 'size'\cf0 \strokec4 : \cf8 \strokec8 200\cf0 \strokec4 , \cf6 \strokec6 'highlight'\cf0 \strokec4 : \cf7 \strokec7 False\cf0 \strokec4 \},\cb1 \
\cb3     \cf6 \strokec6 'wmdp_bio_rephrased_translated_farsi'\cf0 \strokec4 : \{\cf6 \strokec6 'marker'\cf0 \strokec4 : \cf6 \strokec6 'd'\cf0 \strokec4 , \cf6 \strokec6 'label'\cf0 \strokec4 : \cf6 \strokec6 'Translated'\cf0 \strokec4 , \cf6 \strokec6 'size'\cf0 \strokec4 : \cf8 \strokec8 200\cf0 \strokec4 , \cf6 \strokec6 'highlight'\cf0 \strokec4 : \cf7 \strokec7 False\cf0 \strokec4 \},\cb1 \
\cb3     \cf6 \strokec6 'wmdp_bio_rephrased_translated_german'\cf0 \strokec4 : \{\cf6 \strokec6 'marker'\cf0 \strokec4 : \cf6 \strokec6 'd'\cf0 \strokec4 , \cf6 \strokec6 'label'\cf0 \strokec4 : \cf6 \strokec6 'Translated'\cf0 \strokec4 , \cf6 \strokec6 'size'\cf0 \strokec4 : \cf8 \strokec8 200\cf0 \strokec4 , \cf6 \strokec6 'highlight'\cf0 \strokec4 : \cf7 \strokec7 False\cf0 \strokec4 \},\cb1 \
\cb3     \cf6 \strokec6 'wmdp_bio_rephrased_translated_korean'\cf0 \strokec4 : \{\cf6 \strokec6 'marker'\cf0 \strokec4 : \cf6 \strokec6 'd'\cf0 \strokec4 , \cf6 \strokec6 'label'\cf0 \strokec4 : \cf6 \strokec6 'Translated'\cf0 \strokec4 , \cf6 \strokec6 'size'\cf0 \strokec4 : \cf8 \strokec8 200\cf0 \strokec4 , \cf6 \strokec6 'highlight'\cf0 \strokec4 : \cf7 \strokec7 False\cf0 \strokec4 \},\cb1 \
\cb3 \}\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 for\cf0 \strokec4  style \cf7 \strokec7 in\cf0 \strokec4  task_styles.values():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     style[\cf6 \strokec6 'size'\cf0 \strokec4 ] = style[\cf6 \strokec6 'size'\cf0 \strokec4 ] / \cf8 \strokec8 3\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Define filled tasks\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 filled_tasks = \{\cb1 \
\cb3     \cf6 \strokec6 'wmdp_bio'\cf0 \strokec4 ,\cb1 \
\cb3     \cf6 \strokec6 'tinyMMLU'\cf0 \strokec4 ,\cb1 \
\cb3     \cf6 \strokec6 'wmdp_bio_rephrased_english_filler'\cf0 \strokec4 ,\cb1 \
\cb3     \cf6 \strokec6 'wmdp_bio_rephrased_hindi_filler'\cf0 \cb1 \strokec4 \
\cb3 \}\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Create figure with additional space at the top for the task legend\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # fig = plt.figure(figsize=(5.4, 12))\cf0 \cb1 \strokec4 \
\
\cf5 \cb3 \strokec5 # # # Add the main plot with enough space at the top for the legend\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # # # This uses a percentage of the figure - bottom 80%, leaving 20% at top for legend\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # # main_ax = plt.axes([0.1, 0.1, 0.8, 0.8])\cf0 \cb1 \strokec4 \
\
\cf5 \cb3 \strokec5 # gs = fig.add_gridspec(4, 1, height_ratios=[1, 4, .8, 4])\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # task_legend_ax = fig.add_subplot(gs[0])\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # main_ax = fig.add_subplot(gs[1])\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # model_legend_ax = fig.add_subplot(gs[1])\cf0 \cb1 \strokec4 \
\
\cf5 \cb3 \strokec5 # ax2 = fig.add_subplot(gs[2])\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # ax2.axis("off")  # This is just for spacing\cf0 \cb1 \strokec4 \
\
\cf5 \cb3 \strokec5 # # Hide the legend axes frames\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # task_legend_ax.axis('off')\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # model_legend_ax.axis('off')\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # plt.subplots_adjust(hspace=0.03)  # tighten vertical spacing\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 fig = plt.figure(figsize=(\cf8 \strokec8 14\cf0 \strokec4 , \cf8 \strokec8 10\cf0 \strokec4 ))\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # # Add the main plot with enough space at the top for the legend\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # # This uses a percentage of the figure - bottom 80%, leaving 20% at top for legend\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # main_ax = plt.axes([0.1, 0.1, 0.8, 0.8])\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 gs = fig.add_gridspec(\cf8 \strokec8 2\cf0 \strokec4 , \cf8 \strokec8 2\cf0 \strokec4 , height_ratios=[\cf8 \strokec8 1\cf0 \strokec4 , \cf8 \strokec8 4\cf0 \strokec4 ])\cb1 \
\cb3 task_legend_ax = fig.add_subplot(gs[\cf8 \strokec8 0\cf0 \strokec4 ,:])\cb1 \
\cb3 main_ax = fig.add_subplot(gs[\cf8 \strokec8 1\cf0 \strokec4 ,\cf8 \strokec8 0\cf0 \strokec4 ])\cb1 \
\cb3 model_legend_ax = fig.add_subplot(gs[\cf8 \strokec8 1\cf0 \strokec4 ,\cf8 \strokec8 0\cf0 \strokec4 ])\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # ax2 = fig.add_subplot(gs[2])\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # ax2.axis("off")  # This is just for spacing\cf0 \cb1 \strokec4 \
\
\cf5 \cb3 \strokec5 # Hide the legend axes frames\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 task_legend_ax.axis(\cf6 \strokec6 'off'\cf0 \strokec4 )\cb1 \
\cb3 model_legend_ax.axis(\cf6 \strokec6 'off'\cf0 \strokec4 )\cb1 \
\cb3 plt.subplots_adjust(hspace=\cf8 \strokec8 0.03\cf0 \strokec4 )  \cf5 \strokec5 # tighten vertical spacing\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Diagonal reference line\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 main_ax.plot([\cf8 \strokec8 0\cf0 \strokec4 , \cf8 \strokec8 1\cf0 \strokec4 ], [\cf8 \strokec8 0\cf0 \strokec4 , \cf8 \strokec8 1\cf0 \strokec4 ], \cf6 \strokec6 'k--'\cf0 \strokec4 , alpha=\cf8 \strokec8 0.3\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Plot points\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 for\cf0 \strokec4  family \cf7 \strokec7 in\cf0 \strokec4  model_families:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     base_data = df[df[\cf6 \strokec6 'model'\cf0 \strokec4 ] == family[\cf6 \strokec6 'base'\cf0 \strokec4 ]]\cb1 \
\cb3     elm_data = df[df[\cf6 \strokec6 'model'\cf0 \strokec4 ] == family[\cf6 \strokec6 'elm'\cf0 \strokec4 ]]\cb1 \
\cb3     merged = pd.merge(base_data, elm_data, on=\cf6 \strokec6 'task'\cf0 \strokec4 , suffixes=(\cf6 \strokec6 '_base'\cf0 \strokec4 , \cf6 \strokec6 '_elm'\cf0 \strokec4 ))\cb1 \
\
\cb3     \cf2 \strokec2 for\cf0 \strokec4  _, row \cf7 \strokec7 in\cf0 \strokec4  merged.iterrows():\cb1 \
\cb3         task = row[\cf6 \strokec6 'task'\cf0 \strokec4 ]\cb1 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  task \cf7 \strokec7 not\cf0 \strokec4  \cf7 \strokec7 in\cf0 \strokec4  task_styles:\cb1 \
\cb3             \cf2 \strokec2 continue\cf0 \cb1 \strokec4 \
\
\cb3         style = task_styles[task]\cb1 \
\cb3         is_filled = task \cf7 \strokec7 in\cf0 \strokec4  filled_tasks\cb1 \
\cb3         is_highlight = style.get(\cf6 \strokec6 'highlight'\cf0 \strokec4 , \cf7 \strokec7 False\cf0 \strokec4 )\cb1 \
\
\cb3         facecolor = family[\cf6 \strokec6 'color'\cf0 \strokec4 ] \cf2 \strokec2 if\cf0 \strokec4  is_filled \cf2 \strokec2 else\cf0 \strokec4  \cf6 \strokec6 'none'\cf0 \cb1 \strokec4 \
\cb3         edgecolor = \cf6 \strokec6 'black'\cf0 \strokec4  \cf2 \strokec2 if\cf0 \strokec4  is_highlight \cf2 \strokec2 else\cf0 \strokec4  family[\cf6 \strokec6 'color'\cf0 \strokec4 ]\cb1 \
\cb3         linewidth = \cf8 \strokec8 2\cf0 \strokec4  \cf2 \strokec2 if\cf0 \strokec4  is_highlight \cf2 \strokec2 else\cf0 \strokec4  \cf8 \strokec8 1\cf0 \cb1 \strokec4 \
\
\cb3         main_ax.scatter(\cb1 \
\cb3             row[\cf6 \strokec6 'adjusted_accuracy_base'\cf0 \strokec4 ],\cb1 \
\cb3             row[\cf6 \strokec6 'adjusted_accuracy_elm'\cf0 \strokec4 ],\cb1 \
\cb3             facecolor=facecolor,\cb1 \
\cb3             edgecolor=edgecolor,\cb1 \
\cb3             marker=style[\cf6 \strokec6 'marker'\cf0 \strokec4 ],\cb1 \
\cb3             s=style.get(\cf6 \strokec6 'size'\cf0 \strokec4 , \cf8 \strokec8 100\cf0 \strokec4 ),\cb1 \
\cb3             linewidth=linewidth,\cb1 \
\cb3             alpha=\cf8 \strokec8 0.9\cf0 \strokec4 ,\cb1 \
\cb3             zorder=\cf8 \strokec8 5\cf0 \strokec4  \cf2 \strokec2 if\cf0 \strokec4  is_highlight \cf2 \strokec2 else\cf0 \strokec4  \cf8 \strokec8 4\cf0 \cb1 \strokec4 \
\cb3         )\cb1 \
\
\cb3         \cf2 \strokec2 if\cf0 \strokec4  task == \cf6 \strokec6 'wmdp_bio_rephrased_hindi_filler'\cf0 \strokec4 :\cb1 \
\cb3             \cf2 \strokec2 if\cf0 \strokec4  family[\cf6 \strokec6 'name'\cf0 \strokec4 ] == \cf6 \strokec6 'Zephyr'\cf0 \strokec4 :\cb1 \
\cb3                 main_ax.text(\cb1 \
\cb3                 row[\cf6 \strokec6 'adjusted_accuracy_base'\cf0 \strokec4 ] + \cf8 \strokec8 0.006\cf0 \strokec4 ,\cb1 \
\cb3                 row[\cf6 \strokec6 'adjusted_accuracy_elm'\cf0 \strokec4 ] + \cf8 \strokec8 0.01\cf0 \strokec4 ,\cb1 \
\cb3                 \cf6 \strokec6 'Hindi filler'\cf0 \strokec4 ,\cb1 \
\cb3                 fontsize=\cf8 \strokec8 11\cf0 \strokec4 ,\cb1 \
\cb3                 alpha=\cf8 \strokec8 0.85\cf0 \cb1 \strokec4 \
\cb3             )\cb1 \
\cb3             \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3                 main_ax.text(\cb1 \
\cb3                     row[\cf6 \strokec6 'adjusted_accuracy_base'\cf0 \strokec4 ] + \cf8 \strokec8 0.011\cf0 \strokec4 ,\cb1 \
\cb3                     row[\cf6 \strokec6 'adjusted_accuracy_elm'\cf0 \strokec4 ] + \cf8 \strokec8 0.003\cf0 \strokec4 ,\cb1 \
\cb3                     \cf6 \strokec6 'Hindi filler'\cf0 \strokec4 ,\cb1 \
\cb3                     fontsize=\cf8 \strokec8 11\cf0 \strokec4 ,\cb1 \
\cb3                     alpha=\cf8 \strokec8 0.85\cf0 \cb1 \strokec4 \
\cb3                 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Axis labels\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 main_ax.set_xlabel(r\cf6 \strokec6 'Base Model Accuracy (Adjusted)'\cf0 \strokec4 )\cb1 \
\cb3 main_ax.set_ylabel(r\cf6 \strokec6 'Unlearned (ELM) Model Accuracy (Adjusted)'\cf0 \strokec4 )\cb1 \
\cb3 main_ax.set_xlim(\cf8 \strokec8 0\cf0 \strokec4 , \cf8 \strokec8 0.6\cf0 \strokec4 )\cb1 \
\cb3 main_ax.set_ylim(\cf8 \strokec8 0\cf0 \strokec4 , \cf8 \strokec8 0.6\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Grid\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 main_ax.grid(\cf7 \strokec7 True\cf0 \strokec4 , linestyle=\cf6 \strokec6 '--'\cf0 \strokec4 , alpha=\cf8 \strokec8 0.3\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Model family legend - Keep in original position\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 model_legend = [\cb1 \
\cb3     Line2D([\cf8 \strokec8 0\cf0 \strokec4 ], [\cf8 \strokec8 0\cf0 \strokec4 ], marker=\cf6 \strokec6 'o'\cf0 \strokec4 , color=family[\cf6 \strokec6 'color'\cf0 \strokec4 ], label=family[\cf6 \strokec6 'name'\cf0 \strokec4 ],\cb1 \
\cb3            linestyle=\cf6 \strokec6 ''\cf0 \strokec4 , markersize=\cf8 \strokec8 8\cf0 \strokec4 ) \cf2 \strokec2 for\cf0 \strokec4  family \cf7 \strokec7 in\cf0 \strokec4  model_families\cb1 \
\cb3 ]\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Task legend (preserve order and uniqueness)\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 ordered_tasks = [\cb1 \
\cb3     \cf6 \strokec6 'tinyMMLU'\cf0 \strokec4 ,\cb1 \
\cb3     \cf6 \strokec6 'wmdp_bio'\cf0 \strokec4 ,\cb1 \
\cb3     \cf6 \strokec6 'wmdp_bio_rephrased_english_filler'\cf0 \strokec4 ,\cb1 \
\cb3     \cf6 \strokec6 'wmdp_bio_rephrased_hindi_filler'\cf0 \strokec4 ,\cb1 \
\cb3     \cf6 \strokec6 'wmdp_bio_rephrased_latin_filler'\cf0 \cb1 \strokec4 \
\cb3 ]\cb1 \
\cb3 seen_labels = \cf9 \strokec9 set\cf0 \strokec4 ()\cb1 \
\cb3 task_legend = []\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Helper to add a legend entry from a task key\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 def\cf0 \strokec4  \cf10 \strokec10 add_task_legend_entry\cf0 \strokec4 (\cf11 \strokec11 task_key\cf0 \strokec4 , \cf11 \strokec11 label_override\cf0 \strokec4 =\cf7 \strokec7 None\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     style = task_styles[task_key]\cb1 \
\cb3     label = label_override \cf2 \strokec2 if\cf0 \strokec4  label_override \cf2 \strokec2 else\cf0 \strokec4  style[\cf6 \strokec6 'label'\cf0 \strokec4 ]\cb1 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  label \cf7 \strokec7 in\cf0 \strokec4  seen_labels:\cb1 \
\cb3         \cf2 \strokec2 return\cf0 \cb1 \strokec4 \
\cb3     seen_labels.add(label)\cb1 \
\cb3     is_highlight = style.get(\cf6 \strokec6 'highlight'\cf0 \strokec4 , \cf7 \strokec7 False\cf0 \strokec4 )\cb1 \
\cb3     facecolor = \cf6 \strokec6 'white'\cf0 \strokec4  \cf2 \strokec2 if\cf0 \strokec4  is_highlight \cf2 \strokec2 else\cf0 \strokec4  \cf6 \strokec6 '#999999'\cf0 \cb1 \strokec4 \
\cb3     edgecolor = \cf6 \strokec6 'black'\cf0 \strokec4  \cf2 \strokec2 if\cf0 \strokec4  is_highlight \cf2 \strokec2 else\cf0 \strokec4  \cf6 \strokec6 '#999999'\cf0 \cb1 \strokec4 \
\cb3     linewidth = \cf8 \strokec8 2.5\cf0 \strokec4  \cf2 \strokec2 if\cf0 \strokec4  is_highlight \cf2 \strokec2 else\cf0 \strokec4  \cf8 \strokec8 1.5\cf0 \cb1 \strokec4 \
\
\cb3     task_legend.append(\cb1 \
\cb3         Line2D(\cb1 \
\cb3             [\cf8 \strokec8 0\cf0 \strokec4 ], [\cf8 \strokec8 0\cf0 \strokec4 ],\cb1 \
\cb3             marker=style[\cf6 \strokec6 'marker'\cf0 \strokec4 ],\cb1 \
\cb3             markerfacecolor=facecolor \cf2 \strokec2 if\cf0 \strokec4  \cf7 \strokec7 not\cf0 \strokec4  is_highlight \cf2 \strokec2 else\cf0 \strokec4  \cf6 \strokec6 'white'\cf0 \strokec4 ,\cb1 \
\cb3             markeredgecolor=edgecolor,\cb1 \
\cb3             markeredgewidth=linewidth,\cb1 \
\cb3             linestyle=\cf6 \strokec6 ''\cf0 \strokec4 ,\cb1 \
\cb3             markersize=\cf8 \strokec8 10\cf0 \strokec4 ,\cb1 \
\cb3             label=label\cb1 \
\cb3         )\cb1 \
\cb3     )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Add legend items in the requested order\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 add_task_legend_entry(\cf6 \strokec6 'tinyMMLU'\cf0 \strokec4 )  \cf5 \strokec5 # MMLU\cf0 \cb1 \strokec4 \
\cb3 add_task_legend_entry(\cf6 \strokec6 'wmdp_bio'\cf0 \strokec4 )  \cf5 \strokec5 # Base prompt\cf0 \cb1 \strokec4 \
\cb3 add_task_legend_entry(\cf6 \strokec6 'wmdp_bio_rephrased_hindi_filler'\cf0 \strokec4 , label_override=\cf6 \strokec6 'Knowledge retrieval'\cf0 \strokec4 )  \cf5 \strokec5 # Highlighted\cf0 \cb1 \strokec4 \
\cb3 add_task_legend_entry(\cf6 \strokec6 'wmdp_bio_rephrased_english_filler'\cf0 \strokec4 )  \cf5 \strokec5 # Filler text\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Add remaining task types not already seen\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 for\cf0 \strokec4  task_key, style \cf7 \strokec7 in\cf0 \strokec4  task_styles.items():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     label = \cf6 \strokec6 'Knowledge retrieval'\cf0 \strokec4  \cf2 \strokec2 if\cf0 \strokec4  task_key == \cf6 \strokec6 'wmdp_bio_rephrased_hindi_filler'\cf0 \strokec4  \cf2 \strokec2 else\cf0 \strokec4  style[\cf6 \strokec6 'label'\cf0 \strokec4 ]\cb1 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  label \cf7 \strokec7 not\cf0 \strokec4  \cf7 \strokec7 in\cf0 \strokec4  seen_labels:\cb1 \
\cb3         task_legend.append(\cb1 \
\cb3             Line2D(\cb1 \
\cb3                 [\cf8 \strokec8 0\cf0 \strokec4 ], [\cf8 \strokec8 0\cf0 \strokec4 ],\cb1 \
\cb3                 marker=style[\cf6 \strokec6 'marker'\cf0 \strokec4 ],\cb1 \
\cb3                 markerfacecolor=\cf6 \strokec6 'none'\cf0 \strokec4 ,\cb1 \
\cb3                 markeredgecolor=\cf6 \strokec6 '#999999'\cf0 \strokec4 ,\cb1 \
\cb3                 markeredgewidth=\cf8 \strokec8 1.5\cf0 \strokec4 ,\cb1 \
\cb3                 linestyle=\cf6 \strokec6 ''\cf0 \strokec4 ,\cb1 \
\cb3                 markersize=\cf8 \strokec8 10\cf0 \strokec4 ,\cb1 \
\cb3                 label=label\cb1 \
\cb3             )\cb1 \
\cb3         )\cb1 \
\cb3         seen_labels.add(label)\cb1 \
\
\cb3 legend1 = model_legend_ax.legend(\cb1 \
\cb3     handles=model_legend, \cb1 \
\cb3     title=\cf6 \strokec6 'Models'\cf0 \strokec4 , \cb1 \
\cb3     loc=\cf6 \strokec6 'upper left'\cf0 \strokec4 ,\cb1 \
\cb3     \cf5 \strokec5 # bbox_to_anchor=(0.0, 1),  \cf0 \cb1 \strokec4 \
\cb3     columnspacing=\cf8 \strokec8 0.5\cf0 \strokec4 ,\cb1 \
\cb3     handletextpad=\cf8 \strokec8 0.3\cf0 \strokec4 ,\cb1 \
\cb3     handlelength=\cf8 \strokec8 1.2\cf0 \strokec4 ,\cb1 \
\cb3     borderaxespad=\cf8 \strokec8 0.2\cf0 \strokec4 ,\cb1 \
\cb3 )\cb1 \
\
\cb3 legend2 = task_legend_ax.legend(\cb1 \
\cb3     handles=task_legend,\cb1 \
\cb3     title=\cf6 \strokec6 'Tasks'\cf0 \strokec4 ,\cb1 \
\cb3     \cf5 \strokec5 # loc='lower right',\cf0 \cb1 \strokec4 \
\cb3     loc=\cf6 \strokec6 'center'\cf0 \strokec4 ,\cb1 \
\cb3     ncol=\cf8 \strokec8 2\cf0 \strokec4 ,\cb1 \
\cb3     frameon=\cf7 \strokec7 True\cf0 \strokec4 ,\cb1 \
\cb3     columnspacing=\cf8 \strokec8 0.5\cf0 \strokec4 ,      \cf5 \strokec5 # Reduce column gap\cf0 \cb1 \strokec4 \
\cb3     handletextpad=\cf8 \strokec8 0.3\cf0 \strokec4 ,      \cf5 \strokec5 # Reduce gap between marker and label\cf0 \cb1 \strokec4 \
\cb3     handlelength=\cf8 \strokec8 1.2\cf0 \strokec4 ,       \cf5 \strokec5 # Shorter marker length\cf0 \cb1 \strokec4 \
\cb3     borderaxespad=\cf8 \strokec8 0.2\cf0 \strokec4  \cb1 \
\cb3 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # # Save figure\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # plt.savefig('model_performance_comparison.pdf', bbox_inches='tight', dpi=300)\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # plt.show()\cf0 \cb1 \strokec4 \
\
\cf5 \cb3 \strokec5 # print('Saved as: model_performance_comparison.pdf')\cf0 \cb1 \strokec4 \
\
\cf5 \cb3 \strokec5 # Read CSV from file\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 df = pd.read_csv(\cf6 \strokec6 'unlearning_method_comparison.csv'\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Define method name mapping\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 method_name_map = \{\cb1 \
\cb3     \cf6 \strokec6 'tar'\cf0 \strokec4 : \cf6 \strokec6 'TAR'\cf0 \strokec4 ,\cb1 \
\cb3     \cf6 \strokec6 'graddiff'\cf0 \strokec4 : \cf6 \strokec6 'GradDiff'\cf0 \strokec4 ,\cb1 \
\cb3     \cf6 \strokec6 'repnoise'\cf0 \strokec4 : \cf6 \strokec6 'RepNoise'\cf0 \strokec4 ,\cb1 \
\cb3     \cf6 \strokec6 'elm'\cf0 \strokec4 : \cf6 \strokec6 'ELM'\cf0 \strokec4 ,\cb1 \
\cb3     \cf6 \strokec6 'rmu-lat'\cf0 \strokec4 : \cf6 \strokec6 'RMU+LAT'\cf0 \strokec4 ,\cb1 \
\cb3     \cf6 \strokec6 'rmu'\cf0 \strokec4 : \cf6 \strokec6 'RMU'\cf0 \strokec4 ,\cb1 \
\cb3     \cf6 \strokec6 'pbj'\cf0 \strokec4 : \cf6 \strokec6 'PBJ'\cf0 \strokec4 ,\cb1 \
\cb3     \cf6 \strokec6 'rr'\cf0 \strokec4 : \cf6 \strokec6 'RR'\cf0 \cb1 \strokec4 \
\cb3 \}\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Extract base model data\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 base_model_data = df[df[\cf6 \strokec6 'model'\cf0 \strokec4 ] == \cf6 \strokec6 'Llama3-8B-Instruct'\cf0 \strokec4 ]\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Process unlearning models data\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 unlearning_models = []\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 for\cf0 \strokec4  method_key, method_name \cf7 \strokec7 in\cf0 \strokec4  method_name_map.items():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     model_name = \cf7 \strokec7 f\cf6 \strokec6 "LLM-GAT__llama-3-8b-instruct-\cf0 \strokec4 \{method_key\}\cf6 \strokec6 -checkpoint-8"\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  model_name \cf7 \strokec7 in\cf0 \strokec4  df[\cf6 \strokec6 'model'\cf0 \strokec4 ].values:\cb1 \
\cb3         unlearning_models.append(\{\cb1 \
\cb3             \cf6 \strokec6 'name'\cf0 \strokec4 : method_name,\cb1 \
\cb3             \cf6 \strokec6 'model'\cf0 \strokec4 : model_name,\cb1 \
\cb3             \cf6 \strokec6 'color'\cf0 \strokec4 : \cf7 \strokec7 None\cf0 \strokec4   \cf5 \strokec5 # Will be assigned later\cf0 \cb1 \strokec4 \
\cb3         \})\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Wong's colorblind-friendly palette\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 colors = [\cb1 \
\cb3     \cf6 \strokec6 '#882255'\cf0 \strokec4 ,  \cf5 \strokec5 # Burgundy\cf0 \cb1 \strokec4 \
\cb3     \cf6 \strokec6 '#56B4E9'\cf0 \strokec4 ,  \cf5 \strokec5 # Sky Blue\cf0 \cb1 \strokec4 \
\cb3     \cf6 \strokec6 '#E69F00'\cf0 \strokec4 ,  \cf5 \strokec5 # Orange\cf0 \cb1 \strokec4 \
\cb3     \cf6 \strokec6 '#009E73'\cf0 \strokec4 ,  \cf5 \strokec5 # Teal\cf0 \cb1 \strokec4 \
\cb3     \cf6 \strokec6 '#332288'\cf0 \strokec4 ,  \cf5 \strokec5 # Indigo\cf0 \cb1 \strokec4 \
\cb3     \cf6 \strokec6 '#AA7700'\cf0 \strokec4 ,  \cf5 \strokec5 # Dark Gold\cf0 \cb1 \strokec4 \
\cb3     \cf6 \strokec6 '#555555'\cf0 \strokec4 ,  \cf5 \strokec5 # Dark Gray\cf0 \cb1 \strokec4 \
\cb3     \cf6 \strokec6 '#CC79A7'\cf0 \strokec4 ,  \cf5 \strokec5 # Violet\cf0 \cb1 \strokec4 \
\cb3 ]\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Assign colors to models\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 for\cf0 \strokec4  i, model \cf7 \strokec7 in\cf0 \strokec4  \cf10 \strokec10 enumerate\cf0 \strokec4 (unlearning_models):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     model[\cf6 \strokec6 'color'\cf0 \strokec4 ] = colors[i % \cf10 \strokec10 len\cf0 \strokec4 (colors)]\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Define task styles\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 task_styles = \{\cb1 \
\cb3     \cf6 \strokec6 'wmdp_bio'\cf0 \strokec4 : \{\cf6 \strokec6 'marker'\cf0 \strokec4 : \cf6 \strokec6 's'\cf0 \strokec4 , \cf6 \strokec6 'label'\cf0 \strokec4 : \cf6 \strokec6 'Base prompt'\cf0 \strokec4 , \cf6 \strokec6 'size'\cf0 \strokec4 : \cf8 \strokec8 150\cf0 \strokec4 , \cf6 \strokec6 'highlight'\cf0 \strokec4 : \cf7 \strokec7 False\cf0 \strokec4 \},\cb1 \
\cb3     \cf6 \strokec6 'tinyMMLU'\cf0 \strokec4 : \{\cf6 \strokec6 'marker'\cf0 \strokec4 : \cf6 \strokec6 '*'\cf0 \strokec4 , \cf6 \strokec6 'label'\cf0 \strokec4 : \cf6 \strokec6 'tinyMMLU'\cf0 \strokec4 , \cf6 \strokec6 'size'\cf0 \strokec4 : \cf8 \strokec8 200\cf0 \strokec4 , \cf6 \strokec6 'highlight'\cf0 \strokec4 : \cf7 \strokec7 False\cf0 \strokec4 \},\cb1 \
\cb3     \cf6 \strokec6 'wmdp_bio_rephrased_english_filler'\cf0 \strokec4 : \{\cf6 \strokec6 'marker'\cf0 \strokec4 : \cf6 \strokec6 'o'\cf0 \strokec4 , \cf6 \strokec6 'label'\cf0 \strokec4 : \cf6 \strokec6 'Filler text'\cf0 \strokec4 , \cf6 \strokec6 'size'\cf0 \strokec4 : \cf8 \strokec8 150\cf0 \strokec4 , \cf6 \strokec6 'highlight'\cf0 \strokec4 : \cf7 \strokec7 False\cf0 \strokec4 \},\cb1 \
\cb3     \cf6 \strokec6 'wmdp_bio_rephrased_hindi_filler'\cf0 \strokec4 : \{\cf6 \strokec6 'marker'\cf0 \strokec4 : \cf6 \strokec6 'o'\cf0 \strokec4 , \cf6 \strokec6 'label'\cf0 \strokec4 : \cf6 \strokec6 'Filler text'\cf0 \strokec4 , \cf6 \strokec6 'size'\cf0 \strokec4 : \cf8 \strokec8 150\cf0 \strokec4 , \cf6 \strokec6 'highlight'\cf0 \strokec4 : \cf7 \strokec7 False\cf0 \strokec4 \},\cb1 \
\cb3     \cf6 \strokec6 'wmdp_bio_rephrased_latin_filler'\cf0 \strokec4 : \{\cf6 \strokec6 'marker'\cf0 \strokec4 : \cf6 \strokec6 'o'\cf0 \strokec4 , \cf6 \strokec6 'label'\cf0 \strokec4 : \cf6 \strokec6 'Filler text'\cf0 \strokec4 , \cf6 \strokec6 'size'\cf0 \strokec4 : \cf8 \strokec8 150\cf0 \strokec4 , \cf6 \strokec6 'highlight'\cf0 \strokec4 : \cf7 \strokec7 False\cf0 \strokec4 \},\cb1 \
\cb3     \cf6 \strokec6 'wmdp_bio_rephrased_conversation'\cf0 \strokec4 : \{\cf6 \strokec6 'marker'\cf0 \strokec4 : \cf6 \strokec6 '^'\cf0 \strokec4 , \cf6 \strokec6 'label'\cf0 \strokec4 : \cf6 \strokec6 'Rephrased as conversation'\cf0 \strokec4 , \cf6 \strokec6 'size'\cf0 \strokec4 : \cf8 \strokec8 150\cf0 \strokec4 , \cf6 \strokec6 'highlight'\cf0 \strokec4 : \cf7 \strokec7 False\cf0 \strokec4 \},\cb1 \
\cb3     \cf6 \strokec6 'wmdp_bio_rephrased_poem'\cf0 \strokec4 : \{\cf6 \strokec6 'marker'\cf0 \strokec4 : \cf6 \strokec6 'v'\cf0 \strokec4 , \cf6 \strokec6 'label'\cf0 \strokec4 : \cf6 \strokec6 'Rephrased as poem'\cf0 \strokec4 , \cf6 \strokec6 'size'\cf0 \strokec4 : \cf8 \strokec8 150\cf0 \strokec4 , \cf6 \strokec6 'highlight'\cf0 \strokec4 : \cf7 \strokec7 False\cf0 \strokec4 \},\cb1 \
\cb3     \cf6 \strokec6 'wmdp_bio_rephrased_replace_with_variables'\cf0 \strokec4 : \{\cf6 \strokec6 'marker'\cf0 \strokec4 : \cf6 \strokec6 'P'\cf0 \strokec4 , \cf6 \strokec6 'label'\cf0 \strokec4 : \cf6 \strokec6 'Replaced with variables'\cf0 \strokec4 , \cf6 \strokec6 'size'\cf0 \strokec4 : \cf8 \strokec8 150\cf0 \strokec4 , \cf6 \strokec6 'highlight'\cf0 \strokec4 : \cf7 \strokec7 False\cf0 \strokec4 \},\cb1 \
\cb3     \cf6 \strokec6 'wmdp_bio_rephrased_technical_terms_removed_1'\cf0 \strokec4 : \{\cf6 \strokec6 'marker'\cf0 \strokec4 : \cf6 \strokec6 'X'\cf0 \strokec4 , \cf6 \strokec6 'label'\cf0 \strokec4 : \cf6 \strokec6 'Technical terms removed'\cf0 \strokec4 , \cf6 \strokec6 'size'\cf0 \strokec4 : \cf8 \strokec8 150\cf0 \strokec4 , \cf6 \strokec6 'highlight'\cf0 \strokec4 : \cf7 \strokec7 False\cf0 \strokec4 \},\cb1 \
\cb3     \cf6 \strokec6 'wmdp_bio_rephrased_translated_farsi'\cf0 \strokec4 : \{\cf6 \strokec6 'marker'\cf0 \strokec4 : \cf6 \strokec6 'd'\cf0 \strokec4 , \cf6 \strokec6 'label'\cf0 \strokec4 : \cf6 \strokec6 'Translated'\cf0 \strokec4 , \cf6 \strokec6 'size'\cf0 \strokec4 : \cf8 \strokec8 150\cf0 \strokec4 , \cf6 \strokec6 'highlight'\cf0 \strokec4 : \cf7 \strokec7 False\cf0 \strokec4 \},\cb1 \
\cb3     \cf6 \strokec6 'wmdp_bio_rephrased_translated_german'\cf0 \strokec4 : \{\cf6 \strokec6 'marker'\cf0 \strokec4 : \cf6 \strokec6 'd'\cf0 \strokec4 , \cf6 \strokec6 'label'\cf0 \strokec4 : \cf6 \strokec6 'Translated'\cf0 \strokec4 , \cf6 \strokec6 'size'\cf0 \strokec4 : \cf8 \strokec8 150\cf0 \strokec4 , \cf6 \strokec6 'highlight'\cf0 \strokec4 : \cf7 \strokec7 False\cf0 \strokec4 \},\cb1 \
\cb3     \cf6 \strokec6 'wmdp_bio_rephrased_translated_korean'\cf0 \strokec4 : \{\cf6 \strokec6 'marker'\cf0 \strokec4 : \cf6 \strokec6 'd'\cf0 \strokec4 , \cf6 \strokec6 'label'\cf0 \strokec4 : \cf6 \strokec6 'Translated'\cf0 \strokec4 , \cf6 \strokec6 'size'\cf0 \strokec4 : \cf8 \strokec8 150\cf0 \strokec4 , \cf6 \strokec6 'highlight'\cf0 \strokec4 : \cf7 \strokec7 False\cf0 \strokec4 \},\cb1 \
\cb3 \}\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 for\cf0 \strokec4  style \cf7 \strokec7 in\cf0 \strokec4  task_styles.values():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     style[\cf6 \strokec6 'size'\cf0 \strokec4 ] = style[\cf6 \strokec6 'size'\cf0 \strokec4 ] / \cf8 \strokec8 3\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Define filled tasks\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 filled_tasks = \{\cb1 \
\cb3     \cf6 \strokec6 'wmdp_bio'\cf0 \strokec4 ,\cb1 \
\cb3     \cf6 \strokec6 'tinyMMLU'\cf0 \strokec4 ,\cb1 \
\cb3 \}\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Create figure with space for stacked legends and plot\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # fig = plt.figure(figsize=(5.4, 6))\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # fig = plt.figure(figsize=(5.4, 5.4))\cf0 \cb1 \strokec4 \
\
\cf5 \cb3 \strokec5 # Create a gridspec layout with space for legends above\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # gs = fig.add_gridspec(3, 1, height_ratios=[1, 1, 6])\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # task_legend_ax = fig.add_subplot(gs[0])\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # method_legend_ax = fig.add_subplot(gs[1])\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # ax = fig.add_subplot(gs[2])\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # gs = fig.add_gridspec(2, 1, height_ratios=[1, 4])\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # task_legend_ax = fig.add_subplot(gs[0])\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 ax = fig.add_subplot(gs[\cf8 \strokec8 1\cf0 \strokec4 ,\cf8 \strokec8 1\cf0 \strokec4 ])\cb1 \
\cb3 method_legend_ax = fig.add_subplot(gs[\cf8 \strokec8 1\cf0 \strokec4 ,\cf8 \strokec8 1\cf0 \strokec4 ])\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Hide the legend axes frames\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # task_legend_ax.axis('off')\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 method_legend_ax.axis(\cf6 \strokec6 'off'\cf0 \strokec4 )\cb1 \
\cb3 plt.subplots_adjust(hspace=\cf8 \strokec8 0.03\cf0 \strokec4 )  \cf5 \strokec5 # tighten vertical spacing\cf0 \cb1 \strokec4 \
\
\cb3 adjustment_factor = \cf8 \strokec8 0.25\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Plot points\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 for\cf0 \strokec4  model \cf7 \strokec7 in\cf0 \strokec4  unlearning_models:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     model_data = df[df[\cf6 \strokec6 'model'\cf0 \strokec4 ] == model[\cf6 \strokec6 'model'\cf0 \strokec4 ]]\cb1 \
\cb3     \cb1 \
\cb3     \cf2 \strokec2 for\cf0 \strokec4  _, model_row \cf7 \strokec7 in\cf0 \strokec4  model_data.iterrows():\cb1 \
\cb3         task = model_row[\cf6 \strokec6 'task'\cf0 \strokec4 ]\cb1 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  task \cf7 \strokec7 not\cf0 \strokec4  \cf7 \strokec7 in\cf0 \strokec4  task_styles:\cb1 \
\cb3             \cf2 \strokec2 continue\cf0 \cb1 \strokec4 \
\cb3             \cb1 \
\cb3         \cf5 \strokec5 # Find corresponding base model accuracy for this task\cf0 \cb1 \strokec4 \
\cb3         base_row = base_model_data[base_model_data[\cf6 \strokec6 'task'\cf0 \strokec4 ] == task]\cb1 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  \cf10 \strokec10 len\cf0 \strokec4 (base_row) == \cf8 \strokec8 0\cf0 \strokec4 :\cb1 \
\cb3             \cf2 \strokec2 continue\cf0 \cb1 \strokec4 \
\cb3             \cb1 \
\cb3         base_accuracy = base_row[\cf6 \strokec6 'accuracy'\cf0 \strokec4 ].values[\cf8 \strokec8 0\cf0 \strokec4 ] - adjustment_factor\cb1 \
\cb3         model_accuracy = model_row[\cf6 \strokec6 'accuracy'\cf0 \strokec4 ] - adjustment_factor\cb1 \
\cb3         \cb1 \
\cb3         \cf5 \strokec5 # Skip if adjusted accuracy is negative\cf0 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  base_accuracy <= \cf8 \strokec8 0\cf0 \strokec4  \cf7 \strokec7 or\cf0 \strokec4  model_accuracy <= \cf8 \strokec8 0\cf0 \strokec4 :\cb1 \
\cb3             \cf2 \strokec2 continue\cf0 \cb1 \strokec4 \
\cb3             \cb1 \
\cb3         style = task_styles[task]\cb1 \
\cb3         is_filled = task \cf7 \strokec7 in\cf0 \strokec4  filled_tasks\cb1 \
\cb3         is_highlight = style.get(\cf6 \strokec6 'highlight'\cf0 \strokec4 , \cf7 \strokec7 False\cf0 \strokec4 )\cb1 \
\cb3         \cb1 \
\cb3         facecolor = model[\cf6 \strokec6 'color'\cf0 \strokec4 ] \cf2 \strokec2 if\cf0 \strokec4  is_filled \cf2 \strokec2 else\cf0 \strokec4  \cf6 \strokec6 'none'\cf0 \cb1 \strokec4 \
\cb3         edgecolor = \cf6 \strokec6 'black'\cf0 \strokec4  \cf2 \strokec2 if\cf0 \strokec4  is_highlight \cf2 \strokec2 else\cf0 \strokec4  model[\cf6 \strokec6 'color'\cf0 \strokec4 ]\cb1 \
\cb3         linewidth = \cf8 \strokec8 1\cf0 \cb1 \strokec4 \
\cb3         \cb1 \
\cb3         \cf5 \strokec5 # Add scatter point\cf0 \cb1 \strokec4 \
\cb3         ax.scatter(\cb1 \
\cb3             base_accuracy,\cb1 \
\cb3             model_accuracy,\cb1 \
\cb3             facecolor=facecolor,\cb1 \
\cb3             edgecolor=edgecolor,\cb1 \
\cb3             marker=style[\cf6 \strokec6 'marker'\cf0 \strokec4 ],\cb1 \
\cb3             s=style[\cf6 \strokec6 'size'\cf0 \strokec4 ],\cb1 \
\cb3             linewidth=linewidth,\cb1 \
\cb3             alpha=\cf8 \strokec8 0.9\cf0 \strokec4 ,\cb1 \
\cb3             zorder=\cf8 \strokec8 5\cf0 \strokec4  \cf2 \strokec2 if\cf0 \strokec4  is_highlight \cf2 \strokec2 else\cf0 \strokec4  \cf8 \strokec8 4\cf0 \cb1 \strokec4 \
\cb3         )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Add diagonal reference line\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 ax.plot([\cf8 \strokec8 -.01\cf0 \strokec4 , \cf8 \strokec8 1\cf0 \strokec4 ], [\cf8 \strokec8 -.01\cf0 \strokec4 , \cf8 \strokec8 1\cf0 \strokec4 ], \cf6 \strokec6 'k--'\cf0 \strokec4 , alpha=\cf8 \strokec8 0.3\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Set labels and title\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 ax.set_xlabel(\cf6 \strokec6 'Base Model (Llama3-8B-Instruct) Accuracy (Adjusted)'\cf0 \strokec4 )\cb1 \
\cb3 ax.set_ylabel(\cf6 \strokec6 'Unlearned Model Accuracy (Adjusted)'\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Set axis limits to 0.75 for both axes\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 ax.set_xlim(\cf8 \strokec8 -.01\cf0 \strokec4 , \cf8 \strokec8 0.5\cf0 \strokec4 )\cb1 \
\cb3 ax.set_ylim(\cf8 \strokec8 -.01\cf0 \strokec4 , \cf8 \strokec8 0.5\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Add grid\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 ax.grid(\cf7 \strokec7 True\cf0 \strokec4 , linestyle=\cf6 \strokec6 '--'\cf0 \strokec4 , alpha=\cf8 \strokec8 0.3\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Create model legend\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 model_legend_handles = [\cb1 \
\cb3     Line2D([\cf8 \strokec8 0\cf0 \strokec4 ], [\cf8 \strokec8 0\cf0 \strokec4 ], marker=\cf6 \strokec6 'o'\cf0 \strokec4 , color=model[\cf6 \strokec6 'color'\cf0 \strokec4 ], label=model[\cf6 \strokec6 'name'\cf0 \strokec4 ],\cb1 \
\cb3            linestyle=\cf6 \strokec6 ''\cf0 \strokec4 , markersize=\cf8 \strokec8 8\cf0 \strokec4 ) \cf2 \strokec2 for\cf0 \strokec4  model \cf7 \strokec7 in\cf0 \strokec4  unlearning_models\cb1 \
\cb3 ]\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # # Create task legend with priority for tinyMMLU\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # task_legend_handles = []\cf0 \cb1 \strokec4 \
\
\cf5 \cb3 \strokec5 # # First add tinyMMLU to legend\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # tinyMMLU_style = task_styles['tinyMMLU']\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # task_legend_handles.append(\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #     Line2D(\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #         [0], [0],\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #         marker=tinyMMLU_style['marker'],\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #         markerfacecolor='#999999' if 'tinyMMLU' in filled_tasks else 'none',\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #         markeredgecolor='black' if tinyMMLU_style.get('highlight', False) else '#999999',\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #         markeredgewidth=1.5,\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #         linestyle='',\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #         markersize=10,\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #         label=tinyMMLU_style['label']\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #     )\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # )\cf0 \cb1 \strokec4 \
\
\cf5 \cb3 \strokec5 # # Add all other task styles to legend\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # seen_labels = \{tinyMMLU_style['label']\}  # Initialize with tinyMMLU already added\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # for key, style in task_styles.items():\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #     if key == 'tinyMMLU':  # Skip tinyMMLU as it's already added\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #         continue\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3         \cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 #     label = style['label']\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #     if label not in seen_labels:\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #         seen_labels.add(label)\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #         is_highlight = style.get('highlight', False)\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3         \cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 #         # Use proper styling for legend items\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #         facecolor = 'none'  # Most markers are not filled\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #         if key in filled_tasks:\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #             facecolor = '#999999'  # Use gray for filled markers in legend\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3         \cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 #         edgecolor = 'black' if is_highlight else '#999999'\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #         linewidth = 1.5\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3         \cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 #         task_legend_handles.append(\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #             Line2D(\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #                 [0], [0],\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #                 marker=style['marker'],\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #                 markerfacecolor=facecolor,\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #                 markeredgecolor=edgecolor,\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #                 markeredgewidth=linewidth,\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #                 linestyle='',\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #                 markersize=10,\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #                 label=label\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #             )\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #         )\cf0 \cb1 \strokec4 \
\
\cf5 \cb3 \strokec5 # # Add legends with Tasks on top and Unlearning Methods below\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # task_legend = task_legend_ax.legend(\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #     handles=task_legend_handles,\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #     title='Tasks',\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #     loc='lower right',\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #     ncol=2,\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #     frameon=True,\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #     columnspacing=0.5,      # Reduce column gap\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #     handletextpad=0.3,      # Reduce gap between marker and label\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #     handlelength=1.2,       # Shorter marker length\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 #     borderaxespad=0.2       # Reduce padding to axes\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # )\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 method_legend = method_legend_ax.legend(\cb1 \
\cb3     handles=model_legend_handles,\cb1 \
\cb3     title=\cf6 \strokec6 'Unlearning Methods'\cf0 \strokec4 ,\cb1 \
\cb3     loc=\cf6 \strokec6 'upper left'\cf0 \strokec4 ,\cb1 \
\cb3     ncol=\cf8 \strokec8 2\cf0 \strokec4 ,\cb1 \
\cb3     frameon=\cf7 \strokec7 True\cf0 \strokec4 ,\cb1 \
\cb3     columnspacing=\cf8 \strokec8 0.5\cf0 \strokec4 ,\cb1 \
\cb3     handletextpad=\cf8 \strokec8 0.3\cf0 \strokec4 ,\cb1 \
\cb3     handlelength=\cf8 \strokec8 1.2\cf0 \strokec4 ,\cb1 \
\cb3     borderaxespad=\cf8 \strokec8 0.2\cf0 \strokec4 ,\cb1 \
\cb3     \cf5 \strokec5 # bbox_to_anchor=(-.1, 0),  # x = 0 (left), y > 1 = above plot\cf0 \cb1 \strokec4 \
\cb3 )\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Save figure as PDF\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # plt.tight_layout()\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 plt.savefig(\cf6 \strokec6 'horizontal.pdf'\cf0 \strokec4 , bbox_inches=\cf6 \strokec6 'tight'\cf0 \strokec4 , dpi=\cf8 \strokec8 300\cf0 \strokec4 )\cb1 \
\cb3 plt.close()\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf10 \cb3 \strokec10 print\cf0 \strokec4 (\cf6 \strokec6 'Visualization saved'\cf0 \strokec4 )\cb1 \
}