# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:07:29 2019

@author: Narayan Devpura
"""

"""
http://forsk.in/images/Forsk_logo_bw.png"

Download the image from the url above and store in your workking diretory with the same
name as the image name.

Do not hardcode the name of the image


"""

from selenium import webdriver
#from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.actions.interaction import KEY
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/Users/User/Desktop/Forsk_ML-Training/chromedriver")
driver.get("http://forsk.in/images/Forsk_logo_bw.png")

img = driver.find_element_by_xpath('/html/body/img')

ac = ActionChains(driver)
ac.move_to_element(img).context_click(img).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()