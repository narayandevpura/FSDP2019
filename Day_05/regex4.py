# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:04:23 2019

@author: Narayan Devpura
"""

"""

Code Challenge
  Name: 
    Regular Expression 4
  Filename: 
    regex4.py
  Problem Statement:
    You are given email addresses. 
    Your task is to print a list containing only valid email addresses in lexicographical order .
    (Take input from User)

    Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores. 
    The website name can only have letters and digits. 
    The maximum length of the extension is  
 
  Hint: 
    Using Regular Expression 
  Input:
    ajeet@forsk.com
    kunal-23@forsk.com
    yogendra_54@forsk.com
  Output:
    ['ajeet@forsk.com', 'kunal-23@forsk.com', 'yogendra_54@forsk.com’]

"""

import re
ls = []
while True:
    N = input('Enter email addresses: ')

    if re.search(r'^[a-z0-9_-]+@[a-z0-9]+\.[a-z]{2,4}$',N):
        ls.append(N)
    elif N == 'q':
        break
    else:
        continue

print(sorted(ls))
