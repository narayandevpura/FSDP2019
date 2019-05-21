# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:11:16 2019

@author: Narayan Devpura
"""
"""
 Code Challenge 

 Find the mean, median, mode, and range for the following list of values:
 13, 18, 13, 14, 13, 16, 14, 21, 13


Answer : Mean = 15, Median = 14 , Mode = 13 , Range = 21 - 13 = 8
"""

import numpy as np
x = [13,18,13,14,13,16,14,21,13]
np.array(x)

Mean = np.mean(x,dtype=int)
Median = np.median(x)
Mode =  np.bincount(x).argmax()
Range = np.max(x) - np.min(x)

print("Mean: ",Mean)
print("Median: ",int(Median))
print("Mode: ", Mode)
print("Range: ",Range)