#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/8/21 15:17
# software: PyCharm


import json, os, subprocess, time

from flask import Flask
from flask import request
from flask_cors import *
import logging
import logging.handlers
from shutil import copyfile, move

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


@app.route('/hello', methods=['get'])
def hell0():
    return "hellp"


@app.route('/start', methods=['get'])
def start():
    # req = request.data
    # data = json.loads(req)
    port = request.args.get("port")
    # 限定目录
    # location = data.get("location")
    try:
        if port != None:
            portstr = str(port)
            subpro = subprocessMap.get(port)
            if subpro is not None:
                # 杀掉子进程
                subpro.kill()
            # 干掉端口占用
            taskinfo = os.popen('netstat -ano | findstr %s' % str(port))
            try:
                line = taskinfo.readline()
                aList = line.split()
                taskinfo.close()
                pid = aList[4]
                os.popen('taskkill /pid %s /f' % pid)
            except Exception as e:
                print(e)
                logger.info("端口%s无占用" % port)
            # pathd = os.path.join(location, "startup-dmp.cmd")
            #
            if port == "8085":
                cmdPath = "D:\DMP\DMP2.4sqlserver8085\dmp\startup-dmp.cmd"
                subjavarun(cmdPath)
            elif port == "8081":
                cmdPath = "D:\DMP\DMP2.4sqlserver8081\dmp\startup-dmp.cmd"
                subjavarun(cmdPath)
            elif port == "9981":
                cmdPath = "D:\DMP\jenkinstestdmp\dmp\startup-dmp.cmd"
                child_process = subjavarun(cmdPath)
            else:
                logger.info("error port")
                child_process = None
            subprocessMap[portstr] = child_process
            return "ok"
        else:
            logger.info("端口号不能为空")
        return "fail"
    except Exception as e:
        return "error" + str(e)


def subjavarun(cmdPath):
    now = int(time.time())  # 1533952277
    timeArray = time.localtime(now)
    otherStyleTime = time.strftime("%Y-%m-%d-%H:%M:%S", timeArray)
    jarPath = os.path.join(os.path.dirname(cmdPath), "apps\\dmp-datafactory.jar")
    move(jarPath, jarPath + otherStyleTime)
    copyfile("D:\\jenkins\\apps\\dmp-datafactory.jar",
             os.path.join(os.path.dirname(cmdPath), "apps\\dmp-datafactory.jar"))
    child_process = subprocess.Popen(cmdPath)
    return child_process


if __name__ == '__main__':
    app.debug = True  # 设置调试模式，生产模式的时候要关掉debug
    app.run(host='0.0.0.0', port=10101)
