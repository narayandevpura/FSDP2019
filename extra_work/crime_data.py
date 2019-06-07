# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 22:03:34 2019

@author: Narayan Devpura
"""

import folium
import csv
import pandas as pd

df = pd.read_csv('crime_data.csv')
dfe = pd.read_csv('crime_map.csv')
city=[]
data_lon=[]
data_lat=[]
crime_name=[]
#Reading csv file.
y=0
with open("crime_map.csv") as crime:
    read=csv.reader(crime,delimiter=",")
    for i in read:
        if(y%2==0):
            city.append(i[0])
            crime_name.append(i[1])
            data_lon.append(i[8])
            data_lat.append(i[9])
        y+=1
#for skiping columns name
city=city[1:]
data_lon=data_lon[1:]
data_lat=data_lat[1:]

map = folium.Map([20.5937,78.9629], zoom_start=5)

tile = folium.TileLayer('Mapbox Bright').add_to(map)
tile = folium.TileLayer('Mapbox Control Room').add_to(map)
tile = folium.TileLayer('Stamen Terrain').add_to(map)
tile = folium.TileLayer('Stamen Toner').add_to(map)
tile = folium.TileLayer('stamenwatercolor').add_to(map)
tile = folium.TileLayer('cartodbpositron').add_to(map)
tile = folium.TileLayer('cartodbdark_matter').add_to(map)

from folium.plugins import MarkerCluster
marker_cluster = MarkerCluster().add_to(map)
#adding marker and popup of city and crime-name
for i in range(0,len(city)):
    folium.Marker([float(data_lon[i])  ,float(data_lat[i])],popup="city name ="+city[i]+"\n crime_of_city = "+crime_name[i]).add_to(marker_cluster)
#we can change tiles with help of LayerConrol
folium.LayerControl().add_to(map)

#saving map to a html file
map.save('crime_data.html')
#creating a html iframe
from IPython.display import HTML
HTML('<iframe src=plot_data.html width=300 height=200></iframe>')







