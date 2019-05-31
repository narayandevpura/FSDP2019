# -*- coding: utf-8 -*-
"""
Created on Fri May 31 12:51:38 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    Replacing of Characters
  Filename: 
    restart.py
  Problem Statement:
    In a hardcoded string RESTART, replace all the R with $ except the first occurrence and print it.
  Input:
    RESTART
  Output: 
    RESTA$T
"""

String = "RESTART"
String = String[::-1].replace("R","$",1)
print(String[::-1])
