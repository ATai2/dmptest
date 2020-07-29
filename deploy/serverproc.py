#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/7/29 18:13
# software: PyCharm
import time

import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname="10.72.213.91", username="dmp", password="asdfasdf" ,port="220")

channel = client.invoke_shell()
# channel.send('cd /usr/local\n')
# time.sleep(3)
# channel.send('mkdir aa\n')
channel.send('ipconfig\n')
time.sleep(0.1) # 这个延时必须要使用，要不然recv的内容中就不会含有ifconfig的内容
output=channel.recv(2024)
# output=channel.recv(2024).decode('utf-8')
print(output)
#Close the connection
client.close()
print('Connection closed.')


