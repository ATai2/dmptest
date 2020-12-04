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
    # test = DmpLogin()
    @pytest.mark.repeat(50)
    def test_modeltree(self):
        test = DmpLogin()
        data = {"id": "DAST"}
        post = test.post_api("/modeltree/getChildNode", data=data)
        assert len(post) > 0

    @pytest.mark.repeat(50)
    def test_getRootAndDirectChildNodeiDM(self):
        test = DmpLogin()
        postsearch = test.post_api("/modeltree/getRootAndDirectChildNode",
                                   data={"id": "iDM"})
        print(postsearch)
        assert len(postsearch) > 0

    @pytest.mark.repeat(50)
    def test_getRootAndDirectChildNodeDATS(self):
        test = DmpLogin()
        postsearch = test.post_api("/modeltree/getRootAndDirectChildNode",
                                   data={"id": "DATS"})
        print(postsearch)
        assert len(postsearch) > 0

    @pytest.mark.repeat(50)
    def test_getIdiEtlShow(self):
        test = DmpLogin()
        postsearch = test.get_api("/trans/getIdiEtlShow")
        print(postsearch)

    @pytest.mark.repeat(50)
    def test_getSettingData(self):
        test = DmpLogin()
        postsearch = test.get_api("/gzapi/getSettingData")
        print(postsearch)


if __name__ == '__main__':
    b = TestReport()
    b.test_modeltree()
    # test = DmpLogin()
