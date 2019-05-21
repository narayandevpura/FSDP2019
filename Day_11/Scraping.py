# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:45:32 2019

@author: Narayan Devpura
"""
"""
Code Challenge: 
    
https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area

Scrap the data from State/Territory and National Share (%) columns for top 6 states basis on National Share (%). 
Create a Pie Chart using MatPlotLib and explode the state with largest national share %

"""
from bs4 import BeautifulSoup as BS
import requests


url = "https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"

data = requests.get(url).text

soup = BS(data , 'lxml')

table = soup.find('table', class_ = 'wikitable')

a = []
b = []
num = 1
body = table.find('tbody')
for row in body.findAll('tr'):
    if num <= 7:
        r = row.findAll('td')
        if r:
            a.append(r[1].text.strip())
            b.append(r[4].text.strip()) 
        num = num + 1

import matplotlib.pyplot as plt
plt.pie(x=b, labels = a, autopct='%2.2f%%', explode = (0.2,0,0,0,0,0), shadow = True, startangle = 180)
        