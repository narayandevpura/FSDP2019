# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:01:14 2019

@author: Narayan Devpura
"""

num = int(input("Enter a number: "))
for i in range(1,num):
    print('* ' * i)

for i in range(num,0,-1):
    print('* ' * i)
    