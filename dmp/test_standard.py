#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/12/3 11:12
# software: PyCharm

import common.util as util
from dmp.GetSession import DmpLogin


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

    #  标签维度查询
    def test_label_scope(self):
        test = DmpLogin()
        postsearch = test.get_api("/labelDimension/getDimensionListData",
                                  { "page": 1, "size": 20})
        print(postsearch)
        assert postsearch['total']>=10

    # 标签维度添加，查询，删除
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

    def test_lable_search_private_info(self):
        test = DmpLogin()
        postsearch = test.get_api("/labelDimension/getDimensionListData",
                                  {"searchContent": "ddtest", "page": 1, "size": 20})
        print(postsearch)

    def test_lable_search_private_info_del(self):
        test = DmpLogin()
        postsearch = test.get_api("/tagManagement/addTagInfo",
                                  {"searchContent": "ddtest", "page": 1, "size": 20})
        print(postsearch)



    # def test_

if __name__ == '__main__':
    b = TestReport()
    b.test_del_label_scope()
    # test = DmpLogin()