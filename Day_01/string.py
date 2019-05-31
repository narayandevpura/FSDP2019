# -*- coding: utf-8 -*-
"""
Created on Fri May 31 12:52:32 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    String Handling
  Filename: 
    string.py
  Problem Statement:
    Take first and last name in single command from the user and print  them in reverse order with a space between them, find the index using find/index function and then print using slicing concept of the index
  Input:
      Sylvester Fernandes
  Output: 
      Fernandes Sylvester 
"""

# input from user
name = input("Enter your name with lastname :")

# index for space
index = name.index(' ')  

print (name[index+1:]+' '+name[0:index+1])

