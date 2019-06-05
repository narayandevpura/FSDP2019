# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:52:40 2019

@author: Narayan Devpura
"""
"""
Q1. (Create a program that fulfills the following specification.)
tshirts.csv


T-Shirt Factory:

You own a clothing factory. You know how to make a T-shirt given the height and weight of a customer.

You want to standardize the production on three sizes: small, medium, and large. How would you figure out the actual size of these 3 types of shirt to better fit your customers?

Import the tshirts.csv file and perform Clustering on it to make sense out of the data as stated above.
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import DBSCAN

# Importing the dataset (Bivariate Data Set with 3 Clusters)
dataset = pd.read_csv('material/tshirts.csv')
features = dataset.iloc[:, [1, 2]].values

#Scatter all these data points on the matplotlib
plt.scatter(features[:,0], features[:,1])
plt.show()

# Compute DBSCAN
db = DBSCAN(eps=0.3, min_samples=10).fit(features)
#core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
#core_samples_mask[db.core_sample_indices_] = True
labels_pred = db.labels_






