# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:49:22 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    Character Frequency
  Filename: 
    frequency.py
  Problem Statement:
    This program accepts a string from User and counts the number of characters (character frequency) in the input string.  
  Input: 
    www.google.com
  Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
"""

inputs = input("Enter a string: ")
dict1 = {}

for item in inputs:
    if item in dict1.keys():
        dict1[item] += 1
    else:
        dict1[item] = 1
        
print(dict1)