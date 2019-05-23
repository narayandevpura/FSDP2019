# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:17:56 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    Translate Function
  Filename: 
    translate.py
  Problem Statement:
    Write a function translate() that will translate the text as mentioned. 
    That is, double every consonant and place an occurrence of "o" in between. 
    Take Input from User  
  Input: 
    This is fun
  Output:
    ToThohisos isos fofunon  
"""

def translate(string):
    newstr = ''
    vowels = 'aeiou AEIOU'
    
    for char in string:
        if char not in vowels:
            newstr = newstr + char + 'o' + char
        else:
            newstr += char
    
    return newstr

inp = input("Enter a string: ")
translate(inp)

