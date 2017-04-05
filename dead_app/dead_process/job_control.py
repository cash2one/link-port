#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: job_control.py
Author: work(work@baidu.com)
Date: 2017/03/28 15:47:33
"""
import os
import sys
import urllib2
import HTMLParser
import urllib
import cookielib
import urlparse
import re
import logging
import log
reload(sys)
sys.setdefaultencoding('utf-8')


class JobControl(object):
    """
        JobControl.
    """
    def __init__(self):
        """init
        Args:
        Returns:
        """
        pass

    def get_job_submit(self, tag, attrs):
        """get_job_submit
        Args:
        Returns:
        """
        pass

    def get_job_is_token_legal(self, tag, attrs):
        """get_job_is_token_legal
        Args:
        Returns:
        """
        pass

    def get_job_cutoff_url(self, tag, attrs):
        """get_job_cutoff_url
        Args:
        Returns:
        """
        pass

    def set_job_send_crawl(self, tag, attrs):
        """set_job_send_crawl
        Args:
        Returns:
        """
        pass

    def set_job_submit_result(self, tag, attrs):
        """set_job_submit_result
        Args:
        Returns:
        """
        pass
