# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:45:01 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""

fp = open('absentee.txt','w')
num = 0
while num != 25:
    name = input('Enter name')
    if name != '':
        fp.write(name)
        fp.write('\n')
        num += 1
    else:
        break
fp.close()
fp = open('absentee.txt', 'rt')

print(fp.read())
fp.close()
