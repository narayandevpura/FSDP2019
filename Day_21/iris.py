# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 15:45:58 2019

@author: Narayan Devpura
"""

"""
Q2. This famous classification dataset first time used in Fisher’s classic 1936 paper, 
The Use of Multiple Measurements in Taxonomic Problems. Iris dataset is having 4 features 
of iris flower and one target class.

The 4 features are

SepalLengthCm
SepalWidthCm
PetalLengthCm
PetalWidthCm
The target class

The flower species type is the target class and it having 3 types

Setosa
Versicolor
Virginica
The idea of implementing svm classifier in Python is to use the iris features to train 
an svm classifier and use the trained svm model to predict the Iris species type. To 
begin with let’s try to load the Iris dataset.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score

# loading dataset
dic = datasets.load_iris() 

# features and labels
X = pd.DataFrame(dic.data, columns = dic.feature_names).values
y = dic.target

# train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 101)

# Applying svm 
svc =SVC(kernel= 'linear', random_state= 101)
svc.fit(X_train, y_train)
y_predL = svc.predict(X_test)

# Confusion matrix
cL = confusion_matrix(y_test, y_predL)
score_L = round(accuracy_score(y_test, y_predL) * 100, 2)
print("Confusion matrix: ",cL)
print("Score: ", score_L)
