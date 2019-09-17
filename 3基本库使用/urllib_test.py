#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import socket

__author__ = 'kgy'

import urllib.request

response = urllib.request.urlopen('http://c.biancheng.net/view/2406.html')

print(response.read().decode('utf-8'))

print(type(response))
print(dir(response))
# print(response.__all__)
print([e for e in dir(response) if not e.startswith('_')])
print(urllib.request.__file__)
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))

print('*' * 30)
import urllib.parse
import urllib.error

try:
    data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
    response = urllib.request.urlopen('http://httpbin.org/post', data=data, timeout=1)
    print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
