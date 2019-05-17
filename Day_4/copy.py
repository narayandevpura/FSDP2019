# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:44:15 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    copy command
  Filename: 
    copy.py
  Problem Statement:
    Make a program that create a copy of a file    
"""
filename = input('Enter filename: ')
with open(filename,'r') as rf:
    with open('copy.txt','w') as wf:
        for line in rf:
            wf.write(line)
print('Copy of file created as copy.txt')

