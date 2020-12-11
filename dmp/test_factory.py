#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/12/3 11:12
# software: PyCharm

from dmp.GetSession import DmpLogin


# cases, list_params = util.get_test_data("data/test_setting.yml")


# 系统管理

class TestReport:

    def test_saveGroup(self):
        '''
        加工厂数据共享新建分类
        :return:
        '''
        test = DmpLogin()
        postsearch = test.post_api("/group/saveGroup",
                               json={"id": "", "pid": "234", "caption": "ci", "code": "ci", "type": "244",
                                     "content": "                        "})
        print(postsearch)
        # assert postsearch['total'] >= 10




if __name__ == '__main__':
    b = TestReport()
    b.test_del_label_scope()
    # test = DmpLogin()
