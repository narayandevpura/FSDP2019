# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:00:45 2019

@author: Narayan Devpura
"""
"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic2.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      You need to develop using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:
    True
"""
inputs = input('Enter list of numbers: ').split()
if all([int(x) for x in inputs]) and any([x == x[::-1] for x in inputs]):
    print('True')
else:
    print('False')