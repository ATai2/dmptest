#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/5/29 9:00
# software: PyCharm

import json

from flask import Flask
from flask import request
from flask_cors import *

app = Flask(__name__)
CORS(app, supports_credentials=True, resources=r'/*')


@app.route('/excute', methods=['post'])
def excute():
    host_name = request.data
    form = json.loads(host_name)


    return "ok"


if __name__ == '__main__':
    app.debug = True  # 设置调试模式，生产模式的时候要关掉debug
    app.run(port=10100)
