#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/5/29 9:00
# software: PyCharm

import datetime
import json
import os
import requests
import socket
import sys
import time
from threading import Timer

import paramiko
from apscheduler.schedulers.background import BackgroundScheduler
from bs4 import BeautifulSoup
from flask import Flask
from flask import request
from flask_caching import Cache
from flask_cors import *

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


@app.route('/getJars', methods=['post'])
def getJars():
    '''
    更改文件服务器
    :return:
    '''
    post = requests.get("http://10.110.87.202:9998")
    soup = BeautifulSoup(post.text)
    res = {"list": []}
    for i in soup.find_all("li"):
        item = i.text
        res['list'].append(item)
    return res


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


@app.route('/excute', methods=['post'])
def excute():
    host_name = request.data
    form = json.loads(host_name)

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=form['hostName'], username="dmp", password="asdfasdf", port="220")

    channel = client.invoke_shell()
    channel.send(form['cmd'] + '\n')
    time.sleep(0.1)  # 这个延时必须要使用，要不然recv的内容中就不会含有ifconfig的内容
    output = channel.recv(2024)


    # output=channel.recv(2024).decode('utf-8')
    print(output)
    # Close the connection
    client.close()
    print('Connection closed.')

    # clientTrans = paramiko.Transport((form['hostName'],220))
    # clientTrans.connect(username="dmp", password="asdfasdf", port=220)
    # sftp = paramiko.SFTPClient.from_transport(clientTrans)
    # sftp.put("D:\\tools\\a.rp", form["dir"])
    # clientTrans.close()

    return "dbs"


def freshDb():
    print("定时任务begin")
    timestart = time.time()
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

        timeend = time.time()
        print("耗时：" + str(timeend - timestart))


if __name__ == '__main__':
    # scheduler = BackgroundScheduler()
    # scheduler.add_job(freshDb, 'interval', seconds=10)  # 间隔3秒钟执行一次
    # scheduler.start()  # 这里的调度任务是独立的一个线程
    app.debug = True  # 设置调试模式，生产模式的时候要关掉debug
    app.run(port=8000)
