#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/8/19 14:25
# software: PyCharm


import cx_Oracle
import os, re, sys, json

cx_Oracle.init_oracle_client(lib_dir=r"D:\tools\instantclient_19_8")


def get_sql_files(absdbfilePath):
    sql_files = []
    # abspath = os.path.abspath(os.path.join(absdbfilePath,"Sqlserver\ddl"))
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
    db = cx_Oracle.connect("%s/%s@%s/%s" % (db['username'], db['pwd'], db['host'], db['database']))

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    for file in get_sql_files(absdbfilePath):
        print("开始执行文件：" + file)
        executeScriptsFromFile(file, cursor)

    # executeScriptsFromFile("D:\code\dmptest\sql\(08)DASX_mss_ddl.sql", cursor)
    db.close()


def executeScriptsFromFile(filename, cursor):
    sqlFile = ''
    with  open(filename, 'r', encoding='utf-8') as fd:
        listlines = fd.readlines()
        for item in listlines:
            if item.strip() == "/":
                continue
            sqlFile = sqlFile + item
    # oracle 整体执行

    for command in [sqlFile]:
        print("==========================")
        print(command)
        try:
            cursor_execute = cursor.execute(command)
            print(cursor_execute)
            print("OK")
        except Exception as msg:
            print(msg)
    print('sql执行完成')


def cycle_db(path):
    path_join = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dbinfo.json")
    with open(path_join, "r") as f:
        content = f.read()
        dbinfo = json.loads(content)
        dblist = dbinfo['oracle']
        for item in dblist:
            connectSQL(path, item)


if __name__ == '__main__':
    # cycle_db("D:\doc\BA-DMP-DOC\项目管理\数据管理平台202009\\03数据库设计\\01DMP202009全量sql\Oracle\ddl")
    # cycle_db("D:\doc\BA-DMP-DOC\项目管理\数据管理平台202009\\03数据库设计\\01DMP202009全量sql\Oracle\dml")
    sql = '''
 declare
      num int :=0;
begin

	select count(1) into num from R_LOGLEVEL ;
	if(num <= 0 ) then
		execute immediate ( 'INSERT INTO R_LOGLEVEL VALUES (''1'', ''Error'', ''错误日志'')');

		execute immediate ( 'INSERT INTO R_LOGLEVEL VALUES (''2'', ''Minimal'', ''最小日志'')');

		execute immediate ( 'INSERT INTO R_LOGLEVEL VALUES (''3'', ''Basic'', ''基本日志'')');

		execute immediate ( 'INSERT INTO R_LOGLEVEL VALUES (''4'', ''Detailed'', ''详细日志'')');

		execute immediate ('INSERT INTO R_LOGLEVEL VALUES (''5'', ''Debug'', ''调试'')');

		execute immediate ( 'INSERT INTO R_LOGLEVEL VALUES (''6'', ''Rowlevel'', ''行级日志(非常详细)'')');
	end if;
end;
    '''
    path_join = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dbinfo.json")
    with open(path_join, "r") as f:
        content = f.read()
        dbinfo = json.loads(content)
        dblist = dbinfo['oracle']
        db=dblist[0]
        db = cx_Oracle.connect("%s/%s@%s/%s" % (db['username'], db['pwd'], db['host'], db['database']))

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        execute = cursor.execute(sql)
        print(execute)
    except Exception as e:
        print(e)
    db.close()
