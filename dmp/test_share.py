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
    res_dir_index = 0

    @pytest.mark.repeat(5)
    def test_resource_dir_add(self):
        test = DmpLogin()
        getCatalogListData = test.post_api("/catalogController/getCatalogListData")
        for item in getCatalogListData['rows']:
            if item['CLASSIFYCODE'] == 'ci':
                #         del
                deleteCatalog = test.post_api("/catalogController/deleteCatalog",
                                              json=[item['ID']])
                assert deleteCatalog['code'] == '200'

        postsearchci = test.post_api("/catalogController/addCatalogInfo",
                                     json={"classifyCode": "ci", "classifyName": "ci", "descriptions": "", "pid": "-1",
                                           "pName": "", "contactPerson": "", "phone": "", "mobilePhone": "",
                                           "email": "", "orderid": ""})
        assert postsearchci['code'] == '200'

    @pytest.mark.repeat(50)
    def test_resource_dir_add_batch(self):
        test = DmpLogin()
        postsearchci = test.post_api("/catalogController/addCatalogInfo",
                                     json={"classifyCode": "ci" + str(TestReport.res_dir_index),
                                           "classifyName": "ci" + str(TestReport.res_dir_index), "descriptions": "",
                                           "pid": "-1",
                                           "pName": "", "contactPerson": "", "phone": "", "mobilePhone": "",
                                           "email": "", "orderid": ""})
        TestReport.res_dir_index = TestReport.res_dir_index + 1
        assert postsearchci['code'] == '200'

    def test_saveGroup(self):
        '''
        加工厂数据共享新建分类
        :return:
        '''
        test = DmpLogin()

        postsearchci = test.post_api("/modeltree/getSearchNodeIDs",
                                     data={'rootID': 'iDF', 'searchText': 'ci'})
        if len(postsearchci) == 0:
            saveGroup = test.post_api("/group/saveGroup",
                                      json={"id": "", "pid": "234", "caption": "ci", "code": "ci", "type": "244",
                                            "content": "                        "})
        postdb = test.post_api("/dbConnPool/getDbConnPoolList",
                               data=None)
        postsearchci = test.post_api("/modeltree/getSearchNodeIDs",
                                     data={'rootID': 'iDF', 'searchText': 'ci'})
        postsearchcirepo = test.post_api("/modeltree/getSearchNodeIDs",
                                         data={'rootID': 'iDF', 'searchText': 'cirepo'})

        if len(postsearchcirepo) < 1:
            saveRepository = test.post_api("/repository/saveRepository",
                                           json={"id": None, "caption": "cirepo", "code": "cirepo",
                                                 "nodePid": postsearchci[0], "nodeType": "253",
                                                 "dbcpId": postdb[0]['DBCP_ID'], "dbType": "3",
                                                 "description": "", "division": "", "industry": "", "leaddept": "",
                                                 "impldept": ""})

            assert saveRepository['ID'] != None


if __name__ == '__main__':
    b = TestReport()
    b.test_resource_dir_add()
    # test = DmpLogin()
