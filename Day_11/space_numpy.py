# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:04:10 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    Space Seperated data
  Filename: 
    space_numpy.py
  Problem Statement:
    You are given a 9 space separated numbers. 
    Write a python code to convert it into a 3x3 NumPy array of integers.
  Input:
    6 9 2 3 5 8 1 5 4
  Output:
      [[6 9 2]
      [3 5 8]
      [1 5 4]]
  
"""

lists = list(map(int, input("Enter space separated numbers: ").split()))
import numpy as np
x = np.array(lists).reshape((3,3))
print("2-D Array is:")
print(x)