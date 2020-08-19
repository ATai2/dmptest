#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/8/19 14:25
# software: PyCharm


import pymssql
import os, re


def get_sql_files():
    sql_files = []
    abspath = os.path.abspath("D:\doc\BA-DMP-DOC\项目管理\数据管理平台202009\\03数据库设计\\01DMP202009全量sql\Sqlserver\ddl")
    dirpath = abspath
    files = os.listdir(abspath)
    # files = os.listdir(os.path.dirname(os.path.abspath(__file__)))
    for file in files:
        if os.path.splitext(file)[1] == '.sql':
            sql_files.append(os.path.join(dirpath, file))
    return sql_files


def connectSQL():
    # 打开数据库连接
    db = pymssql.connect(server="localhost", user="SA", password="asdfF@1234", database="paas")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    for file in get_sql_files():
        print("开始执行文件：" + file)
        executeScriptsFromFile(file, cursor)

    # executeScriptsFromFile("D:\code\dmptest\sql\(08)DASX_mss_ddl.sql", cursor)
    db.close()


def executeScriptsFromFile(filename, cursor):
    fd = open(filename, 'r', encoding='utf-8')
    sqlFile = fd.read()
    fd.close()
    sqlFile = sqlFile.replace("GO\n", "go")
    pattern = re.compile(r'GO[ ]+')
    sqlFile = re.sub(pattern, "go", sqlFile)

    sqlCommands = sqlFile.split('go')

    for command in sqlCommands:
        print("==========================")
        print(command)
        try:
            if command.endswith("GO"):
                command = command.replace("GO", "")
                command = command.replace("go", "")
            cursor.execute(command)
            print("OK")
        except Exception as msg:
            print(msg)
    print('sql执行完成')


if __name__ == '__main__':
    connectSQL()
