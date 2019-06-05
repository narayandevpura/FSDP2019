# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:52:47 2019

@author: Narayan Devpura
"""

"""
Code Challenge:
dataset: BreadBasket_DMS.csv

Q1. In this code challenge, you are given a dataset which has data and time wise transaction on a bakery retail store.
1. Draw the pie chart of top 15 selling items.
2. Find the associations of items where min support should be 0.0025, min_confidence=0.2, min_lift=3.
3. Out of given results sets, show only names of the associated item from given result row wise.
"""

import pandas as pd
from material.apyori import apriori
import matplotlib.pyplot as plt

# read and check data
df = pd.read_csv('material/BreadBasket_DMS.csv')
df.isnull().any(axis = 0)
df["Item"].value_counts()

# taking indexes of NONE items
index = df.index[df['Item'] == "NONE"].tolist()

# drop all rows with NONE as Item
df.drop(index, axis =0, inplace =True)

# Draw the pie chart of top 15 selling items
x = df['Item'].value_counts().head(15)
name = x.index.tolist()
count = x.values.tolist()
plt.pie(count, labels = name, shadow = True, autopct = "%2.2f%%", startangle= 180, radius =2, explode = [0.2,0,0,0,0,0,0,0,0,0,0,0,0,0,0])


#  Find the associations of items where min support should be 0.0025, min_confidence=0.2, min_lift=3.
item = df.groupby('Transaction')['Item'].unique()
item_list = [x.tolist() for x in item]

# Training Apriori on the dataset

rules = apriori(item_list, min_support = 0.0025, min_confidence = 0.2, min_lift = 3)

# Visualising the results
results = list(rules)

for item in results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
