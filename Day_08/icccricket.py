# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:07:19 2019

@author: Narayan Devpura
"""


"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
    
    
    #https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    #https://www.icc-cricket.com/rankings/mens/team-rankings/test
"""

from bs4 import BeautifulSoup as BS
import requests

url = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"

data = requests.get(url).text

soup = BS(data , 'lxml')

table = soup.find('table', class_ = 'table')

a = []
b = []
c = []
d = []
e = []
h = []
for row in table.findAll('tr'):
    head = row.findAll('th')
    body = row.findAll('td')
    if len(body) > 0:
        a.append(body[0].text.strip())
        b.append(body[1].text.strip())
        c.append(body[2].text.strip())
        d.append(body[3].text.strip())
        e.append(body[4].text.strip())
    else:
        
        for i in head:
            h.append(i.text)

import pandas as pd

df = pd.DataFrame(dict(zip(h,[a,b,c,d,e])))
df.to_csv('ODI Rankings.csv')

    

