# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:31:12 2019

@author: Narayan Devpura
"""

Input = list(map(int,input("Enter space separeted list of numbers").split()))

Input.remove(max(Input))
Input.remove(min(Input))
sums = 0
length = len(Input)
for i in Input:
    sums += i
average = int(sums/length)
print("Centered Average is: " + str(average))
