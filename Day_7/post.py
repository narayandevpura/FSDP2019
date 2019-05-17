# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:44:56 2019

@author: Narayan Devpura
"""


# Create a new Code Challenge to POST data 

# Research the below wesbite and post some data on it

# https://requestbin.com

import requests

Host = "http://httpbin.org"

data = {"firstname":"abx","language":"Urdu"}

headers = {"Content-Type":"application/json","Content-Length":len(data)}

def post_method():
    response = requests.post(Host+"/post",json=data)
    return response

print ( post_method().text )


def get_method():
    response = requests.get("http://httpbin.org/get?q=firstname=dev023")
    return response

print (get_method().json())
