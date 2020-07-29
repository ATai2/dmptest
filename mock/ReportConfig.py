#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/7/10 11:28
# software: PyCharm

from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
try:
    driver.maximize_window()
    driver.get("http://localhost:8085/dmp-datafactory")
    driver.find_element_by_id("j_username").send_keys("scott")
    driver.find_element_by_id("j_password").send_keys("aaaaaa")
    time.sleep(2)
    driver.find_element_by_class_name("login-btn").click()

    driver.find_element_by_class_name("slick-next").click()

    WebDriverWait(driver, 20, 0.5).until(lambda x: x.find_element_by_id("content11"))
    driver.find_element_by_id("content11").click()
    driver.switch_to.frame("mainpartiframe")
    driver.find_element_by_xpath("//ul[@id='tree']/li[1]/ul/li[1]").click()

except Exception as e:
    print(e)
    driver.quit()
else:
    time.sleep(20)
    driver.quit()
