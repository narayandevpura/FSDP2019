# -*- coding: utf-8 -*-
"""
Created on Tue May 21 11:51:23 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    Telecom Churn Analysis
  Dataset:
    Telecom_churn.csv
  Filename: 
    telecom_churn.py
  Problem Statement:
    Read the telecom_churn.csv file and perform the following task :
    To perfrom analysis on the Telecom industry churn dataset -
    1. Predict the count of Churned customer availing both voice mail plan and international plan schema
    2. Total charges for international calls made by churned and non-churned customer and visualize it
    3. Predict the state having highest night call minutes for churned customer
    4. Visualize -
        a. the most popular call type among churned user
        b. the minimum charges among all call type among churned user
    5. Which category of customer having maximum account lenght? Predict and print it
    6. Predict a relation between the customer and customer care service that whether churned customer have shown their concern to inform the customer care service about their problem or not
    7. In which area code the international plan is most availed?
"""


import pandas as pd

tel = pd.read_csv("material/Telecom_churn.csv")

# Predict the count of Churned customer availing both voice mail plan and international plan schema
churn_int_voice = tel[(tel['churn'] == True) & (tel['voice mail plan'] == 'yes') & (tel['international plan'] == 'yes')]['churn'].count()

# Total charges for international calls made by churned and non-churned customer and visualize it
tot_int_chrg_churn = tel[tel['churn'] == True]['total intl charge'].sum()
tot_int_chrg_non_churn = tel[tel['churn'] == False]['total intl charge'].sum()

import matplotlib.pyplot as plt
plt.pie([tot_int_chrg_churn, tot_int_chrg_non_churn], labels = ['tot_int_chrg_churn','tot_int_chrg_non_churn'],autopct="%2.2f%%")

# tel.groupby('churn')['total intl charge'].sum()

# Predict the state having highest night call minutes for churned customer
max_state = tel[tel['total night minutes'] == tel[(tel['churn'] == True)]['total night minutes'].max()]['state']

# visualize the most popular call type among churned user
most_pop = tel[(tel['churn'] == True)]