# -*- coding: utf-8 -*-
"""
Created on Fri May 31 12:52:11 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    Ride Cost Calculator
  Filename: 
    ridecost_cal.py
  Problem Statement:
    Assume you travel 80 km to and fro in a day. 
    Cost of Diesel per litre is 80 INR 
    Your vehicle Fuel Average is 18 km/litre. 
    Now calculate the cost of driving per day to office. 
  Hint: 
 """    
 
# distance travel
travel = 80
 
# Diesel cost
cost = 80
 
# Vehicle fuel average
fuel_avg = 18

fuel_used = (travel/fuel_avg)
 
# cost of driving per day to office
cost_per_day = (cost*fuel_used)

print ("Cost of driving per day to office is :"+str(round(cost_per_day,2))+" INR")