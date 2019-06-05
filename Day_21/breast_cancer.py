# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 15:44:46 2019

@author: Narayan Devpura
"""

"""
1. (Create a program that fulfills the following specification.)

Program Specification:

Import breast_cancer.csv file.

This breast cancer database was obtained from the University of Wisconsin

Hospitals, Madison from Dr. William H. Wolberg.

Attribute Information: (class attribute has been moved to last column)

Sample Code Number(id number)                     ----> represented by column A.

Clump Thickness (1 – 10)                                     ----> represented by column B.
Uniformity of Cell Size(1 - 10)                             ----> represented by column C.
Uniformity of Cell Shape (1 - 10)                        ----> represented by column D.
Marginal Adhesion (1 - 10)                                  ----> represented by column E.
Single Epithelial Cell Size (1 - 10)                        ----> represented by column F.
Bare Nuclei (1 - 10)                                               ----> represented by column G.
Bland Chromatin (1 - 10)                                     ----> represented by column H.
Normal Nucleoli (1 - 10)                                      ----> represented by column I.
Mitoses (1 - 10)                                                     ----> represented by column J.
Class: (2 for Benign and 4 for Malignant)         ----> represented by column K. 
A Benign tumor is not a cancerous tumor and Malignant tumor is a cancerous tumor.

Impute the missing values with the most frequent values.

Perform Classification on the given data-set to predict if the tumor is cancerous or not.
Check the accuracy of the model.

Predict whether a women has Benign tumor or Malignant tumor, if her Clump thickness is around 6, uniformity
of cell size is 2, Uniformity of Cell Shape is 5, Marginal Adhesion is 3, Bland Chromatin is 9, Mitoses is
4, Bare Nuclei is 7, Normal Nuclei is 2 and Single Epithelial Cell Size is 2
(you can neglect the id number column as it doesn't seem  a predictor column)  [6,2,5,3,2,7,9,2,4]
"""

import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
import numpy as np
# read data
df = pd.read_csv('material/breast_cancer.csv')

# check data
df.info()
df.isnull().any(axis = 0)

# handling nan values
df['G'] = df['G'].fillna(df['G'].mode()[0])

# features and labels
X = df.drop(['A','K'], axis = 1).values
y = df['K'].values

# train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 101)

# Applying classification algo SVM - linear
svc = SVC(kernel = 'linear', random_state= 101)
svc.fit(X_train, y_train)
y_predSl = svc.predict(X_test)

# Confusion matrix
cSl = confusion_matrix(y_test, y_predSl)
score_Sl = round(accuracy_score(y_test, y_predSl) * 100, 2)
print("Confusion matrix: ",cSl)
print("Score: ", score_Sl)

woman = np.array([6,2,5,3,2,7,9,2,4]).reshape(1,-1)
woman_pred = svc.predict(woman)

if woman_pred[0] == 4:
    print("Woman has a Malignant tumor")
else:
    print("Woman has a Benign tumor")
