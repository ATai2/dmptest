#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/10/14 10:21
# software: PyCharm

import json,time
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
        self.login.loginOneStation("wth", "admin@123")
        time.sleep(2)
        self.driver.implicitly_wait(5)
        self.driver.get("http://10.110.87.200:8912/dmp/dmp-datafactory/mainFrame?id=DATS")
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath("//*[contains(text(),'配置信息')]").click()
        time.sleep(3)
        name = self.driver.find_element_by_tag_name("iframe")
        self.driver.switch_to.frame(name)

        #  read config file
        with open('report_setting.json', 'r', encoding='utf-8') as f:
            content = f.read()
        setting_content = json.loads(content)

        #         set data
        # 报送单位
        self.clear_set_input(setting_content, 'reportAgency')
        # 信用代码
        self.clear_set_input(setting_content, 'socialCreditCode')
        # 接口编码
        self.clear_set_input(setting_content, 'apiCode')
        # 上传路径
        self.clear_set_input(setting_content, 'uploadPath')
        # 下载路径
        self.clear_set_input(setting_content, 'downLoadPath')
        # 本级用户名称
        self.clear_set_input(setting_content, 'userName')
        # 本级用户密码
        self.clear_set_input(setting_content, 'userPasswd')
        # 上级用户名称
        self.clear_set_input(setting_content, 'preUserName')
        # 上级用户密码
        self.clear_set_input(setting_content, 'preUserPasswd')
        # 下发的SM2公钥
        self.clear_set_input(setting_content, 'SM2Key')
        # 下发的SM4公钥
        self.clear_set_input(setting_content, 'uploadUrl')
        self.clear_set_input(setting_content, 'catalogUrl')
        self.clear_set_input(setting_content, 'noticeUrl')
        self.clear_set_input(setting_content, 'keyUrl')
        self.clear_set_input(setting_content, 'taskUrl')
        self.clear_set_input(setting_content, 'logUrl')
        self.clear_set_input(setting_content, 'acceptDataUrl')


        self.clear_set_input(setting_content, 'preCatalogUrl')
        self.clear_set_input(setting_content, 'preNoticeUrl')
        self.clear_set_input(setting_content, 'preKeyUrl')
        self.clear_set_input(setting_content, 'preTaskUrl')
        self.clear_set_input(setting_content, 'preDataUrl')
        self.clear_set_input(setting_content, 'preStatusUrl')
        self.clear_set_input(setting_content, 'prePointConnUrl')

    def clear_set_input(self, settingContent, name):
        self.driver.find_element_by_name(name).clear()
        self.driver.find_element_by_name(name).send_keys(settingContent[name])

        # self.driver.find_element_by_xpath(
        #     "//*[contains(text(),'报送单位')]/../following-sibling::div[" + str(index) + "]/span/input").clear()
        # self.driver.find_element_by_xpath(
        #     "//*[contains(text(),'报送单位')]/../following-sibling::div[" + str(index) + "]/span/input").send_keys(
        #     settingContent[key])


#       save


if __name__ == '__main__':
    bean = SettingInfo()
    bean.set_config_info()
