#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/12/3 13:15
# software: PyCharm

import yaml

def get_test_data(test_data_path):
    case = []  # 存储测试用例名称
    data = []  # 存储请求对象
    expected = []  # 存储预期结果
    with open(test_data_path,"r",encoding='utf-8') as f:
        dat = yaml.load(f.read(), Loader=yaml.SafeLoader)
        test = dat['tests']
        for td in test:
            case.append(td.get('case', ''))
            data.append(td.get('data', {}))
            expected.append(td.get('expected', {}))
    parameters = zip(case, data, expected)
    return case, parameters

cases, parameters = get_test_data("../dmp/data/test_report.yml")
list_params=list(parameters)
print(list_params)