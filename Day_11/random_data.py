# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:09:56 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    Random Data
  Filename: 
    random_data.py
  Problem Statement:
    Create a random array of 40 integers from 5 - 15 using NumPy. 
    Find the most frequent value with and without Numpy.
  Hint:
      Try to use the Counter class
      
"""
import numpy as np
# generating array of random numbers from 5 to 15
x = np.random.randint(5, 15, 40, dtype = int)
# most frequent no. using numpy
most_freq1 = np.bincount(x).argmax()

from collections import Counter
# most frequent no. without using numpy but using Counter class of collections library
most_freq2 = Counter(x).most_common(1)[0][0]

print("Most frequent using numpy : ",most_freq1)
print("Most frequent using Counter : ",most_freq2)