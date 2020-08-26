#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/8/21 14:12
# software: PyCharm


import subprocess, time, os


def startSim():
    pathd = os.path.join(os.path.dirname(__file__), "startup-dmp.cmd")
    child_process = subprocess.Popen(pathd)


if __name__ == '__main__':
    startSim()
