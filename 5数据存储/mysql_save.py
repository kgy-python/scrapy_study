#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import traceback

__author__ = 'kgy'

import pymysql

id = '20120001'
user = 'Bob'
age = 20

# db = pymysql.connect(host='localhost', user='root', password='root', port=3307)
# cursor = db.cursor()
# cursor.execute('select version()')
# data = cursor.fetchone()
# print('database version:', data)
# cursor.execute('create database spiders default character set utf8mb4')
# db.close()

db = pymysql.connect(host='localhost', user='root', password='root', port=3307, db='spiders')
cursor = db.cursor()
sql = 'insert into students (id,name,age) values (%s,%s,%s)'
try:
    cursor.execute(sql, (id, user, age))
    db.commit()
except:
    traceback.print_exc()
    db.rollback()
db.close()
