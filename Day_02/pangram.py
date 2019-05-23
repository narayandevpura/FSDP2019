# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:34:03 2019

@author: Narayan Devpura
"""

pangram = 'qwertyuioplkjhgfdsazxcvbnm'

Input = input("Enter a statement")
flag = 1
for i in pangram:
    if i not in Input:
        print("Not Pangram")
        flag = 0
        break
    else:
        flag = 1

if flag:
    print("Pangram")
