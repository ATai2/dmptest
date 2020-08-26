#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/8/21 14:12
# software: PyCharm


import subprocess, time, sys


def startSim(port):
    import os
    taskinfo = os.popen('netstat -ano | findstr %s' % str(port))
    try:
        line = taskinfo.readline()
        aList = line.split()
        taskinfo.close()
        pid = aList[4]
        os.popen('taskkill /pid %s /f' % pid)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    if len(sys.argv) > 0:
        startSim(sys.argv[0])
    else:
        startSim(8085)
