# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:25:20 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    Duplicate
  Filename: 
    duplicate.py
  Problem Statement:
    With a given list [12,24,35,24,88,120,155,88,120,155]
    Write a program to print this list after removing all duplicate values 
    with original order reserved  
"""

ls = input("Enter list of numbers: ").split(',')
ls2 = []
for item in ls:
    if item in ls2:
        continue
    else:
        ls2.append(item)
print(ls2)