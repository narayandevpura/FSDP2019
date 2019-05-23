# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:38:32 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Filename: 
    height.py
  Problem Statement:

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

height_total = 0
height_count = 0
for person in people:
    if 'height' in person:
        height_total += person['height']
        height_count += 1

if height_count > 0:
    average_height = height_total / height_count

    print (average_height)
    
Try rewriting the code below using map, reduce and filter. 
Filter takes a function and a collection. 
It returns a collection of every item for which the function returned True.
    

"""
from functools import reduce
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

persons = list(filter(lambda item: 'height' in item, people))
height = list(map(lambda x: x['height'], persons))
total = reduce(lambda x,y: x+y, height)

#total = reduce(lambda x,y: x+y,map(lambda x: x['height'], filter(lambda item: 'height' in item, people)))

print("Average height is: ", total/len(height))