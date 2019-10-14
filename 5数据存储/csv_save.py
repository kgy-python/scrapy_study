#!/usr/bin/env python 
# -*- coding:utf-8 -*-

__author__ = 'kgy'
import csv

with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'mike', '20'])
    writer.writerow(['10002', 'bob', '22'])
