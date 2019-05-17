# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:07:27 2019

@author: Narayan Devpura
"""

"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""

import pandas as pd
from selenium import webdriver

url = "https://bidplus.gem.gov.in/bidlists"

driver = webdriver.Chrome("C:/Users/User/Desktop/Forsk_ML-Training/chromedriver")

driver.get(url)

a=[]
b=[]
c=[]
d=[]
e=[]
f=[]

for i in range(1,11):    
    bid = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a')
    items = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span')
    quantity = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/span')
    dept = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]')
    sdate = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span')
    edate = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span')

    a.append(bid.text.strip())
    b.append(items.text.strip())
    c.append(quantity.text.strip())
    d.append(dept.text.strip())
    e.append(sdate.text.strip())
    f.append(edate.text.strip())


heads = ['Bid No.','Items', 'Quantity Required', 'Department and Address', 'Start Date', 'End Date']    
df = pd.DataFrame(dict(zip(heads,[a,b,c,d,e,f])))

df.to_csv('bid_plus.csv')

    
