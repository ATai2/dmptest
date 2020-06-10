#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangtaihe
# datetime:2020/6/10 13:44
# software: PyCharm

import requests


def restPost(url, data=None, json=None, headers=None):
    post = requests.post(url, data=data, json=json, headers=headers)
    if post.status_code == 200:
        print(post.text)
        return post.text
    else:
        print("post error")