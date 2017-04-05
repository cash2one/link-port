#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: gen_py.py
Author: work(work@baidu.com)
Date: 2017/03/28 15:54:28
"""

import os
import sys

def gen(file,funlist):
    fd = open(file,'a')
    for fun in funlist:
        fd.write("\n")
        fd.write("    def %s(self, tag, attrs):\n" %(fun))
        fd.write("        \"\"\"%s\n" %(fun))
        fd.write("        Args:\n")
        fd.write("        Returns:\n")
        fd.write("        \"\"\"\n")
        fd.write("        pass\n")
    fd.close()

if __name__ == "__main__":
    filelist = ['crawl.py', 'job_control.py', 'message_control.py', 'quota_control.py', 'scan_control.py']
    for file in filelist:
        if file == "user_control.py":
            funlist = ['user_apply', 'user_approve']
        elif file == "crawl.py":
            funlist = ['init', 'start', 'send_url_csent', 'save_csent_result']
        elif file == "job_control.py":
            funlist = ['get_job_submit', 'get_job_is_token_legal', 'get_job_cutoff_url', 'set_job_send_crawl', 'set_job_submit_result']
        elif file == "message_control.py":
            funlist = ['set_to_mail', 'set_to_hi', 'set_to_sms']
        elif file == "quota_control.py":
            funlist = ['get_user_quota_url_count', 'get_user_quota_url_surplus', 'get_user_quota_url_use', 'get_user_quota_site_count', 'get_user_quota_site_surplus', 'get_user_quota_site_use', 'get_site_quota_from_redis', 'get_site_quota_day_surplus', 'get_site_quota_day_use', 'get_url_to_crawl', 'get_url_site']
        elif file == "scan_control.py":
            funlist = ['init', 'start', 'search_rtdlc_tera', 'next_search_time', 'save_search_result']

        gen(file,funlist)
