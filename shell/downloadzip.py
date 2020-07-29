#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/7/29 14:54
# software: PyCharm

import paramiko
import scp
from paramiko import SSHClient
from scp import SCPClient
import sys, tarfile, os

ssh=SSHClient()
ssh.connect(hostname='',username='',password='')

def progress(filename,size,sent):
    sys.stdout.write("%s \'s progresss: %.2f%%     \r"%(filename,float(sent)/float(float(size))*100))

scp=SCPClient(ssh.get_transport(),progress=progress())
scp.get("")