#!/usr/bin/env python 
# -*- coding:utf-8 -*-

__author__ = 'kgy'

from lxml import etree

text = ''' 
<div> 
<Ul> 
<li class="item-O"><a href="linkl. html">first item</a></li> 
<li class="item-1"><a href="link2.html"> second item</a></li> 
<li class="item-inactive"><a href="link3.html">third item</a></li> 
<li class="item-1"><a href="link4.html">fourth item</a></li> 
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))

html = etree.parse('./test.html',etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))

result = html.xpath('//*')
print(result)

result = html.xpath('//li')
print(result)
print(result[0])

result = html.xpath('//li/a')
print(result)

# 父节点
result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)

# 属性匹配
result = html.xpath('//li[@class="item-0"]')
print(result)

# 文本获取
result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)

result = html.xpath('//li[@class="item-0"]//text()')
print(result)

# 属性获取
result = html.xpath('//li/a/@href')
print(result)