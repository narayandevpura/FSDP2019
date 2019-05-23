# -*- coding: utf-8 -*-
"""
Created on Mon May 13 18:09:41 2019

@author: Narayan Devpura
"""


"""
This Python function accepts a list of numbers and computes the product of all the odd numbers:

def productOfOdds(list):
    result = 1
    for i in list:
        if int(i) % 2 == 1:
            result *= int(i)
    return result
    

    
Rewrite the Python code using map, filter, and reduce:

def productOfOdds(list):
    return reduce(r_func, filter(f_func, map(m_func, list)))

    
"""

from functools import reduce
def productOfOdds(lists):
    return reduce(lambda x, y: x*y , filter(lambda x: x % 2 ==1 ,map(int,lists)))

lists = input('Enter list of numbers: ').split()
productOfOdds(lists)