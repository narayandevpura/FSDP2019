# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:23:15 2019

@author: Narayan Devpura
"""

"""
Code Challenge: Simple Linear Regression

  Name: 
    Box Office Collection Prediction Tool
  Filename: 
    Bahubali2vsDangal.py
  Dataset:
    Bahubali2vsDangal.csv
  Problem Statement:
    It contains Data of Day wise collections of the movies Bahubali 2 and Dangal 
    (in crores) for the first 9 days.
    
    Now, you have to write a python code to predict which movie would collect 
    more on the 10th day.
  Hint:
    First Approach - Create two models, one for Bahubali and another for Dangal
    Second Approach - Create one model with two labels
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read data
bd = pd.read_csv('material/Bahubali2_vs_Dangal.csv')

# Plotting data for bahubali2 movie
bd.plot(x='Days', y='Bahubali_2_Collections_Per_day', style='o')  
plt.title('Box Office Collection')  
plt.xlabel('Days')  
plt.ylabel('Money Collected')  
plt.show()

# Plotting data for dangal movie
bd.plot(x='Days', y='Dangal_collections_Per_day', style='o')  
plt.title('Box Office Collection')  
plt.xlabel('Days')  
plt.ylabel('Money Collected')  
plt.show()

# features and labels
features = bd.iloc[:,0:1]
labels = bd.iloc[:,1:3]

# Applying LinearRegression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features,labels)

# prediction
day = 10
day = np.array(day).reshape(1,-1)
pred = regressor.predict(day)

print(pred)
print("Collection at Day 10 for Bahubali2 will be: ",pred[0][0])
print("Collection at Day 10 for Dangal will be: ",pred[0][1])