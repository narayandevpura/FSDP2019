# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:45:30 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    Romeo and Juliet
  Filename: 
    romeo.py
  Problem Statement:
    Let’s start with a very simple file of words taken from the text of 
    Romeo and Juliet. (romeo.txt)
    We will write a Python program to read through the lines of the file
    break each line into a list of words
    and then loop through each of the words in the line,
    and count each word using a dictionary.    
"""

with open('romeo.txt', mode = 'r') as fp:
    dict1 = {}
    for line in fp:
        for item in line.split():
            if item in dict1.keys():
                dict1[item] += 1
            else:
                dict1[item] = 1
        
print("Count of each word in file is: ",dict1)