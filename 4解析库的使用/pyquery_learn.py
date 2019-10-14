#!/usr/bin/env python 
# -*- coding:utf-8 -*-

__author__ = 'kgy'

from pyquery import PyQuery as pq

html = '''
<div>
<Ul>
<li class="item-O"><a href="linkl. html">first item</a></li>
<li class="item-1"><a href="link2.html"> second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''
doc = pq(html)
print(doc('li'))

doc = pq(url='https://cuiqingcai.com')
print(doc('title'))

doc = pq(filename='test.html')
print(doc('li'))
