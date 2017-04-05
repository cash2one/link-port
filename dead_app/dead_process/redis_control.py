#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: redis_control.py
Author: work(work@baidu.com)
Date: 2017/03/28 20:26:08
"""

import os
import sys
import redis
import logging
import log
reload(sys)
sys.setdefaultencoding('utf-8')


class RedisControl():
    """
        RedisControl
    """
    def __init__(self):
        """init
        """
        self.host = "127.0.0.1"
        self.port = "6379"
        self.pool = redis.ConnectionPool(host = self.host, port = self.port)
        self.r = redis.Redis(connection_pool = self.pool)
        self.count = 0

    def set_siterate_data(self, site, sitecount):
        """
            save siterate data to redis
        """
        #https://github.com/andymccurdy/redis-py/blob/master/README.rst see this url for pipeline
        pipe = self.r.pipeline()
        pipe.set(site, sitecount)
        pipe.execute()

    def get_site(self, site):
        """
            get site 
            Args : site
            Returns : sitecount
        """
        sitecount = self.r.get(site)
        return sitecount
"""
for line in sys.stdin:
    rc = RedisControl()
    if line == "":
        rc.set_redis_execute()
    res = line.strip().split(" ")
    site = res[0]
    siterate = res[3]
    sitecount = 50000
    if siterate in ['7']: #表示站点评级为8级
        sitecount = 300000
    elif siterate in ['6']: #表示站点评级为7级
        sitecount = 200000
    elif siterate in ['5']: #表示站点评级为6/5级
        sitecount = 100000
    else:
        continue
    print site,siterate
    rc.set_siterate_data(site, sitecount)
    sys.exit(1)
"""

#if __name__ == "__main__":
#    rc = RedisControl()
#    rc.set_siterate_data()
#    rc.get_site("www.baidu.com")



        
