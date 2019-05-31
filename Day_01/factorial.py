# -*- coding: utf-8 -*-
"""
Created on Fri May 31 12:40:59 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    Facorial
  Filename: 
    factorial.py
  Problem Statement:
    Find the factorial of a number. 
  Hint: 
    Factorial of 3 = 3 * 2 * 1= 6 
    Try to first find the function from math module using dir and help 
  Input:
    Take the number from the keyboard as input from the user.
"""

from math import factorial
x = input("Enter the number: ")
Fact = factorial(int(x))
print ("Factorial of {0} is {1}".format(x,Fact))