#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests

if __name__ == '__main__':

    post = requests.post("http://localhost:8000/getAgents")

    print(post.text)
