# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:08:09 2019

@author: Narayan Devpura
"""
"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
"""

import requests

url1 = "http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y&apiKey=1ef10a3f684542e6600c"
url2 = "http://data.fixer.io/api/latest?base=EUR&rates=INR&access_key=3bc5b1ad07bff13f15bacc9a7f2b0ee9"
response1 = requests.get(url1)
response2 = requests.get(url2)

USD_TO_INR = response1.json()
EUR_TO_INR = response2.json()

print("USD_TO_INR: ",USD_TO_INR['USD_INR']['val'])
print("EUR_TO_INR: ",EUR_TO_INR['rates']['INR'])