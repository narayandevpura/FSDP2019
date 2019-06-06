# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:10:55 2019

@author: Narayan Devpura
"""

"""
Code Challenge -
Data: "data.csv"

This data is provided by The Metropolitan Museum of Art Open Access
1. Visualize the various countries from where the artworks are coming.
2. Visualize the top 2 classification for the artworks
3. Visualize the artist interested in the artworks
4. Visualize the top 2 culture for the artworks
"""

import pandas as pd
import matplotlib.pyplot as plt

# read data
df = pd.read_csv('material/data.csv')

#Visualize the various countries from where the artworks are coming.
country = df['Country'].value_counts()
labels = country.index.tolist()
values =  country.values
percent = 100.0 * values / values.sum()
labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(labels, percent)]
pie = plt.pie(values, shadow=True)
plt.legend(pie[0], labels, loc="upper corner", bbox_to_anchor = (1,1))

#Visualize the top 2 classification for the artworks
top_2_classification = df['Classification'].value_counts().head(2)
plt.bar(x = top_2_classification.index.tolist(), height = top_2_classification.values.tolist())

# Visualize the artist interested in the artworks


# Visualize the top 2 culture for the artworks
top_2_culture = df['Culture'].value_counts().head(2)
plt.bar(top_2_culture.index.tolist(), height = top_2_culture.values.tolist())
