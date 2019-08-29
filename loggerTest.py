#!/usr/bin/env python 
# -*- coding:utf-8 -*-

__author__ = 'kgy'

import logging
import logging.config
import os
import time


if not os.path.exists('logs'):
    os.mkdir('logs')
logging.config.fileConfig('logging.conf')

# 输出日志到控制台,获取的是root对应的logger
#console_logger = logging.getLogger()

# 输出日志到单个文件
#file_logger = logging.getLogger(name="fileLogger")

# rotatingFileLogger中额consoleHandler输出到控制台，rotatingHandler输出日志到文件
rotating_logger = logging.getLogger(name="rotatingFileLogger")

rotating_logger.info("affds")
time.sleep(2)
rotating_logger.info("affds22")