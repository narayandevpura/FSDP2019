# -*- coding: utf-8 -*-
"""
Created on Fri May 31 15:44:37 2019

@author: Narayan Devpura
"""

"""
Code Challenge 01: (Prostate Dataset)
Load the dataset from given link: 
pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat")

This is the Prostate Cancer dataset. Perform the train test split before you apply the model.

(a) Can we predict lpsa from the other variables?
(1) Train the unregularized model (linear regressor) and calculate the mean squared error.
(2) Apply a regularized model now - Ridge regression and lasso as well and check the mean squared error.

(b) Can we predict whether lpsa is high or low, from other variables?

"""

import pandas as pd
import numpy as np

# read data
df = pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat", sep= ' ')

# check data
df.info()
df.head()
df.isnull().any(axis = 0)

# features and labels
X = df.drop('lpsa', axis = 1).values
y = df['lpsa'].values

y_mean = np.mean(y) 

# train_test_split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .2, random_state = 0)

# Applying LinearRegression
from sklearn.linear_model import LinearRegression
LR = LinearRegression()
LR.fit(X_train, y_train)
y_predLR = LR.predict(X_test)

# Metrics Report
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import mean_squared_error as mse
print("Mean Absolute Error: ", mae(y_test, y_predLR))
print("Mean Squared Error: ", mse(y_test, y_predLR))
print("Root Mean Squared Error: ", np.sqrt(mse(y_test, y_predLR)))

# LinearRegression Model Checking
if np.sqrt(mse(y_test, y_predLR)) < (0.1 * y_mean):
    print("ALgo works properly")
else:
    print("Model needs some changes")
    
# Score 
score_train = round((LR.score(X_train, y_train) * 100),2)
score_test = round((LR.score(X_test, y_test) * 100), 2)
print("Score of Training Data: ",score_train)
print("Score of Testing Data: ", score_test)

# checking for overfitting and underfitting
if score_train > score_test:
    print("Overfitted model")
elif score_train < 70:
    print("Underfitting model")




####### Applying Lasso, Ridge, ElasticNet regression #######

from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet

L = Lasso()
R = Ridge()
EN = ElasticNet()

L.fit(X_train, y_train)
R.fit(X_train, y_train)
EN.fit(X_train, y_train)

y_predL = L.predict(X_test)
y_predR = R.predict(X_test)
y_predEN = EN.predict(X_test)

# Metrics Report
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import mean_squared_error as mse
print("Lasso Mean Absolute Error: ", mae(y_test, y_predL))
print("Lasso Mean Squared Error: ", mse(y_test, y_predL))
print("Lasso Root Mean Squared Error: ", np.sqrt(mse(y_test, y_predL)))

# Lasso Model Checking
if np.sqrt(mse(y_test, y_predL)) < (0.1 * y_mean):
    print("ALgo works properly")
else:
    print("Model needs some changes")

from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import mean_squared_error as mse
print("Ridge Mean Absolute Error: ", mae(y_test, y_predR))
print("Ridge Mean Squared Error: ", mse(y_test, y_predR))
print("Ridge Root Mean Squared Error: ", np.sqrt(mse(y_test, y_predR)))

# Ridge Model Checking
if np.sqrt(mse(y_test, y_predR)) < (0.1 * y_mean):
    print("ALgo works properly")
else:
    print("Model needs some changes")

from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import mean_squared_error as mse
print("ElasticNet Mean Absolute Error: ", mae(y_test, y_predEN))
print("ElasticNet Mean Squared Error: ", mse(y_test, y_predEN))
print("ElasticNet Root Mean Squared Error: ", np.sqrt(mse(y_test, y_predEN)))

# ElasticNet Model Checking
if np.sqrt(mse(y_test, y_predEN)) < (0.1 * y_mean):
    print("ALgo works properly")
else:
    print("Model needs some changes")
    
    
# Score
score_train_L = round((L.score(X_train, y_train) * 100),2)
score_test_L = round((L.score(X_test, y_test) * 100), 2)
print("Lasso Score of Training Data: ",score_train_L)
print("Lasso Score of Testing Data: ", score_test_L)

score_train_R = round((R.score(X_train, y_train) * 100),2)
score_test_R = round((R.score(X_test, y_test) * 100), 2)
print("Ridge Score of Training Data: ",score_train_R)
print("Ridge Score of Testing Data: ", score_test_R)

score_train_EN = round((EN.score(X_train, y_train) * 100),2)
score_test_EN = round((EN.score(X_test, y_test) * 100), 2)
print("ElasticNet Score of Training Data: ",score_train_EN)
print("ElasticNet Score of Testing Data: ", score_test_EN)


######## Converting Into High(1) Low(0) #########

df['lpsa'] = df['lpsa'].apply(lambda x: 1 if x >= y_mean else 0)

# labels now
y = df['lpsa'].values

# train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Applying KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier
KNN = KNeighborsClassifier()
KNN.fit(X_train, y_train)
y_predK = KNN.predict(X_test)

# Confusion and Classification Report
from sklearn.metrics import classification_report, confusion_matrix
cm = confusion_matrix(y_test, y_predK)
cr = classification_report(y_test, y_predK)

print("Classification Report: ", cr)



