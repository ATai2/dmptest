#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/12/3 15:05
# software: PyCharm

import pytest, sys
from GetSession import DmpLogin
print(sys.path)

if __name__ == '__main__':
    arglengh = len(sys.argv)
    print(arglengh)
    if arglengh == 1:
        arg1 = None
        ip = None
    elif arglengh == 2:
        arg1 = sys.argv[1]
        ip = None
    elif arglengh == 3:
        arg1 = sys.argv[1]
        ip = sys.argv[2]

    if ip == None:
        ip = "localhost"

    if arg1 == "remote":
        dmplist = {
            "dm": "9001",
            "ms": "9002",
            "my8": "9003",
            "my57": "9004",
            "orc": "9005",
            "oscar": "9006",
            "pg": "9007",
        }
        for k in dmplist:
            Config.url = "http://" + ip + ":" + dmplist[k]
            print(Config.url)
            DmpLogin.cookieStr=None
            # pytest.main(["-v", "--html=../" + k + "report.html"])
            pytest.main(["test_setting.py","-v", "--html=./" + k + "report.html"])
    else:
        pytest.main(["-v", "--html=./report.html"])

    # 2 并发执行
    # pytest.main(["-n 2","--html=./report.html"])
    # pytest.main(["test_setting.py::TestReport::test_save_settingdata","-v",   "--html=./report.html"])
    # pytest.main(["test_share.py::TestReport::test_resource_dir_add_batch","-v",   "--html=./report.html"])

    # pytest.main(["-v", "-n 2", "--html=./report.html"])
    # pytest.main(["--count=10", "--html=./report.html"])
    # os.system("py.test  --html=./report.html")
    # os.system("py.test test_report.py --html=./report.html")
    # os.system("py.test test_setting.py --html=./report.html")
    # os.system("py.test test_standard.py --html=./report.html")
    # os.system("py.test test_standard.py::TestReport::test_del_label_scope --html=./report.html")

    # pytest.main(["test_anhui.py", "--html=./report.html"])
