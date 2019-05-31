# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:33:46 2019

@author: Narayan Devpura
"""

"""
(Create a program that fulfills the following specification.)
Auto_mpg.txt

Here is the dataset about cars. The data concerns city-cycle fuel consumption in miles per gallon (MPG).

    Import the dataset Auto_mpg.txt
    Give the column names as "mpg", "cylinders", "displacement","horsepower","weight","acceleration", 
    "model year", "origin", "car name" respectively
    
    Display the Car Name with highest miles per gallon value
    
    Build the Decision Tree and Random Forest models and find out which of the two is more accurate in
    predicting the MPG value
    
    Find out the MPG value of a 80's model car of origin 3, weighing 2630 kgs with 6 cylinders, having 
    acceleration around 22.2 m/s due to it's 100 horsepower engine giving it a displacement of about 215.
    (Give the prediction from both the models)

"""

import pandas as pd
import numpy as np

df = pd.read_csv('material/Auto_mpg.txt', sep = '\s+', header = None)
df.columns = ["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name"]

# check for null values
df.isnull().any(axis = 0)

# check unique values of 'horsepower'
df['horsepower'].unique()
df['car name'].value_counts()

# replacing '?' with mode
df['horsepower'] = df['horsepower'].replace('?', df['horsepower'].mode()[0])

# changing dtype to numeric
df['horsepower'] = pd.to_numeric(df['horsepower'])

# Display the Car Name with highest miles per gallon value
high_mpg_car = df['car name'][df['mpg'] == df['mpg'].max()].values[0]
print('Car Name with highest miles per gallon value: ', high_mpg_car)

# features and labels
X = df.drop(['mpg', 'car name'], axis = 1)
y = df['mpg']

# performing train_test_split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# performing Standard Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# performing Decision tree Model
from sklearn.tree import DecisionTreeRegressor
DTR = DecisionTreeRegressor(random_state = 0)
DTR.fit(X_train, y_train)
y_predD = DTR.predict(X_test)
score_D = DTR.score(X_test, y_test) * 100
print("Score of DTR Model: ", score_D)

# performing Random forest Model
from sklearn.ensemble import RandomForestRegressor
RFR = RandomForestRegressor(n_estimators= 25, random_state= 0)
RFR.fit(X_test, y_test)
y_predR = RFR.predict(X_test)
score_R = RFR.score(X_test, y_test) * 100
print("Score of RFR Model: ", score_R)

if score_R > score_D:
    print("Random Forest Model pedicted more accurate mpg with Accuracy: ", score_R)
else:
    print("Decision Tree Model pedicted more accurate mpg with Accuracy: ", score_D)

# Find out the MPG value of a 80's model car of origin 3, weighing 2630 kgs with 6 cylinders, having 
# acceleration around 22.2 m/s due to it's 100 horsepower engine giving it a displacement of about 215.
new_X = [6,215,100,2630,22.2,80,3]
new_X = np.array(new_X).reshape(1,-1)
new_X = sc.transform(new_X)
new_yD = DTR.predict(new_X)
new_yR = RFR.predict(new_X)

print("Predicted value for new feature by DTR: ", new_yD[0])
print("Predicted value for new feature by RFR: ", new_yR[0])

if new_yR[0] > new_yD[0]:
    print("Random Forest Model pedicted more accurate mpg: ", new_yR[0])
else:
    print("Decision Tree Model pedicted more accurate mpg: ", new_yD[0])






