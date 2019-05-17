# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:23:25 2019

@author: Narayan Devpura
"""

"""
Vowels Finder
"""
states = ['Alabama', 'California', 'Oklahoma', 'Florida']
vowels = ('a','e','i','o','u','A','E','I','O','U')

new_states = []
for item in states:
    strr = ""
    for ele in item:
        if ele not in vowels:
            strr = strr + ele
            
    new_states.append(strr)       

print(new_states)
