# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:51:12 2019

@author: Narayan Devpura
"""
# Hands On 1
# Create a list of number from 1 to 20 using range function. 
list1 = [i for i in range(1,21)]
list1

# Using the slicing concept print all the even and odd numbers from the list 
list_even = list1[1::2]
list_odd = list1[::2]
print (list_even)
print (list_odd)

# Hands On 2
# Make a function to find whether a year is a leap year or no, return True or False

def leapYear(year):
    if year % 400 == 0 :
        return True
    elif year % 4 == 0 and year % 100 != 0:
            return True
    else:
        return False

leapYear(2010)

# Hands On 3
# Make a function days_in_month to return the number of days in a specific month of a year

def Days_in_month(month):
    tuple1 = ('january','march','may','july','august','october','december')
    tuple2 = ('april','june','september','november')
    
    if month.lower() in tuple1:
        return 31
    elif month.lower() in tuple2:
        return 30
    else:
        return (28,29)
    
Input = input("Enter full month name: ")
print("No. of days in {0} is {1}".format(Input.title(),Days_in_month(Input)))