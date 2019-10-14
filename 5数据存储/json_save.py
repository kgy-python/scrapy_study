#!/usr/bin/env python 
# -*- coding:utf-8 -*-

__author__ = 'kgy'

import json

str = '''
[{
    "name":"Bob",
    "gender":"male",
    "birthday":"1992-10-18"
},{
    "name":"selina",
    "gender":"female",
    "birthday":"1992-10-18"
}]
'''
print(type(str))
data = json.loads(str)
print(data)
print(type(data))

with open('data.json','w') as file:
    file.write(json.dumps(data,indent=2))