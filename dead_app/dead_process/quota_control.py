#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: quota_control.py
Author: work(work@baidu.com)
Date: 2017/03/28 15:47:33
"""

from django.conf import settings
import os
import sys
import re
import logging
import datetime
import time
import linux_control
import redis_control
import log
reload(sys)
sys.setdefaultencoding('utf-8')
#parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#sys.path.append(parentdir)
dirs = os.path.join( os.path.dirname(__file__),'../..')
os.sys.path.append(dirs)
os.environ['DJANGO_SETTINGS_MODULE'] ='dead_workspace.settings'
from dead_app.models import *


class QuotaControl(object):
    """
        QuotaControl.
    """
    def __init__(self):
        """init
        Args:
        Returns:
        """
        self.linux = linux_control.LinuxControl()
        self.redis = redis_control.RedisControl()
        self.datenow = datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(hours = 8),\
                "%Y-%m-%d %H:%M:%S")

    def get_user_quota_url_count(self, tag, attrs):
        """get_user_quota_url_count
        Args:
        Returns:
        """
        pass

    def get_user_quota_url_surplus(self, tag, attrs):
        """get_user_quota_url_surplus
        Args:
        Returns:
        """
        pass

    def get_user_quota_url_use(self, tag, attrs):
        """get_user_quota_url_use
        Args:
        Returns:
        """
        pass

    def get_user_quota_site_count(self, tag, attrs):
        """get_user_quota_site_count
        Args:
        Returns:
        """
        pass

    def get_user_quota_site_surplus(self, tag, attrs):
        """get_user_quota_site_surplus
        Args:
        Returns:
        """
        pass

    def get_user_quota_site_use(self, tag, attrs):
        """get_user_quota_site_use
        Args:
        Returns:
        """
        pass

    def get_site_quota_from_redis(self, tag, attrs):
        """get_site_quota_from_redis
        Args:
        Returns:
        """
        pass

    def get_site_quota_day_surplus(self, tag, attrs):
        """get_site_quota_day_surplus
        Args:
        Returns:
        """
        pass

    def get_site_quota_day_use(self, tag, attrs):
        """get_site_quota_day_use
        Args:
        Returns:
        """
        pass

    def get_url_to_crawl(self, tag, attrs):
        """get_url_to_crawl
        Args:
        Returns:
        """
        pass

    def get_url_site_count(self, urlfile):
        """get_url_site
        Args: urlfile
        Returns: sitefile,sitecountfile
        """
        shell_file = "common/get_url_site.sh"
        testurlfile = "url"
        cmd = """sh %s %s""" %(shell_file, testurlfile)
        self.linux.run_shell(cmd)
    
    def set_site_count_to_db(self, urlfile):
        """save site count to db. 
        当用户提交任务时，获取提交链接的站点默认配额，存储表DeadSiteCenter
        Args: urlfile
        Returns: NULL
        """
        urlfile = "url"
        url_site_count_file = "%s.site.count" %(urlfile)
        self.get_url_site_count(urlfile)
        fd = open(url_site_count_file)
        lines = fd.readlines()
        for line in lines:
            res = line.strip().split(" ")
            site = res[0]
            site_use_count = int(res[1])
            m = DeadSiteCenter()
            if not DeadSiteCenter.objects.filter(ds_site_name = site):
                site_count = self.redis.get_site(site)
                if site_count is None:
                    site_count = 50000
                print site_count
                m = DeadSiteCenter()
                m.ds_site_name = site
                m.ds_site_count = site_count
                m.ds_site_surplus = site_count - site_use_count
                m.ds_site_use = site_use_count
            else:
                m = DeadSiteCenter.objects.filter(ds_site_name = site)[0]
                m.ds_site_surplus -= site_use_count
                m.ds_site_use += site_use_count
            m.ds_site_last_submit_time = self.datenow
            print self.datenow
            m.save()
                
    

        
if __name__ == "__main__":
    qc = QuotaControl()
#    qc.get_url_site_count("part-00129")
    qc.set_site_count_to_db("url")


