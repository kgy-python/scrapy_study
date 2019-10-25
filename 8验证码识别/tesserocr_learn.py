#!/usr/bin/env python 
# -*- coding:utf-8 -*-

__author__ = 'kgy'

import tesserocr
from PIL import Image

def hello_world():
    image = Image.open('CheckCode.jpg')
    result = tesserocr.image_to_text(image)
    print(result)
    image = image.convert('L')
    image.show()
    image = image.convert('1')
    image.show()

def image_test():
    image = Image.open('CheckCode.jpg')
    image = image.convert('L')
    threshold = 140
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    image = image.point(table,'1')
    image.show()
    result = tesserocr.image_to_text(image)
    print(result)

if __name__ == '__main__':
    # hello_world()
    image_test()