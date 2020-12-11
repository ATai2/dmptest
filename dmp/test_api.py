#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/12/3 11:12
# software: PyCharm

import common.util as util
from common.GetSession import DmpLogin
import json
import pytest


# cases, list_params = util.get_test_data("data/test_setting.yml")


# 系统管理

class TestReport:

    def test_database(self):
        '''
        加工厂数据共享新建分类
        :return:
        '''
        test = DmpLogin()
        postsearch = test.get_api("/api/db/database")
        print(postsearch)
        assert postsearch['data']["databaseName"] == 'slkfjlesfjl失而复得'


if __name__ == '__main__':
    b = TestReport()
    b.test_database()
    # test = DmpLogin()
