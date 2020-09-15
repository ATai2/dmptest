#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/8/19 14:25
# software: PyCharm


import pymssql
import os, re, json


def get_sql_files(absdbfilePath):
    sql_files = []
    # abspath = os.path.abspath("D:\doc\BA-DMP-DOC\项目管理\数据管理平台202009\\03数据库设计\\01DMP202009全量sql\Sqlserver\ddl")
    abspath = absdbfilePath
    dirpath = abspath
    files = os.listdir(abspath)
    # files = os.listdir(os.path.dirname(os.path.abspath(__file__)))
    for file in files:
        if os.path.splitext(file)[1] == '.sql':
            sql_files.append(os.path.join(dirpath, file))
    return sql_files


def connectSQL(absdbfilePath, db):
    # 打开数据库连接
    db = pymssql.connect(server=db['host'], user=db['username'], password=db['pwd'], database=db['database'])
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    for file in get_sql_files(absdbfilePath):
        print("开始执行文件：" + file)
        executeScriptsFromFile(file, cursor)
    # executeScriptsFromFile("D:\code\dmptest\sql\(08)DASX_mss_ddl.sql", cursor)
    db.close()


def executeScriptsFromFile(filename, cursor):
    fd = open(filename, 'r', encoding='utf-8')
    sqlFile = fd.read()
    fd.close()
    sqlFile = sqlFile.replace("GO\n", "go\n")
    pattern = re.compile(r'GO[ ]+')
    sqlFile = re.sub(pattern, "go", sqlFile)

    sqlCommands = sqlFile.split('go\n')

    for command in sqlCommands:
        print("==========================")

        if command.endswith("GO") or command.endswith("go"):
            command = command[:-2]
        print(command)
        try:
            command = command.strip()
            if command.endswith("\n"):
                command.replace("\n","")
            execute = cursor.execute(command)
            print("OK")
        except Exception as msg:

            print("error: " + str(msg))
    print('sql执行完成')


def cycle_db(path):
    path_join = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dbinfo.json")
    with open(path_join, "r") as f:
        content = f.read()
        dbinfo = json.loads(content)
        dblist = dbinfo['mssql']
        for item in dblist:
            connectSQL(path, item)


if __name__ == '__main__':
    cycle_db("D:\doc\BA-DMP-DOC\项目管理\数据管理平台202009\\03数据库设计\\01DMP202009全量sql\Sqlserver\ddl")
    cycle_db("D:\doc\BA-DMP-DOC\项目管理\数据管理平台202009\\03数据库设计\\01DMP202009全量sql\Sqlserver\dml")
