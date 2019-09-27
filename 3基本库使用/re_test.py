#!/usr/bin/env python 
# -*- coding:utf-8 -*-

__author__ = 'kgy'

import re


def helloworld():
    content = 'Hello 123 4567 World_This is a Regex Demo'
    print(len(content))
    print(len('abc'))
    print(len('呵呵'))
    result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
    print(result)
    print(result.group())
    print(result.span())

def groupTest():
    content = 'Hello 1234567 World_This is a Regex Demo'
    result = re.match('^Hello\s(\d+)\sWorld',content)
    print(result)
    print(result.group())
    print(result.group(1))
    print(result.span())

if __name__ == '__main__':
    # helloworld()
    groupTest()