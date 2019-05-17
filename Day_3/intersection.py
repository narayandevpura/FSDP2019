# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:25:19 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    Intersection
  Filename: 
    Intersection.py
  Problem Statement:
    With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155]
    Write a program to make a list whose elements are intersection of the above given lists.  
"""

inp1 = list(map(int, input('Enter first list').split(',')))
inp2 = list(map(int, input('Enter second list').split(',')))

print("first list is: ", inp1)
print("second list is: ", inp2)

inp3 = set(inp1).intersection(set(inp2))

print('new list is: ',list(inp3))