# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:10:03 2019

@author: Narayan Devpura
"""

Input = input("enter some integers: ")
int_list = list(map(int,Input.split()))
for item in int_list:
    if item > 0 and str(item) == str(item)[::-1]:
        flag = True
        break
    else:
        flag = False
if flag == True:
    print("True")
else:
    print("False")
