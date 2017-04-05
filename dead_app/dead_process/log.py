#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: log.py
Author: spider(spider@baidu.com)
Date: 2017/03/06 16:20:44
"""
import os
import sys
import logging
import logging.handlers

def init_log(log_path, level=logging.INFO, when="D", backup=7,
        format="%(levelname)s: %(asctime)s: %(filename)s:%(lineno)d * %(thread)d %(message)s",
        datefmt="%m-%d %H:%M:%S"):
    """
        init log
        args:
            level : DEBUG < INFO < WARNING < ERROR < CRITICAL
    """
    formatter = logging.Formatter(format, datefmt)
    logger = logging.getLogger()
    logger.setLevel(level)
    
    dir = os.path.dirname(log_path)
    if not os.path.isdir(dir):
        os.makedirs(dir)

    handler = logging.handlers.TimedRotatingFileHandler(log_path + ".log",\
            when = when, backupCount=backup)
    handler.setLevel(level)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    handler = logging.handlers.TimedRotatingFileHandler(log_path + ".log.wf",\
            when = when, backupCount=backup)
    handler.setLevel(logging.WARNING)
    handler.setFormatter(formatter)
    logger.addHandler(handler)


