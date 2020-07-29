#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    post = requests.get("http://localhost:8080")
    soup = BeautifulSoup(post.text)
    for i in soup.find_all("li"):
        item =i.text
        print(item.replace("/",""))
    print(post.text)
