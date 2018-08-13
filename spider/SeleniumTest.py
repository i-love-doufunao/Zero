# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import random
import time

browser = webdriver.Chrome()
browser.get("https://www.zhipin.com/")

browser.find_element_by_xpath("//div[contains(@class,'search-box')]").click()
time.sleep(1)

lis=browser.find_elements_by_xpath("//div[@class='dorpdown-city']/ul/li/data-val")
for li in lis:
    print(li)

