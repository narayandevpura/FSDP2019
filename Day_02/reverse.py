# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:56:03 2019

@author: Narayan Devpura
"""

def reverse(string):
    strr=''
    length = len(string)
    for i in range(length-1,-1,-1):
        strr = strr + string[i]
    print(strr)
    
reverse('I am testing')