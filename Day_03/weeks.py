# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:14:04 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    weeks
  Filename: 
    weeks.py
  Problem Statement:
    Write a program that adds missing days to existing tuple of days
  Input: 
    ('Monday', 'Wednesday', 'Thursday', 'Saturday')
  Output:
    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
"""

tuple2 = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

inputs = (input('Enter week days :').split())

for item in tuple2:
    if item not in inputs:
        inputs.insert(tuple2.index(item),item)

print(tuple(inputs))
        