#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/5/29 9:00
# software: PyCharm

from flask_cors import *
from flask import Flask
from flask import request
import json, sys, os, socket, time, datetime
from threading import Timer
from flask_caching import Cache
from flask_apscheduler import APScheduler # 引入APScheduler

app = Flask(__name__)
CORS(app, supports_credentials=True, resources=r'/*')

cache = Cache()
app.config['CACHE_TYPE'] = 'simple'  # 本地缓存，一级缓存，缓存量大的情况下需使用二级缓存，一般使用redis
app.config['CACHE_DEFAULT_TIMEOUT'] = 24 * 60 * 60  # 默认过期时间 5分钟
cache.init_app(app)


@app.route('/getAgents', methods=['post'])
def getAgents():
    dbs = cache.get("dbs")
    if dbs != None:
        return dbs

    with open(os.path.join(os.path.join(os.path.dirname(__file__), "db"), "template.json"), "r+") as db:
        datas = db.read()
        dbs = json.loads(datas)
        cache.set("dbs", dbs)  # 把数据放入缓存
    return dbs


@app.route('/addAgent', methods=['post'])
def addAgent():
    host_name = request.data
    form = json.loads(host_name)
    dbs = {}
    with open(os.path.join(os.path.join(os.path.dirname(__file__), "db"), "template.json"), "r+") as db:
        datas = db.read()
        dbs = json.loads(datas)
    dbs['list'].append(form)

    dumps = json.dumps(dbs)
    with open(os.path.join(os.path.join(os.path.dirname(__file__), "db"), "template.json"), "w+") as dbw:
        dbw.write(dumps)

    return dbs


# http://前置服务器地址:8088/DataCollectorEnterpriseWeb/dataPushAction/uploadFile.do
@app.route('/DataCollectorEnterpriseWeb/dataPushAction/uploadFile.do', methods=['POST'])
def uploadFile():
    files = request.headers.get("files")
    charset = request.headers.get("Accept-Charset")
    type = request.headers.get("Content-Type")

    api = request.form.get("API_CODE")
    api = request.form.get("BUSINESS_TYPE")
    # 上传，上传到根目录

    return 'Hello World'


@app.route('/DataCollectorEnterpriseWeb/dataPushAction/downLoadFile.do', methods=['POST'])
def downLoadFile():
    # 文件下载， 从根目录取文件

    res = {
        "code": "1",
        "msg": "ok"
    }

    return res


def timerTask():
    print('TimeNow:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    t = Timer(5, freshDb)
    t.start()


def freshDb():
    print("定时任务begin")
    timestart=time.time()
    with open(os.path.join(os.path.join(os.path.dirname(__file__), "db"), "template.json"), "r+") as db:
        datas = db.read()
        dbs = json.loads(datas)
        for item in dbs['list']:
            # 查询服务状态
            try:
                sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sk.settimeout(2)
                sk.connect((str(item['hostName']), int(item['port'])))
                sk.close()
                now = time.strftime("%Y-%m-%d %H:%M:%S")
                print(now)
                # item['lastDeployTime']=now
                tt = "check port success!"
                item['status'] = 'up'
            except socket.error:
                item['status'] = 'down'
        cache.set("dbs", dbs)

        timeend=time.time()
        print("耗时："+str(timeend-timestart))


if __name__ == '__main__':
    timerTask()
    app.debug = True  # 设置调试模式，生产模式的时候要关掉debug
    app.run(port=8000)
