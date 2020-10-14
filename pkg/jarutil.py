#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/9/29 17:48
# software: PyCharm

import os
import hashlib
import shutil
import zipfile, time


def get_file_md5(file):
    md5_l = hashlib.md5()
    with open(file, mode="rb") as f:
        by = f.read()

    md5_l.update(by)
    ret = md5_l.hexdigest()
    # print(ret)
    return ret


def unpack_jar(path):
    zfile = zipfile.ZipFile(path, 'r')
    jarlog_ = os.getcwd() + '/jarlog'
    if not os.path.exists(jarlog_):
        # shutil.rmtree(jarlog_)
        os.makedirs(os.getcwd() + '/jarlog/')
    outPath = jarlog_ + "/" + str(time.time())
    zfile.extractall(outPath)
    return outPath


def ite_file_md5(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            # 获取文件所属目录
            # print(root)
            # 获取文件路径
            path_join = os.path.join(root, file)
            print(path_join)
            print(get_file_md5(path_join))


def compare_jar_class_file(jar1, jar2):
    path1 = unpack_jar(jar1)
    path2 = unpack_jar(jar2)

    for root, dirs, files in os.walk(path1):
        for file in files:
            # 获取文件所属目录
            # print(root)
            # 获取文件路径
            path_join1 = os.path.join(root, file)
            path_join2 = os.path.join(path2, file)

            print(path_join1)
            print(get_file_md5(path_join1))
            if get_file_md5(path_join1) == get_file_md5(path_join2):
                print("equals")



if __name__ == '__main__':
    compare_jar_class_file('D:\code\dmptest\pkg\wordcount-1.0-SNAPSHOT.jar','D:\code\dmptest\pkg\wordcount-2.0-SNAPSHOT.jar')
