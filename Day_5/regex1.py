# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:02:58 2019

@author: Narayan Devpura
"""

"""

Code Challenge
  Name: 
    Regular Expression 1
  Filename: 
    regex1.py
  Problem Statement:
    You are given a string N. 
    Your task is to verify that N is a floating point number.
    Take Input From User

    In this task, a valid float number must satisfy all of the following 
    requirements:  
   
    Number can start with +, - or . symbol.
  Hint: 
    Using Regular Expression 
  Input:
    4  
    4.000
    -1.00
    +4.54
  Output:
    False
    True
    True
    True
"""

import re
while True:
    N = input('Enter a string: ')
    
    if re.search(r'^[+-]?[0-9]*\.[0-9]+$',N):
        print(re.search(r'^[+-]?[0-9]*\.[0-9]+$',N).start())
        print('True')
    elif N == 'q':
        break
    else:
        print('False')
    