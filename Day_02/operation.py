# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:59:23 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    Operations Function
  Filename: 
    operation.py
  Problem Statement:
    Write following functions for list operations. Take list as input from the User
    Add(), Multiply(), Largest(), Smallest(), Sorting(), Remove_Duplicates(), Print()
    Only call Print() function to display the results in the below displayed 
    format (i.e all the functions must be called inside the print() function 
    and only the Print() is to be called in the main script)

  Input: 
    5,2,6,2,3
  Output:
    Sum = 18
    Multiply = 360
    Largest = 6
    Smallest = 2
    Sorted = [2, 2, 3, 5, 6]
    Without Duplicates = [2, 3, 5, 6]  
"""

usr_input = list(map(int,input("Enter a list of numbers (space separated): ").split()))

def Sum(lists):
    return sum(lists)

def Multiply(lists):
    mul = 1
    for item in lists:
        mul *= item
    
    return mul

def Largest(lists):
    return max(lists)

def Smallest(lists):
    return min(lists)

def Sorted(lists):
    return sorted(lists)

def NoDuplicates(lists):
    return list(set(lists))

def Print(lists):
    print("Sum = {0}".format(Sum(lists)))
    print("Multiply = {0}".format(Multiply(lists)))
    print("Largest = {0}".format(Largest(lists)))
    print("Smallest = {0}".format(Smallest(lists)))
    print("Sorted = {0}".format(Sorted(lists)))
    print("NoDuplicates = {0}".format(NoDuplicates(lists)))
    
Print(usr_input)