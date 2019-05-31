# -*- coding: utf-8 -*-
"""
Created on Fri May 31 15:44:37 2019

@author: Narayan Devpura
"""

"""
Code Challenges 02: (House Data)
This is kings house society data.
In particular, we will: 
• Use Linear Regression and see the results
• Use Lasso (L1) and see the resuls
• Use Ridge and see the score
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# read data
df = pd.read_csv("material/kc_house_data.csv")
df.isnull().any(axis = 0)

# Handling nan values
df['sqft_above'] = df['sqft_above'].fillna(np.mean(df['sqft_above']))

# changing date column
df['date'] = pd.to_numeric(df['date'].apply(lambda x: x[:4]))

# features and labels
X = df.drop(['price', 'id'], axis = 1).values
y = df['price'].values

# train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Scaling Data
s = StandardScaler()
X_train = s.fit_transform(X_train)
X_test = s.transform(X_test)

# Applying LinearRegression
LR = LinearRegression()
LR.fit(X_train, y_train)
y_predLR = LR.predict(X_test)
score_LR = LR.score(X_test, y_test)
print('Score of Linear Regression: ', score_LR * 100)

# Applying Lasso and Ridge
L = Lasso()
R = Ridge()

L.fit(X_train, y_train)
R.fit(X_train, y_train)

y_predL = L.predict(X_test)
y_predR = R.predict(X_test)

score_L = L.score(X_test, y_test)
score_R = R.score(X_test, y_test)

print("Score of Lasso:", score_L * 100)
print("Score of Ridge: ", score_R * 100)












