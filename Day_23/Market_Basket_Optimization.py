# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:52:47 2019

@author: Narayan Devpura
"""

"""
Code Challenge:
Datset: Market_Basket_Optimization.csv
Q2. In today's demo sesssion, we did not handle the null values before fitting the data to model, remove the null values from each row and perform the associations once again.
Also draw the bar chart of top 10 edibles.

"""
import pandas as pd
from material.apyori import apriori
import matplotlib.pyplot as plt

# Data Preprocessing
df = pd.read_csv('material/Market_Basket_Optimisation.csv', header = None)

# Importing the libraries



transactions = []

for i in range(0, 7501):
    #transactions.append(str(df.iloc[i,:].values)) #need to check this one
    transactions.append([str(df.values[i,j]) for j in range(0, 20) if str(df.values[i,j]) != "nan"])

# Training Apriori on the df

rules = apriori(transactions, min_support = 0.003, min_confidence = 0.25, min_lift = 4)

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

flat_list = []
for sublist in transactions:
    for item in sublist:
        flat_list.append(item)

top_10_df = pd.DataFrame(flat_list)
top_10 = top_10_df[0].value_counts().head(10)

names = top_10.index.tolist()    
count = top_10.values.tolist()

plt.bar(names, count, align = 'center', alpha = 0.5)
plt.xticks(rotation =90)
plt.show()
