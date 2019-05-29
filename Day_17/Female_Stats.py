# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:44:11 2019

@author: Narayan Devpura
"""

"""
Q. (Create a program that fulfills the following specification.)
Female_Stats.Csv

Female Stat Students

Import The Female_Stats.Csv File

The Data Are From N = 214 Females In Statistics Classes At The University Of 
California At Davi.

Column1 = Student’s Self-Reported Height,

Column2 = Student’s Guess At Her Mother’s Height, And

Column 3 = Student’s Guess At Her Father’s Height. All Heights Are In Inches.

Build A Predictive Model And Conclude If Both Predictors (Independent Variables) 
Are Significant For A Students’ Height Or Not

When Father’s Height Is Held Constant, The Average Student Height Increases By 
How Many Inches For Each One-Inch Increase In Mother’s Height.

When Mother’s Height Is Held Constant, The Average Student Height Increases By 
How Many Inches For Each One-Inch Increase In Father’s Height.

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fem = pd.read_csv("material/Female_Stats.Csv")

features = fem.iloc[:,1:].values
labels = fem.iloc[:,0].values


# Build A Predictive Model And Conclude If Both Predictors (Independent Variables) 
# Are Significant For A Students’ Height Or Not

import statsmodels.api as sm
features = sm.add_constant(features)

features_opt = features[:, [0, 1, 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
# regressor_OLS.summary()
print(regressor_OLS.pvalues)

print("Since all pvalues are less than 5% so all values are important.")
print("This shows that both fathers and mothers height affects students height.")


# When Father’s Height Is Held Constant, The Average Student Height Increases By 
# How Many Inches For Each One-Inch Increase In Mother’s Height.

# When Mother’s Height Is Held Constant, The Average Student Height Increases By 
# How Many Inches For Each One-Inch Increase In Father’s Height.


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features,labels)

pred = regressor.predict(features)

df = pd.DataFrame(pred, labels)

print(regressor.coef_)

print("When Father’s Height Is Held Constant, The Average Student Height Increases By: ", regressor.coef_[1])

print("When Mother’s Height Is Held Constant, The Average Student Height Increases By: ", regressor.coef_[0])
