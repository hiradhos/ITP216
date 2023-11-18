# Hirad Hosseini, hiradhos@usc.edu
# ITP 216, Fall 2023
# Section: 32081
# Lab 13
# Description:
# Describe what this program does in your own words such as:
'''
This program uses our newly learned concepts underlying pandas and matplotlib in order to make a simple visualization
of a Penguins dataset comparing flipper length distributions among 3 different species.
'''

import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

def get_freq_dict(series):
    freq_dict = {}
    if i in freq_dict:
        freq_dict[i] += 1
    else:
        freq_dict[i] = 1
    return freq_dict

def get_freq_dict_counter(series):
    return Counter(series)

df = pd.read_csv("penguins.csv")
df.dropna(inplace=True)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)
fig, ax = plt.subplots(1,1)
species_list = df["species"].unique()
df_grouped = df.groupby("species")
color_list = ["blue", "FF00FF", "green"]
marker_list = ["*", "D", "^"]
for index, species in enumerate(species_list):
    df_group = df_grouped.get_group(species)
    ax.hist(df_group["flipper_length_mm"], bins = 25, alpha = 0.5, label=species)
plt.legend()
ax.set(title = "Penguin flipper lengths", xlabel = "Flipper length (mm)", ylabel = "Frequency")
fig.tight_layout()
plt.grid()
plt.show()
