# -*- coding: utf-8 -*-
"""
Created on Fri May 31 12:44:10 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    Formatted String
  Filename: 
    format2.py
  Problem Statement:
    Write a program to print the output in the given format. 
    Take input from the user. 
  Hint:
    Try to serach for some function in the str class using help() and dir()
  Input:
    Welcome to Pink City Jaipur
  Output:
    Welcome*to*Pink*City*Jaipur
"""

# input string
x = input("Enter a string :")

# splitted string
x_split = x.split()

print ("*".join(x_split))