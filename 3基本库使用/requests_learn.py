#!/usr/bin/env python 
# -*- coding:utf-8 -*-

__author__ = 'kgy'

import requests


def helloworld():
    r = requests.get('https://www.baidu.com')
    print(type(r))
    print(r.status_code)
    print(type(r.text))
    print(r.text)
    print(r.cookies)


def get():
    r = requests.get('http://httpbin.org/get')
    print(r.text)

    data = {
        'name': 'germey',
        'age': 22
    }
    r = requests.get('http://httpbin.org/get', params=data)
    print(type(r.text))
    print(r.text)
    print(r.json())
    print(type(r.json()))


def getPage():
    import re
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    r = requests.get("https://www.zhihu.com/explore", headers=headers)
    pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
    print(r.text)
    titles = re.findall(pattern, r.text)
    print(titles)


def getIco():
    r = requests.get("https://github.com/favicon.ico")
    with open('favicon.ico', 'wb') as f:
        f.write(r.content)


def session():
    s = requests.Session()
    s.get('http://httpbin.org/cookies/set/number/123456789')
    r = s.get('http://httpbin.org/cookies')
    print(r.text)


def prepared_request():
    from requests import Request, Session
    url = 'http://httpbin.org/post'
    data = {
        'name': 'germey'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    s = Session()
    req = Request('POST', url, data=data, headers=headers)
    prepped = s.prepare_request(req)
    r = s.send(prepped)
    print(r.text)


if __name__ == '__main__':
    # helloworld()
    # get()
    # getPage()
    # getIco()
    # session()
    prepared_request()