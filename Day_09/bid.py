# -*- coding: utf-8 -*-
"""
Created on Thu May 16 16:07:30 2019

@author: Narayan Devpura
"""

"""
Code Challenge 3
In the Bid plus Code Challenege 

          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)

Store the information into a database mySQL Database

"""

import mysql.connector 

conn = mysql.connector.connect(user = 'root', password = '', host= 'localhost')

c = conn.cursor()

c.execute("CREATE DATABASE bids_plus")
c.execute('USE bids_plus')
#c.execute('DROP TABLE bids')

c.execute("""CREATE TABLE bids(
        Bid_No VARCHAR(20),
        Items VARCHAR(20),
        Quantity_Required INT,
        DepartAndAddress VARCHAR(50),
        Start_Date VARCHAR(20),
        End_Date VARCHAR(20))""")

#import pandas as pd
from selenium import webdriver

url = "https://bidplus.gem.gov.in/bidlists"

driver = webdriver.Chrome("C:/Users/User/Desktop/Forsk_ML-Training/chromedriver")

driver.get(url)

for i in range(1,11):    
    bid = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a').text.strip()
    items = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span').text.strip()
    quantity = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/span').text.strip()
    dept = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]').text.strip().split('\n')
    sdate = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text.strip()
    edate = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text.strip()
    
    c.execute("INSERT INTO bids VALUES('"+bid+"','"+items+"',"+quantity+",'"+dept[0]+dept[1]+"','"+sdate+"','"+edate+"')")

#c.execute("SELECT * FROM bids")
#c.fetchall()
#c.execute("SELECT * FROM bids")

conn.commit()
conn.close()