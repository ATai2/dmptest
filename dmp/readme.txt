1. 下载chromedriver.exe到chrome安装目录（注意版本）
2. 安装类库
pip install -U pytest  pytest-html   pytest-repeat  selenium

3. 编写用例与执行
py.test test_report.py --html=./report.html

4. 若调试环境应用未能有效关闭：
taskkill /f /t /im chrome.exe
taskkill /f /t /im chromedriver.exe


pytest-xdist可以并发执行测试用例，来提升测试用例的执行速度