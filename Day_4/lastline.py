# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:45:43 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    Last Line
  Filename: 
    lastline.py
  Problem Statement:
    Ask the user for the name of a text file. 
    Display the final line of that file.
    Think of ways in which you can solve this problem, 
    and how it might relate to your daily work with Python.
"""

file = input('Enter file name: ')
with open(file, mode = 'r') as fp:
    ls = []
    for line in fp:
        ls.append(line)
    print(ls[-1])