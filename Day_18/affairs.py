# -*- coding: utf-8 -*-
"""
Created on Wed May 29 15:59:01 2019

@author: Narayan Devpura
"""

"""

Q1. (Create a program that fulfills the following specification.)
affairs.csv


Import the affairs.csv file.

It was derived from a survey of women in 1974 by Redbook magazine, in which married women were asked 
about their participation in extramarital affairs.

Description of Variables

The dataset contains 6366 observations of 10 variables:(modified and cleaned)

rate_marriage: woman's rating of her marriage (1 = very poor, 5 = very good)

age: women's age

yrs_married: number of years married

children: number of children

religious: women's rating of how religious she is (1 = not religious, 4 = strongly religious)

educ: level of education (9 = grade school, 12 = high school, 14 = some college, 16 = college graduate, 
17 = some graduate school, 20 = advanced degree)

occupation: women's occupation (1 = student, 2 = farming/semi-skilled/unskilled, 3 = "white collar", 
4 = teacher/nurse/writer/technician/skilled, 5 = managerial/business, 6 = professional with advanced 
degree)

occupation_husb: husband's occupation (same coding as above)

affair: outcome 0/1, where 1 means a woman had at least 1 affair.

    Now, perform Classification using logistic regression and check your model accuracy using confusion
    matrix and also through .score() function.

NOTE: Perform OneHotEncoding for occupation and occupation_husb, since they should be treated as 
categorical variables. Careful from dummy variable trap for both!!

    What percentage of total women actually had an affair?

(note that Increases in marriage rating and religiousness correspond to a decrease in the likelihood 
of having an affair.)

    Predict the probability of an affair for a random woman not present in the dataset. She's a 
    25-year-old teacher who graduated college, has been married for 3 years, has 1 child, rates 
    herself as strongly religious, rates her marriage as fair, and her husband is a farmer.

Optional

    Build an optimum model, observe all the coefficients.

"""
import numpy as np
import pandas as pd

af = pd.read_csv("material/affairs.csv")

# features and labels
X = af.iloc[:,:-1]
Y = af.iloc[:,-1]

# Performing dummy variables for two columns
X = pd.get_dummies(data = X, columns=['occupation', 'occupation_husb'], drop_first = True)

# train_test_split
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.33, random_state = 0)

# Applying LogisticRegression
from sklearn.linear_model import LogisticRegression
log = LogisticRegression()
log.fit(X_train, Y_train)
pred = log.predict(X_test)


# Confusing matrix
from sklearn.metrics import confusion_matrix
c = confusion_matrix(Y_test, pred)
print(c)
print("Accuracy of the model: ",log.score(X_test, Y_test))


# Prediction for new women
woman = [3,25,3,1,5,16,0,0,1,0,0,1,0,0,0,0]
woman = np.array(woman).reshape(1,-1)
afon = log.predict(woman)
prob =log.predict_proba(woman)
print("Affair or not:", afon[0])
print("Probability of not affair: ",prob[0][0])

# What percentage of total women actually had an affair?
wom_with_aff = af['affair'][af['affair'] == 1].count() 
perc = (wom_with_aff / af['affair'].count()) * 100
print("percentage of total women actually had an affair: ", perc)




""" Alternate Way

import numpy as np
import pandas as pd

af = pd.read_csv("material/affairs.csv")

features = af.iloc[:,:-1]
labels = af.iloc[:,-1]

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(features, labels, test_size = 0.33, random_state = 0)

from sklearn.preprocessing import OneHotEncoder
OHE = OneHotEncoder(categorical_features= [-2,-1])
X_train = OHE.fit_transform(X_train).toarray()
X_train = np.delete(X_train, [0,11], axis = 1)

X_test = OHE.transform(X_test).toarray()
X_test = np.delete(X_test, [0,11], axis = 1)

from sklearn.linear_model import LogisticRegression
regressor = LogisticRegression()
regressor.fit(X_train,Y_train)
labels_pred = regressor.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, labels_pred)

#accuracy of our model
regressor.score(X_test, Y_test)
women_data = [3,25,3,1,5,16,4,2]
x = np.array(women_data).reshape(1,-1)
y = OHE.transform(x).toarray()
y = np.delete(y, [0,6], axis=1)

#calculate percentage of women who had an affair
women_aff = af[af["affair"]==1]['affair'].count()

percentage = women_aff/af["affair"].count()*100

print("Total women who had an affair:",percentage)
"""