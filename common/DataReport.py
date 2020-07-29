#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/5/25 11:00
# software: PyCharm


from selenium import webdriver
import time, requests,base64
import common.Config as config


class Test(object):
    url = "http://localhost:8085"

    # def __init__(self):
        # self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        # self.driver.get(config.url)

    def test_login(self):
        self.driver.find_element_by_id("j_username").send_keys("scott")
        self.driver.find_element_by_id("j_password").send_keys("aaaaaa")
        self.driver.find_element_by_class_name("login-btn").click()

        return self.driver

    def test_getSettingData(self):
        url = self.url + '/dmp-datafactory/gzapi/getSettingData'
        s = requests.Session()
        s.auth = ('c2NvdHQ=', 'YWFhYWFh')
        s.headers.update({'x-test': 'true'})
        # 用session对象发出get请求，设置cookies
        post = s.post(url)
        # post = requests.post(url)
        print(post.text)

    def test_save(self, data):
        pass

    def test_getSessionParams(self):
        # 创建一个session对象
        s = requests.Session()
        s.auth = ('scott', 'aaaaaa')
        s.headers.update({'x-test': 'true'})
        # 用session对象发出get请求，设置cookies
        post = s.post('http://localhost:8085/dmp-datafactory/user/login',
                      json={"j_username": "scott", "j_password": "aaaaaa"})
        # 用session对象发出另外一个get请求，获取cookies
        # r = s.get("http://httpbin.org/cookies")
        # 显示结果
        # r.text





if __name__ == '__main__':
    bean = Test()
    bean.test_getSettingData()
