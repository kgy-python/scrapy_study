#!/usr/bin/env python 
# -*- coding:utf-8 -*-

__author__ = 'kgy'

import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

html = requests.get(url,headers=headers).text
doc = pq(html)
items = doc('.ExploreHomePage-specials .ExploreSpecialCard').items()
for item in items:
    question = item.find('.ExploreSpecialCard-title').text()
    author = item.find('.ExploreSpecialCard-count').text()
    file = open('explore.txt','a',encoding='utf-8')
    file.write('\n'.join([question,author]))
    file.write('\n' + '=' * 50 + '\n')
    file.close()