#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/10/14 10:21
# software: PyCharm

import json
from common.onestation.Login import TestOneStation


class SettingInfo(object):
    def __init__(self):
        self.login = TestOneStation()
        self.driver = self.login.driver

    def set_config_info(self):
        # swtich to settingInfo page
        # self.driver.find_element_by_xpath("//img[@title='数据报送']").click()
        # self.driver.switch_to.frame("DATSApp")
        # self.driver.find_element_by_xpath("//*[contains(text(),'配置信息')]").click()

        self.driver.get("http://10.110.87.200:8912/dmp/dmp-datafactory/mainFrame?id=DATS")
        self.driver.find_element_by_xpath("//*[contains(text(),'配置信息')]").click()
        self.driver.switch_to.frame(self.driver.find_elements_by_tag_name("iframe"))

        #  read config file
        with open('report_setting.json', 'r', encoding='utf-8') as f:
            content = f.read()
        settingContent = json.loads(content)

        #         set data
        # 报送单位
        self.clear_set_input(settingContent, 1, 'reportCompany')
        # 信用代码
        self.clear_set_input(settingContent, 3, 'reditCode')
        # 接口编码
        self.clear_set_input(settingContent, 5, 'interfaceCode')
        # 上传路径
        self.clear_set_input(settingContent, 7, 'uploadPath')
        # 下载路径
        self.clear_set_input(settingContent, 9, 'downloadPath')
        # 本级用户名称
        self.clear_set_input(settingContent, 11, 'selfLevelName')
        # 本级用户密码
        self.clear_set_input(settingContent, 13, 'selfLevelPwd')
        # 上级用户名称
        self.clear_set_input(settingContent, 15, 'upLevelName')
        # 上级用户密码
        self.clear_set_input(settingContent, 17, 'upLevelPwd')
        # 下发的SM2公钥
        self.clear_set_input(settingContent, 19, 'downloadSM2PublicKey')
        # 下发的SM4公钥
        self.clear_set_input(settingContent, 21, 'downloadSM4PublicKey')

    def clear_set_input(self, settingContent, index, key):
        self.driver.find_element_by_xpath(
            "//*[contains(text(),'报送单位')]/../following-sibling::div[" + str(index) + "]/span/input").clear()
        self.driver.find_element_by_xpath(
            "//*[contains(text(),'报送单位')]/../following-sibling::div[" + str(index) + "]/span/input").send_keys(
            settingContent[key])


#       save


if __name__ == '__main__':
    bean = SettingInfo()
    bean.set_config_info()
