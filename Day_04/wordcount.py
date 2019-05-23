# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:46:41 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    Word count
  Filename: 
    wordcount.py
  Problem Statement:
    Unix systems contain many utility functions. 
    One of the most useful to me is wc, the "word count" program. 
    If you run wc against a text file, it'll count the characters, words, 
    and lines that the file contains.
     
    The challenge for this exercise is to write a version of wc in Python. 
    However, your version of wc will return four different types of information 
    about the files:
 
        Number of characters (including whitespace)
        Number of words (separated by whitespace)
        Number of lines
        Number of unique words
    
    The program should ask the user for the name of an input file, 
    and then produce output for that file. 
    
"""

file = input('Enter filename: ')
with open(file, mode = 'r') as fp:
    c_line = 0
    c_words = 0
    c_char = 0
    c_unique = 0
    w = set()
    for line in fp:
        c_line += 1
        c_char += len(line)
        for item in line.split():
            c_words += 1
            w.add(item)
    c_unique += len(w)
    print('Number of characters: ',c_char)
    print('Number of words: ',c_words)
    print('Number of lines: ',c_line)
    print('Number of unique words: ',c_unique)
            
            
                
            
        