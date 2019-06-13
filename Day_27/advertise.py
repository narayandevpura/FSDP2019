#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 14:44:46 2019

@author: narayan
"""

"""
(Click Here To Download Training data File): 
http://openedx.forsk.in/c4x/Forsk_Labs/ST101/asset/Advertisement_training_data.json

(Click Here To Download Test data File):
http://openedx.forsk.in/c4x/Forsk_Labs/ST101/asset/Advertisement_test_data.json


This is the data for local classified advertisements. It has 9 prominent sections: jobs, resumes, gigs,
personals, housing, community, services, for-sale and discussion forums. Each of these sections is divided 
into subsections called categories. For example, the services section has the following categories under it:
beauty, automotive, computer, household, etc.

For a set of sixteen different cities (such as newyork, Mumbai, etc.), we provide to you data from four sections

        for-sale
        housing
        community
        services

and we have selected a total of 16 categories from the above sections.

        activities
        appliances
        artists
        automotive
        cell-phones
        childcare
        general
        household-services
        housing
        photography
        real-estate
        shared
        temporary
        therapeutic
        video-games
        wanted-housing

Each category belongs to only 1 section.

About Data:

        city (string) : The city for which this Craigslist post was made.
        section (string) : for-sale/housing/etc.
        heading (string) : The heading of the post.

each of the fields have no more than 1000 characters. The input for the program 
has all the fields but category which you have to predict as the answer.

A total of approximately 20,000 records have been provided to you, proportionally 
represented across these sections, categories and cities. The format of training 
data is the same as input format but with an additional field "category", the category 
in which the post was made.

Task:

    Given the city, section and heading of an advertisement, can you predict the 
    category under which it was posted?
    Also Show top 5 categories which has highest number of posts
"""

import pandas as pd
import requests
import numpy as np

url = 'http://openedx.forsk.in/c4x/Forsk_Labs/ST101/asset/Advertisement_training_data.json'
url2 = 'http://openedx.forsk.in/c4x/Forsk_Labs/ST101/asset/Advertisement_test_data.json'

data = requests.get(url)
test = requests.get(url2)
data = data.text
test = test.text

df = pd.read_json(data, lines = True)
df2 = pd.read_json(test, lines = True)

X= df.drop(['category','heading'], axis= 1).values
X_test = df2.drop('heading', axis= 1).values

y= df['category'].values

from sklearn.preprocessing import LabelEncoder
LE = LabelEncoder()
LE2 = LabelEncoder()

X[:,0] = LE.fit_transform(X[:,0])
X[:,1] = LE2.fit_transform(X[:,1])
X_test[:,0] = LE.transform(X_test[:,0])
X_test[:,1] = LE2.transform(X_test[:,1])


from sklearn.preprocessing import OneHotEncoder
OHE = OneHotEncoder(categorical_features = [0,1])
X = OHE.fit_transform(X).toarray()
X_test = OHE.transform(X_test).toarray()

X = X[:,1:19]
X_test = X_test[:,1:19]

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

corpus = []
for i in range(0, 20217):
    review = re.sub('[^a-zA-Z]', ' ', df['heading'][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
    review = ' '.join(review)
    corpus.append(review)

corpus2 = []
for i in range(0, 15370):
    review = re.sub('[^a-zA-Z]', ' ', df2['heading'][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
    review = ' '.join(review)
    corpus2.append(review)    
    
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features = cv.fit_transform(corpus).toarray()
features_test = cv.fit_transform(corpus2).toarray()

X = np.concatenate((X, features), axis =1)
X_test = np.concatenate((X_test, features_test), axis =1)

from sklearn.neighbors import KNeighborsClassifier
KNN = KNeighborsClassifier()
KNN.fit(X,y)
y_pred = KNN.predict(X_test)
y_pred.tolist()

