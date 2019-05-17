# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:06:15 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    generator
  Filename: 
    generator.py
  Problem Statement:
    This program accepts a sequence of comma separated numbers from user 
    and generates a list and tuple with those numbers.  
  Input: 
    2, 4, 7, 8, 9, 12
  Output:
    List : ['2', ' 4', ' 7', ' 8', ' 9', '12'] 
    Tuple : ('2', ' 4', ' 7', ' 8', ' 9', '122')
"""

inputs = input('Enter some numbers: ')

lists = inputs.split(',')
tuples = tuple(lists)

print("list is : {0}".format(lists))
print("tuple is : {0}".format(tuples))