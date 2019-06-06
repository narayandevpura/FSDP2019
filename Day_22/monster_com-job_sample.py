# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:42:01 2019

@author: Narayan Devpura
"""

"""
Code Challenge - 
 This is a pre-crawled dataset, taken as subset of a bigger dataset 
 (more than 4.7 million job listings) that was created by extracting data 
 from Monster.com, a leading job board.
 
 
 
 Remove location from Organization column?
 Remove organization from Location column?
 
 In Location column, instead of city name, zip code is given, deal with it?
 
 Seperate the salary column on hourly and yearly basis and after modification
 salary should not be in range form , handle the ranges with their average
 
 Which organization has highest, lowest, and average salary?
 
 which Sector has how many jobs?
 Which organization has how many jobs?
 Which Location has how many jobs?
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('material/monster_com-job_sample.csv')









