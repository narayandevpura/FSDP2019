# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:47:42 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    Teen Calculator
  Filename: 
    teen_cal.py
  Problem Statement:
    Take dictionary as input from user with keys, a b c, with some integer 
    values and print their sum. However, if any of the values is a teen -- 
    in the range 13 to 19 inclusive -- then that value counts as 0, except 
    15 and 16 do not count as a teens. Write a separate helper "def 
    fix_teen(n):"that takes in an int value and returns that value fixed for
    the teen rule. In this way, you avoid repeating the teen code 3 times  
  Input: 
    {"a" : 2, "b" : 15, "c" : 13}
  Output:
    Sum = 17
"""

dict1 = {}
print("enter name and age: ")
while True:
    usesr_input = input()
    
    if usesr_input != '':
        k,v = usesr_input.split()
        dict1[k] = int(v)
    if not usesr_input:
        break

print("dictionary is: ",dict1)
sums = 0
for k,v in dict1.items():
    if v not in (13,14,17,18,19):
        sums += v
print("Sum is: ",sums)
        