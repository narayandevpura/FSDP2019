# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:10:14 2019

@author: Narayan Devpura
"""

"""
(Create a program that fulfills the following specification.)

The iris data set consists of 50 samples from each of three species of Iris flower (Iris setosa, 
Iris virginica and Iris versicolor).



    Four features were measured from each sample: the length and the width of the sepals and petals,
    in centimetres (iris.data).
    Import the iris dataset already in sklearn module using the following command:\


from sklearn.datasets import load_iris
iris = load_iris()
iris=iris.data


Reduce dimension from 4-d to 2-d and perform clustering to distinguish the 3 species.
"""

# read data
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
irises = load_iris()
iris = pd.DataFrame(irises.data, columns = irises.feature_names)
iris['Target'] = irises.target
features = iris.iloc[:,:4].values

# Applying PCA
from sklearn.decomposition import PCA
pca = PCA(n_components= 2)
features = pca.fit_transform(features)
explained_variance = pca.explained_variance_ratio_

# Applying KMeans
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters= 3)
pred_cluster = kmeans.fit_predict(features)

# Visualising the clusters
#plt.scatter(features[:,0][y_kmeans == 0], features[:,1][y_kmeans == 0], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = '0')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = '1')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = '2')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('X Cordindates')
plt.ylabel('Y Cordinates')
plt.legend()
plt.show()
