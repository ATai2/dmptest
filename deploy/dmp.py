#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/5/29 9:00
# software: PyCharm

from flask_cors import *
from flask import Flask
from flask import request
import json, sys, os

app = Flask(__name__)
CORS(app, supports_credentials=True,resources=r'/*')

@app.after_request
def cors(environ):
    environ.headers['Access-Control-Allow-Origin']='*'
    environ.headers['Access-Control-Allow-Method']='*'
    environ.headers['Access-Control-Allow-Headers']='x-requested-with,content-type'
    return environ

# http://前置服务器地址:8088/DataCollectorEnterpriseWeb/dataPushAction/uploadFile.do
@app.route('/getAgents', methods=['post'])
def getAgents():
    dbs = []
    with open(os.path.join(os.path.join(os.path.dirname(__file__), "db"), "template.json"), "r+") as db:
        datas = db.read()
        dbs = json.loads(datas)

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


if __name__ == '__main__':
    app.debug = True  # 设置调试模式，生产模式的时候要关掉debug
    app.run(port=8000)
