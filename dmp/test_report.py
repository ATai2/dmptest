#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/12/3 11:12
# software: PyCharm

import common.util as util
from common.GetSession import DmpLogin
import json
import pytest

cases, list_params = util.get_test_data("data/test_report.yml")


class TestReport:
    @pytest.mark.parametrize("case,data,expected", list(list_params), ids=cases)
    def test_save_settingdata(self, case, data, expected):
        test = DmpLogin()
        setting_data = test.getSettingData()
        try:
            setting = json.loads(setting_data)
            data['id'] = setting['data']['basicInfoMap']['id']
            post = test.post_api("/gzapi/save", data=data)
            print(post)
        except Exception as e:
            print(e)
            post = test.post_api("/gzapi/save", data=data)
            print(post)

        assert json.loads(post)['rs'] == expected['rs']


print(list_params)
