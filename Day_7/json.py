# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:07:53 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing
"""

import requests

url = "http://api.openweathermap.org/data/2.5/weather?q=Jaipur&appid=e9185b28e9969fb7a300801eb026de9c"

response = requests.get(url)
details = response.json()

print("Details of Jaipur:")
print("Latitude: {0}\nLongitude: {1}".format(details['coord']['lat'], details['coord']['lon']))
print("Weather Condition:")
print("Temperature: {0}\nPressure: {1}\nHumidity: {2}\nVisibility: {3}\nWind Speed: {4}".format
      (details['main']['temp'], details['main']['pressure'], details['main']['humidity'], 
       details['visibility'], details['wind']['speed']))
