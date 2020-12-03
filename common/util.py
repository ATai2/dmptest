#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/12/3 13:15
# software: PyCharm

import yaml, os, re
import logging
from logging.handlers import TimedRotatingFileHandler

from logging import handlers

logger = logging.getLogger()
# format = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
# rotahandler = handlers.RotatingFileHandler(os.path.join('root’, 'logs/my'), maxBytes=1024 * 1024 * 100)
# rotahandler = handlers.TimedRotatingFileHandler(os.path.join('../logs.log'), when='D')
# rotahandler.setLevel(logging.DEBUG)
# rotahandler.setFormatter(format)

file_handler = TimedRotatingFileHandler(filename='../logs', when="MIDNIGHT", interval=1, backupCount=30)
# filename="mylog" suffix设置，会生成文件名为mylog.2020-02-25.log
file_handler.suffix = "%Y-%m-%d.log"
# extMatch是编译好正则表达式，用于匹配日志文件名后缀
# 需要注意的是suffix和extMatch一定要匹配的上，如果不匹配，过期日志不会被删除。
file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")
# 定义日志输出格式
file_handler.setFormatter(
    logging.Formatter(
        "[%(asctime)s] [%(process)d] [%(levelname)s] - %(module)s.%(funcName)s (%(filename)s:%(lineno)d) - %(message)s"
    )
)



console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(format)

logger.addHandler(file_handler)
logger.addHandler(console)


def info(msg):
    logger.info(msg)


def get_test_data(test_data_path):
    case = []  # 存储测试用例名称
    data = []  # 存储请求对象
    expected = []  # 存储预期结果
    with open(test_data_path, "r", encoding='utf-8') as f:
        dat = yaml.load(f.read(), Loader=yaml.SafeLoader)
        test = dat['tests']
        for td in test:
            case.append(td.get('case', ''))
            data.append(td.get('data', {}))
            expected.append(td.get('expected', {}))
    parameters = zip(case, data, expected)
    return case, parameters


# cases, parameters = get_test_data("../dmp/data/test_report.yml")
# list_params = list(parameters)
# print(list_params)
