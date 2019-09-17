#!/usr/bin/env python 
# -*- coding:utf-8 -*-

__author__ = 'kgy'

from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener

proxy_handler = ProxyHandler({
    'http' : 'http://163.125.112.169:8118'
})

opener = build_opener(proxy_handler)
try:
    response = opener.open('https://www.baidu.com')
    print(response.read().decode('utf-8'))
    print(response.status)
    print(response.getheaders())
    print(response.getheader('Server'))
except URLError as e:
    print(e.reason)