#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/5/25 11:00
# software: PyCharm


import time
import common.Login as Login


class Test(object):

    def test_open(self, driver):
        driver.get(Config.url + 'mainFrame?id=DACX')
        time.sleep(5)

    def test_b_api_add(self,driver):
        driver.find_element_by_xpath("//li/div/span[contains(text(),'B接口')]").click()
        # driver.implicitly_wait(10)
        iframe = driver.find_element_by_tag_name("iframe")
        bapi_url = iframe.get_attribute("src")
        # driver.get(bapi_url)
        driver.switch_to.frame("iframe1080")

        time.sleep(8)
        driver.find_element_by_xpath("//td[contains(text(),'添加')]").click()
        driver.find_element_by_xpath("//input[0]").send_keys("scott0")
        driver.find_element_by_xpath("//input[1]").send_keys("scott1")
        driver.find_element_by_xpath("//input[2]").send_keys("scott2")
        driver.quit()


if __name__ == '__main__':
    bean = Test()
    driver = Login.Test().test_login()
    bean.test_open(driver)
    bean.test_b_api_add(driver)
