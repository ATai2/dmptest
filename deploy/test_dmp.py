#!/usr/bin/env python
# -*- coding:utf-8 -*-
from unittest import TestCase

import paramiko
import requests
from bs4 import BeautifulSoup
import unittest

#
# class dmp_test(unittest.TestCase):
#
#     def runTest(self):
#         clientTrans = paramiko.Transport("localhost", 220))
#         clientTrans.connect(username="dmp", password="asdfasdf", port=220)
#         sftp = paramiko.SFTPClient.from_transport(clientTrans)
#         sftp.put("D:\\tools\\a.rp", "D:\\code\\")
#         clientTrans.close()
#
#         if __name__ == '__main__':
#             post = requests.post("http://localhost:8000/excute", json={
#                 "lastDeployTime": "2020-07-29 10:10:10",
#                 "hostName": "127.0.0.1",
#                 "port": "8080",
#                 "status": "up",
#                 "dir": "D:/data",
#                 "cmd": "pwd",
#                 "sshUserName": "dmp",
#                 "sshPassWord": "asdfasdf",
#                 "sshPort": "220",
#                 "jarFile": "premachine.jar"
#             })
#         print(post.text)
#         # soup = BeautifulSoup(post.text)
#         # for i in soup.find_all("li"):
#         #     item =i.text
#         #     print(item.replace("/",""))
#         # print(post.text)
from paramiko import AuthenticationException
import time

# hostname = "10.72.213.91"
# transport = paramiko.Transport((hostname, 220))
# # transport.connect(username='dmp', password="Ba@trInspur_6530")
# transport.connect(username='dmp', password="asdfasdf")
# sftp = paramiko.SFTPClient.from_transport(transport)
# put = sftp.put("D:\\tools\\a.rp", "D:\\code\\a.rp")
# transport.close()

#
# # python -m SimpleHTTPServer
# client = paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect(hostname="10.72.213.91", username="dmp", password="asdfasdf", port="220")
#
# channel = client.invoke_shell()
# channel.send('python -m SimpleHTTPServer 8080 \n')
# time.sleep(0.1)  # 这个延时必须要使用，要不然recv的内容中就不会含有ifconfig的内容
# output = channel.recv(2024)
# client.close()




# client = paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect(hostname="10.110.87.202", username="dmp", password="Ba@trInspur_6530", port="22")
#
# stdin, stdout, stderr = client.exec_command('ls -l')
# client.close()



# channel = client.invoke_shell()
# channel.send('python3 -m SimpleHTTPServer 7777 ')

# time.sleep(0.1)  # 这个延时必须要使用，要不然recv的内容中就不会含有ifconfig的内容
# output = channel.recv(2024)
# client.close()


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname="10.72.213.91", username="dmp", password="asdfasdf", port="220")

stdin, stdout, stderr = client.exec_command('cmd /c & python -m http.server 7777')
time.sleep(1)
read = stdout.read()
print(read)
client.close()









#
# class Test(TestCase):
#     def test_fresh_db(self):
#         # http://10.110.87.200:8912/
#         hostname = "10.110.87.202"
#         try:
#             transport = paramiko.Transport((hostname, 22))
#             transport.connect(username='dmp', password="Ba@trInspur_6530")
#             # transport.connect(username='dmp', password="asdfasdf")
#             sftp = paramiko.SFTPClient.from_transport(transport)
#             sftp.put("D:\\tools\\a.rp", "D:\\code\\a.rp")
#
#         except AuthenticationException as e:
#             return '主机%s密码错误' % (hostname)
#         except Exception as e:
#             return '未知错误: ', e
#         # else:
#             # sftp.put("D:\\tools\\a.rp", "D:\\code\\a.rp")
#             # sftp.get(source_name, target_name)
#         finally:
#             transport.close()
