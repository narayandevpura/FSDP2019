# -*- coding: utf-8 -*-
"""
Created on Tue May 21 11:50:45 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    Thanks giving Analysis
  Filename: 
    Thanksgiving.py
  Problem Statement:
    Read the thanksgiving-2015-poll-data.csv file and 
    perform the following task :

    Discover regional and income-based patterns in what Americans eat for 
    Thanksgiving dinner

    Convert the column name to single word names
    
    Using the apply method to Gender column to convert Male & Female
    Using the apply method to clean up income
    (Range to a average number, X and up to X, Prefer not to answer to NaN)
    
    compare income between people who tend to eat homemade cranberry sauce for
    Thanksgiving vs people who eat canned cranberry sauce?
    
    find the average income for people who served each type of cranberry sauce
    for Thanksgiving (Canned, Homemade, None, etc).
    
    Plotting the results of aggregation
    
    Do people in Suburban areas eat more Tofurkey than people in Rural areas?
    Where do people go to Black Friday sales most often?
    Is there a correlation between praying on Thanksgiving and income?
    What income groups are most likely to have homemade cranberry sauce?

    Verify a pattern:
        People who have Turducken and Homemade cranberry sauce seem to have 
        high household incomes.
        People who eat Canned cranberry sauce tend to have lower incomes, 
        but those who also have Roast Beef have the lowest incomes
        
    Find the number of people who live in each area type (Rural, Suburban, etc)
    who eat different kinds of main dishes for Thanksgiving:
        
  Hint:

"""

import pandas as pd
import numpy as np

# Read the thanksgiving-2015-poll-data.csv file

tg = pd.read_csv('material/thanksgiving.csv', encoding = 'latin1')

# Discover regional and income-based patterns in what Americans eat for Thanksgiving dinner
    
# Incone-based   
eat_inc = tg.groupby('How much total combined money did all members of your HOUSEHOLD earn last year?')['What is typically the main dish at your Thanksgiving dinner?'].value_counts().unstack()

# Region-based
eat_reg = tg.groupby('US Region')['What is typically the main dish at your Thanksgiving dinner?'].value_counts().unstack()

# Convert the column name to single word names

tg.columns = [i for i in range(1, 66)]

#  Using the apply method to Gender column to convert Male & Female

tg[63].apply(lambda x: x[i-1] if x[i] ==  np.nan else x[i] for i in range(len(tg[63])))