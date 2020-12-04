#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/12/3 15:05
# software: PyCharm


import os, pytest

if __name__ == '__main__':
    pytest.main(["--html=./report.html"])
    # pytest.main(["--count=10", "--html=./report.html"])
    # os.system("py.test  --html=./report.html")
    # os.system("py.test test_report.py --html=./report.html")
    # os.system("py.test test_setting.py --html=./report.html")
    # os.system("py.test test_standard.py --html=./report.html")
    # os.system("py.test test_standard.py::TestReport::test_del_label_scope --html=./report.html")

    # pytest.main(["test_anhui.py", "--html=./report.html"])
