#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/5/26 14:33
# software: PyCharm
import requests

class Test(object):

    def test_health(self):
        data={
            'ip':'127.0.0.1',
            'port':'9001'
        }

        get = requests.get("http://127.0.0.1:8085/dmp-datafactory/health/getCpuRatioData")
        print(get.text)
        print('end')

    def test_upload_report(self):
        '''
        数据报送，用例更新
            数据准备：
            接口调用

        import:
        output:
        :return:
        '''






if __name__ == '__main__':
    bean=Test()
    bean.test_health()