# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:10:31 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    Normally Distributed Random Data
  Filename: 
    normal_dist.py
  Problem Statement:
    Create a normally distributed random data with parameters:
    Centered around 150.
    Standard Deviation of 20.
    Total 1000 data points.
    
    Plot the histogram using matplotlib (bucket size =100) and observe the shape.
    Calculate Standard Deviation and Variance. 
"""

import numpy as np
import matplotlib.pyplot as plt
data = np.random.normal(150, 20, 1000)

plt.hist(data, bins = 100)
print("Standard deviation is: ",np.std(data))
print("Variance is: ",np.var(data))