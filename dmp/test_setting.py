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
    # @pytest.mark.parametrize("case,data,expected", list(list_params), ids=cases)
    def test_save_settingdata(self):
        test = DmpLogin()
        post = test.post_api(
            "/slaveServer/saveSlaveServer?name=kettle&hostName=127.0.0.1&port=8080&webAppName=&username=CeNTILgC6rOizgrFBjPCQQ%3D%3D&password=CeNTILgC6rOizgrFBjPCQQ%3D%3D&idSlave=&master=0",
            data=None)
        util.info(post)
        assert post['rs'] == '1'


