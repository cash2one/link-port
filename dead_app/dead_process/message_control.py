#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: message_control.py
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
import json

reload(sys)
sys.setdefaultencoding('utf-8')


class MessageControl(object):
    """
        MessageControl.
    """
    def __init__(self):
        """init
        """
        self.base_url = "http://jingle.baidu.com/alert/push"
        self.appid = "658"
        self.token = "570e4ec2833bd8bc0b3c9869"

    def set_to_mail(self, title, content,receiver):
        """set_to_mail
        """
        post_data = {
            "appId":self.appid,
            "token":self.token,
            "alertList":[
                {
                    "channel": "email",
                    "description": content,
                    "title": title,
                    "receiver": receiver
                }
            ]
        }
        self.send(post_data)
                

        
    def set_to_hi(self, content, receiver):
        """set_to_hi
        """
        post_data = {
            "appId":self.appid,
            "token":self.token,
            "alertList":[
                {
                    "channel": "hi",
                    "description": content,
                    "receiver": receiver
                }
            ]
        }
        self.send(post_data)
                
        
    def set_to_sms(self, content, receiver):
        """set_to_sms
        """
        post_data = {
            "appId":self.appid,
            "token":self.token,
            "alertList":[
                {
                    "channel": "sms",
                    "description": content,
                    "level": "major",
                    "receiver": receiver
                }
            ]
        }
        self.send(post_data)
                    

    def send(self, post_data):
        """send
        """
        try:
            r =  urllib2.urlopen(self.base_url, data=json.dumps(post_data))
            ret = json.loads(r.read())
            print ret
            if ret["code"] == '1000':
                return True
            else:
                return False
        except Exception as e:
            print e
            return False

#测试接口
#test = MessageControl() 
#test.set_to_mail("测试", "测试message", "liuwenli@baidu.com")
#test.set_to_hi("死链平台测试message", "lll_liar")
#test.set_to_sms("死链平台测试message", "liuwenli")
