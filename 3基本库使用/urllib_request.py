#!/usr/bin/env python 
# -*- coding:utf-8 -*-

__author__ = 'kgy'

import urllib.request

request = urllib.request.Request('https://www.baidu.com/')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))

from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE S. S; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germey'
}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))

