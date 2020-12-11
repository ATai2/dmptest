#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/5/25 11:00
# software: PyCharm


from selenium import webdriver


class Test(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(Config.url)

    def get_driver(self):
        return self.driver

    def test_login(self):
        self.driver.find_element_by_id("j_username").send_keys("scott")
        self.driver.find_element_by_id("j_password").send_keys("aaaaaa")
        self.driver.find_element_by_class_name("login-btn").click()

        return self.driver

    def test_close(self):
        self.driver.quit()

    # def __del__(self):
    #     退出程序时关闭浏览器
        # self.driver.quit()


# driver.implicitly_wait(10)
# driver.find_element_by_id('content2').click()
# time.sleep(5)
# # //iframe[@name='editor_body']//body[@contenteditable='true']
# driver.switch_to.frame("mainpartiframe")
#
# # driver.find_element_by_id("_easyui_tree_6").click()
#
# driver.find_element_by_xpath("//span[contains(text(),'设计区')]").click()
# driver.find_element_by_xpath("//span[contains(text(),'工厂分层')]").click()
# driver.find_element_by_xpath("//span[contains(text(),'ODS操作数据')]").click()
# driver.find_element_by_xpath("//span[contains(text(),'ODS1')]").click()
#
#
# time.sleep(20)
# driver.quit()   # 使用完, 记得关闭浏览器, 不然chromedriver.exe进程为一直在内存中.


if __name__ == '__main__':
    bean = Test()
    bean.test_login()

    print(bean.driver.get_cookies())

    bean.test_close()
