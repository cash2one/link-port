#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: config_load.py
Author: spider(spider@baidu.com)
Date: 2017/03/06 16:13:54
"""
import os
import ConfigParser

class ConfigLoad(object):
    """
        load config
    """
    def __init__(self, conffile):
        """
            获取配置项的值
        """
        cf = ConfigParser.ConfigParser()
        cf.read(conffile)
        keylist = ['thread_count', 'log_path', 'scan_max_count', 'scan_interval', 'scan_finish_rate', 'job_directory']
        confdict = dict().fromkeys(keylist)
        section = "dead"
        for confkey in confdict:
            try:
                value = cf.get(section, confkey)
                confdict[confkey] = value
            except ConfigParser.NoOptionError:
                logger.fatal("there is no Section: %s, \
                        option :%s  from conf file: %s") %(section, option, self.conf)
                sys.exit(1)

        self.thread_count = confdict['thread_count']
        self.log_path = confdict['log_path']
        self.scan_max_count = confdict['scan_max_count']
        self.scan_interval = confdict['scan_interval']
        self.scan_finish_rate = confdict['scan_finish_rate']
        self.job_directory = confdict['job_directory']
        
        if not os.path.exists(self.job_directory):
            try:
                os.mkdir(self.output_directory)
            except Exception as e:
                logger.fatal("mkdir output error")
        
    

