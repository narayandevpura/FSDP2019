# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:25:18 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    Digit Letter Counter
  Filename: 
    digit_letter_counter.py
  Problem Statement:
    Write a Python program that accepts a string from User and calculate the number of digits and letters.
  Hint:
    Store the letters and Digits as keys in the dictionary  
  Input: 
    Python 3.2
  Output:
    Digits 2
    Letters 6 
"""

inputs = input('Enter something: ')
digit = 0
alpha = 0

for item in inputs:
    if item.isdigit():
        digit += 1
    elif item.isalpha():
        alpha += 1
    else:
        continue
print("Digits: ",digit)
print("Letters: ",alpha)