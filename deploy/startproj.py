#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/7/29 15:17
# software: PyCharm

import os, sys, re
import requests
import logging
import platform

import logging.handlers  # 日志滚动及删除使用

myapp = logging.getLogger()
myapp.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s: %(asctime)s %(filename)s %(message)s')
filehandler = logging.handlers.TimedRotatingFileHandler("myapp.log", when='d', interval=1,
                                                        backupCount=7)  # 每 1(interval) 天(when) 重写1个文件,保留7(backupCount) 个旧文件；when还可以是Y/m/H/M/S
filehandler.suffix = "%Y-%m-%d_%H-%M-%S.log"  # 设置历史文件 后缀
filehandler.setFormatter(formatter)
myapp.addHandler(filehandler)


def download_jar(url):
    '''
    下载jar包
    :param url:
    :return:
    '''
    down_res = requests.get(url=url)
    if down_res.status_code != 200:
        logging.info(url + "下载失败")
        return
    file_name = jar[jar.rfind("/") + 1:]
    print(file_name)
    with open(os.path.join(os.path.dirname(__file__), file_name), "w+") as f:
        for a in down_res.iter_content(chunk_size=32):  # iter是iter
            f.write(a)


def kill_old_process(port):
    '''
    关闭旧进程
    :return:
    '''
    if (platform.system() == 'Windows'):
        print('Windows系统')
        kill_windows_process(port)
    elif (platform.system() == 'Linux'):
        print('Linux系统')
        kill_linux_process(port)
    else:
        print('其他')


def kill_windows_process(port):
    with os.popen("netstat -nao|findstr " + str(port)) as res:
        res = res.read().split('\n')
    result = []
    for line in res:
        temp = [i for i in line.split(' ') if i != '']
        if len(temp) > 4:
            result.append({'pid': temp[4], 'address': temp[1], 'state': temp[3]})
    print(result)

    try:
        process_pid = result[0]['pid']
        os.popen('taskkill /pid ' + str(process_pid) + ' /F')
        print("端口已被释放")
    except:
        print("端口未被使用")


def kill_linux_process(port):
    command = '''kill -9 $(netstat -nlp | grep :''' + str(port) + ''' | awk '{print $7}' | awk -F"/" '{ print $1 }')'''
    os.system(command)

# test
if __name__ == '__main__':
    jar = "http://10.110.87.202:9998/a.log"
    # jar = "http://10.110.87.202:9998/dmp-datafactory.jar"
    jarPre = "http://10.110.87.202:9998/preposed-machine.jar"

    if len(sys.argv) == 1:
        print("no args")

    kill_old_process(8085)

    # download_jar(jar)

    # with open(os.path.join(os.path.dirname(__file__), "a.log"), "w+") as f:
    #     f.write("haha")
