#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/9/22 9:01
# software: PyCharm

from selenium import webdriver
import json


class TestOneStation(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://10.110.87.200:8912/#/")
        self.driver.implicitly_wait(3)
        # self.driver.switch_to.frame()


    def loginOneStation(self,name,pwd):
        driver = self.driver
        input_list = driver.find_elements_by_tag_name("input")
        input_list[0].send_keys(name)
        input_list[1].send_keys(pwd)
        driver.find_element_by_class_name('form-actions').click()



    def add_org(self, driver, org):
        driver.find_element_by_class_name("mColImg").click()
        driver.find_element_by_xpath("//span[@title='用户管理']").click()
        driver.find_element_by_xpath("//span[@title='系统组织']").click()
        close_items = driver.find_elements_by_class_name("ant-tree-switcher_close")
        for item in close_items:
            item.click()

        #         切换iframe
        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@class='frameActive']"))
        li_texts = driver.find_elements_by_tag_name("li")
        for text in li_texts:
            if text.text == org:
                print("add org already exists")
                return True

        #         org not exists   点击增加同级
        btns = driver.find_elements_by_tag_name("button")
        btns[0].click()
        # driver.find_element_by_xpath('//button/span[contains(text(), "增加同级")]')
        inputs = driver.find_elements_by_tag_name("input")
        # 编号
        inputs[2].send_keys(org)
        # 名称
        inputs[3].send_keys(org)

        btns[3].click()

    def add_user(self, driver):
        with open("user.json", "r") as f:
            readlines = f.readlines()
        json.loads(readlines)


if __name__ == '__main__':
    pass
