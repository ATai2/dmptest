#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/5/25 11:00
# software: PyCharm

import json
import time, requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.Rest import restPost


class DmpLogin():
    def __init__(self):
        self.url = 'http://localhost:8085'
        # 启用无头模式，可选
        browser_options = webdriver.ChromeOptions()
        browser_options.add_argument('--headless')
        browser_options.add_argument('--disable-gpu')
        self.browser = webdriver.Chrome(chrome_options=browser_options)
        # self.browser = webdriver.Chrome()

        self.login_system()
        cookies = self.get_cookies()
        cookieMap = {}
        cookieStr = ""
        for item in cookies:
            cookieStr += item['name'] + "=" + item['value'] + ";"
            cookieMap[item['name']] = item['value']
        self.headers = {
            "User_Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
            "Cookie": cookieStr
        }
        self.close()

    # 登录系统，具体到自己系统时需要自行修改
    def login_system(self):
        # 登录用户名密码，改成目标系统用户名密码
        username = "scott"
        password = "aaaaaa"
        # 登录页面url，改成目标系统登录页面
        url = self.url + "/dmp-datafactory/#"
        self.browser.get(url)
        # 显性等待，直到用户名控件加载出来才进行下一步
        WebDriverWait(self.browser, 20, 0.5).until(lambda x: x.find_element_by_id("j_username"))
        # WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("someId"))
        # WebDriverWait(self.browser,20,0.5).until(EC.presence_of_element_located((By.ID,"j_username")))
        # 填写用户名
        self.browser.find_element_by_id("j_username").send_keys(username)
        # 填写密码
        self.browser.find_element_by_id("j_password").send_keys(password)
        # 点击登录
        self.browser.find_element_by_class_name("login-btn").click()
        # 强制等待5秒，待session和token都成功返回并存到浏览器中
        # restful隐性等待不太好用？self.browser.implicitly_wait(5)
        # time.sleep(5)

    def get_welcome(self):
        self.browser.get(self.url + "/dmp-datafactory/welcome")

    # 获取sessionid
    def get_sessionid(self):
        # 是要从localStorage中获取还是要从sessionStorage中获取，具体看目标系统存到哪个中
        # window.sessionStorage和直接写sessionStorage是等效的
        # 一定要使用return，不然获取到的一直是None
        # get的Item不一定就叫sessionId，得具体看目标系统把sessionid存到哪个变量中
        sessionid = self.browser.execute_script('return sessionStorage.getItem("sessionId");')

        # 另外sessionid一般都直接通过返回Set-Cookies头设置到Cookie中，所以也可以从Cookie读取
        # 获取浏览器所有Set-Cookie，返回对象是字典列表
        # cookies = self.browser.get_cookies()
        # 获取单项Cookie，是不是叫sessionId取决于系统存成什么变量，单项Cookie是字典
        # cookie = self.browser.get_cookie("sessionId")
        # cookie = cookie["value"]
        # print(f"{cookies}")
        # print(cookies)
        return sessionid

    def get_cookies(self):
        return self.browser.get_cookies()

    # 获取token
    def get_token(self):
        # 是要从localStorage中获取还是要从sessionStorage中获取，具体看目标系统存到哪个中
        # window.sessionStorage和直接写sessionStorage是等效的
        # 一定要使用return，不然获取到的一直是None
        # get的Item不一定就叫token，得具体看目标系统把token存到哪个变量中
        token = self.browser.execute_script('return sessionStorage.getItem("token");')
        # print(f"{token}")
        return token

    def getSettingData(self):
        url = self.url + '/dmp-datafactory/gzapi/getSettingData'
        post = restPost(url, headers=self.headers)
        return post

    def post_api(self, path, json=None, data=None):
        url = self.url + '/dmp-datafactory' + path

        return restPost(url, headers=self.headers, json=json, data=data)

    def get_api(self, path, params=None):
        url = self.url + '/dmp-datafactory' + path
        post = requests.get(url, params=params, headers=self.headers)
        if post.status_code == 200:
            print(post.text)
            return json.loads(post.text)
        else:
            print("post error")


    # post = requests.post(url, headers=headers)
    # print(post.text)

    # def __del__(self):
    #     # 退出程序时关闭浏览器
    #     self.browser.close()
    #     self.browser.quit()

    def close(self):
        # 退出程序时关闭浏览器
        self.browser.close()
        self.browser.quit()




# if __name__ == "__main__":
#     obj = DmpLogin()
#     try:
#
#         obj.save_settingdata()
#     except Exception as e:
#         print(e)
#     finally:
#         obj.close()
#
