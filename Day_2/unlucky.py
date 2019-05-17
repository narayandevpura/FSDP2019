# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:36:45 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    Unlucky 13
  Filename: 
    unlucky.py
  Problem Statement:
    Return the sum of the numbers in the array, returning 0 for an empty array. 
    Except the number 13 is very unlucky, so it does not count and numbers that 
    come immediately after a 13 also do not count
    Take input from user  
  Input: 
    13, 1, 2, 13, 2, 1, 13
  Output:
    3
"""

usr_input = list(map(int,input("Enter a list of numbers (space separated): ").split()))
sums = 0 
flag = False

for item in usr_input:
    sums += item
    
    if flag:
        sums -= item
        flag = False
 
    if item == 13:
        sums -= 13
        flag = True

print (sums)