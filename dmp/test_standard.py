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
    # def test_save_label_scope(self):
    #     test = DmpLogin()
    #     try:
    #         data = {"dimname": "dd", "dimcode": "dd", "descriptions": "test", "pid": "-1", "orderid": "1"}
    #         post = test.post_api("/labelDimension/saveTagDimension", json=data)
    #         util.info(post)
    #
    #     except Exception as e:
    #         util.info(e)

    def test_del_label_scope(self):
        test = DmpLogin()
        # try:
        data = {"dimname": "ddtest", "dimcode": "ddtest", "descriptions": "test", "pid": "-1", "orderid": "1"}
        postsave = test.post_api("/labelDimension/saveTagDimension", json=data)
        print(postsave)

        postsearch = test.get_api("/labelDimension/getDimensionListData",
                                   {"searchContent": "ddtest", "page": 1, "size": 20})
        print(postsearch)
        post = test.post_api("/labelDimension/deleteDimensionList", json=[postsearch['rows'][0]['ID']])
        util.info(post)
        # except Exception as e:
        #     print(e)
        #     util.info(e)
        assert postsave['code'] == '200'
        assert postsearch['total'] == 1
        assert post['code'] == '200'


    # def test_

if __name__ == '__main__':
    b = TestReport()
    b.test_del_label_scope()
    # test = DmpLogin()