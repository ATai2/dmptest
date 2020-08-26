#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/8/21 15:17
# software: PyCharm

from subprocess import Popen, PIPE, STDOUT
import json, os, subprocess

from flask import Flask
from flask import request
from flask_cors import *
import logging
import logging.handlers

LOG_FILE = 'app.log'

handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=5)  # 实例化handler
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'

formatter = logging.Formatter(fmt)  # 实例化formatter
handler.setFormatter(formatter)  # 为handler添加formatter

logger = logging.getLogger('app')  # 获取名为tst的logger
logger.addHandler(handler)  # 为logger添加handler
logger.setLevel(logging.DEBUG)
app = Flask(__name__)
CORS(app, supports_credentials=True, resources=r'/*')

subprocessMap = {}

pathd = os.path.join(os.path.dirname(__file__), "a.bat")
child_process = subprocess.Popen(pathd)

p = Popen("start cmd /c a.bat", stdout=PIPE, stderr=STDOUT)





# @app.route('/hello', methods=['get'])
# def hell0():
#     return "hellp"
#
#
# @app.route('/start', methods=['post'])
# def start():
#     req = request.data
#     data = json.loads(req)
#     port = data.get("port")
#     location = data.get("location")
#     if port != None:
#         portstr = str(port)
#         subpro = subprocessMap[portstr]
#         if subpro is not None:
#             # 杀掉子进程
#             subpro.kill()
#             # 干掉端口占用
#             taskinfo = os.popen('netstat -ano | findstr %s' % str(port))
#             try:
#                 line = taskinfo.readline()
#                 aList = line.split()
#                 taskinfo.close()
#                 pid = aList[4]
#                 os.popen('taskkill /pid %s /f' % pid)
#             except Exception as e:
#                 print(e)
#                 logger.info("端口%s无占用" % port)
#         pathd = os.path.join(location, "startup-dmp.cmd")
#         child_process = subprocess.Popen(pathd)
#         subprocessMap[portstr] = child_process
#         return "ok"
#     else:
#         logger.info("端口号不能为空")
#     return "fail"
#
#
# if __name__ == '__main__':
#     app.debug = True  # 设置调试模式，生产模式的时候要关掉debug
#     app.run(port=10100)
