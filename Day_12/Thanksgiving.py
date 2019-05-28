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
import re

# Read the thanksgiving-2015-poll-data.csv file

tg = pd.read_csv('material/thanksgiving.csv', encoding = 'Windows 1252')


# Handling Nan values

tg = tg.replace(np.nan,"Missing")


# Discover regional and income-based patterns in what Americans eat for Thanksgiving dinner
# Income-based   

eat_incm = tg.groupby('How much total combined money did all members of your HOUSEHOLD earn last year?')['What is typically the main dish at your Thanksgiving dinner?'].value_counts().unstack().fillna(0)

# Region-based

eat_reg = tg.groupby('US Region')['What is typically the main dish at your Thanksgiving dinner?'].value_counts().unstack().fillna(0)


# Convert the column name to single word names

tg.columns = [i for i in range(1, 66)]


#  Using the apply method to Gender column to convert Male & Female

tg[63] = tg[63].apply(lambda x: 'M' if x ==  "Male" else ('F' if x == "Female"  else x ))


# What income groups are most likely to have homemade cranberry sauce?

incm_group = tg.groupby(64)[9].value_counts().unstack()
incm_group.iloc[:,1].plot.bar()


#  Using the apply method to clean up income
# (Range to a average number, X and up to X, Prefer not to answer to NaN)

tg[64] = tg[64].replace(['Missing', 'Prefer not to answer'], ['0', '0'])

def avg_incm(incm):
    incms = re.findall(r'\d+\W*\d+', incm)
    incms = [int(inc.replace(',','')) for inc in incms]
    
    if len(incms) != 0 :   
        return sum(incms)/len(incms)
        
    else:
        return np.nan
   
tg[64] = tg[64].apply(avg_incm)


# compare income between people who tend to eat homemade cranberry sauce for
# Thanksgiving vs people who eat canned cranberry sauce?

tg[9].unique()

sauce_group = tg.groupby(9)[64].mean()

sauce_group.iloc[[0, 1]].plot.bar()


# find the average income for people who served each type of cranberry sauce
# for Thanksgiving (Canned, Homemade, None, etc).
# Plotting the results of aggregation

sauce_group.plot.pie(autopct="%1.1f%%")


# Do people in Suburban areas eat more Tofurkey than people in Rural areas?

eat_group = tg.groupby(61)[3].value_counts().unstack()

eat_group.iloc[1:3,-3].plot.bar()

# Where do people go to Black Friday sales most often?

black_friday = tg[58].value_counts() 
black_friday.plot.pie(autopct="%1.1f%%")


# Is there a correlation between praying on Thanksgiving and income?

prayer_inc = tg.groupby(52)[64].value_counts().unstack().fillna(0)
prayer_inc_visual = prayer_inc.plot.bar()

###############################################################################