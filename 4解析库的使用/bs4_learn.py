#!/usr/bin/env python 
# -*- coding:utf-8 -*-

__author__ = 'kgy'

from bs4 import BeautifulSoup

soup = BeautifulSoup('<p>Hello</p>','lxml')
print(soup.p.string)

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class ="title"  name="dromouse"><b> The  Dormouse  ’ s story</b></p>
<p class ="story">Once  upon  a time  there  were  three  little  s isters;  and  their  names  were
<a href ="http://example.com/elsie" class="sister" id ="linkl"><!-- Elsie --></a>,
<a href ="http://example.com/lacie" class="sister" id ="link2">Lacie</a>  and
<a href="http://example.com/tillie"  class="sister" id ="link3"> T illie</a> ;
and  they  lived  at  the  bottom  of  a well. </p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html,'lxml')
# print(soup.prettify())
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.head)
print(soup.p)

print(soup.p.attrs)
print(soup.p.attrs['name'])
print(soup.p['name'])
print(soup.p.string)
