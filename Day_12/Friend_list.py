# -*- coding: utf-8 -*-
"""
Created on Tue May 21 11:52:38 2019

@author: Narayan Devpura
"""

from selenium import webdriver
from time import sleep

url = "https://www.facebook.com/"

browser = webdriver.Chrome("C:/Users/User/Desktop/FSDP2019/chromedriver")

browser.get(url)

sleep(2)

email = browser.find_element_by_name("email")
username = "shivay2om@gmail.com"
email.send_keys(username)

sleep(2)

password = browser.find_element_by_name("pass")
pswd = "shivay@12345"
password.send_keys(pswd) 

login = browser.find_element_by_xpath('//*[@id="loginbutton"]')
login.click()

sleep(5)

name = browser.find_element_by_xpath('//*[@id="u_0_d"]/div[1]/div[1]/div/a/span/span')
name.click()

sleep(5)

friends = browser.find_element_by_xpath('//*[@id="u_fetchstream_3_9"]/li[3]/a')
friends.click()

sleep(5)

total_friends = browser.find_element_by_xpath('//*[@id="u_fetchstream_4_0"]/span[2]')

friends_list = []

for i in range(total_friends):
    friends_list.append(browser.find_element_by_xpath('//*[@id="pagelet_timeline_app_collection_100024548752324:2356318349:2"]/ul/li[i+1]/div/div/div[2]/div/div[2]/div/a'))

print(friends_list)