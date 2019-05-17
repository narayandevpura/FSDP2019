# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:52:02 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    Bricks
  Filename: 
    bricks.py
  Problem Statement:
    We want to make a row of bricks that is target inches long. 
    We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
    Make a function that prints True if it is possible to make the exact target 
    by choosing from the given bricks or False otherwise. 
    Take list as input from user where its 1st element represents number of small bricks, 
    middle element represents number of big bricks and 3rd element represents the target.
  Input: 
    2, 2, 11
  Output:
    True
"""

small_bricks, large_bricks, target = input('Enter small bricks, large bricks and target : ').split(',')
small_bricks = int(small_bricks)
large_bricks = int(large_bricks)
target = int(target)
flag = True
while target:
    if target >= 5 and large_bricks != 0:
        target -= 5
        large_bricks -= 1
    elif target >= 1 and small_bricks != 0:
        target -= 1
        small_bricks -= 1
    else:
        flag = False
        break
    
if flag:
    print("True")
else:
    print("False")
