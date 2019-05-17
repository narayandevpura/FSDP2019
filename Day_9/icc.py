# -*- coding: utf-8 -*-
"""
Created on Fri May 17 11:56:51 2019

@author: Narayan Devpura
"""

"""
Code Challenge 4

Scrap the data from the URL below and store in sqlite database

https://www.icc-cricket.com/rankings/mens/team-rankings/odi


"""

import sqlite3
#from pandas import DataFrame as DF

conn = sqlite3.connect("icccrickets.db")

c = conn.cursor()

#c.execute("DROP TABLE odi")
c.execute("""CREATE TABLE odis(
        Pos INT,
        Team TEXT,
        Weighted INT,
        Points INT,
        Rating INT)""")


from bs4 import BeautifulSoup as BS
import requests

url = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"

data = requests.get(url).text

soup = BS(data , 'lxml')

table = soup.find('table', class_ = 'table')

for row in table.findAll('tr'):
    head = row.findAll('th')
    body = row.findAll('td')
    if len(body) > 0:
        string = "INSERT INTO odis VALUES("+str(body[0].text.strip())+",'"+str(body[1].text.strip())+"',"+str(body[2].text.strip())+","+str(body[3].text.strip()).replace(',','')+","+str(body[4].text.strip())+")"
        c.execute(string)
        
c.execute('SELECT * FROM odis')

c.fetchall()

conn.commit()
conn.close()
