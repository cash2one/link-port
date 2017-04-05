#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: phone.py
Author: work(work@baidu.com)
Date: 2016/04/13 23:41:59
"""
import json
import requests
import urllib
import urllib2
import time
#id为658
#token为570e4ec2833bd8bc0b3c9869

def get_zhiban_list(q_type="QA"):
    """
    """
    id_type_dict = {
        "QA":"61189",
        "data":"61179",
        "search":"61183",
        "php":"61182"
    }
    if q_type in id_type_dict:
        zhiban_id = id_type_dict[q_type]
    else:
        zhiban_id = id_type_dict["QA"]
    zhiban_url = "http://zhiban.baidu.com/RotaApi/getDNById?id=%s" % zhiban_id
    ret = urllib2.urlopen(zhiban_url).read()
    zhiban_list = ";".join(ret.split(";")[:2])
    zhiban_list += ";zhouyuqing"
    return zhiban_list

def is_phone_alert(receiver,  msg, alert_window_second=30*60):
    """
    """
    print msg
    base_url = "http://szjjh-noah-saver26.szjjh01.baidu.com:8096/NoticeQuery/query?"
    data = {
        'startDate':time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()-alert_window_second)),
        'endDate':time.strftime("%Y-%m-%d %H:%M:%S"),
        'channel':"PHONE",
        'receivers':receiver,
        'content': msg,
        'curPage':1,
        'perPage':1
    }
    try:
        url = base_url + urllib.urlencode(data)
        ret = urllib2.urlopen(url)
        res = json.loads(ret.read())
        print json.dumps(res, ensure_ascii=False, indent=2)
        if res['success'] and len(res['data']) >0:
            return True
        else:
            return False
    except Exception as e:
        print e
        return False

def phone_alert(q_type="QA", msg='美股报警'):
    base_url = "http://jingle.baidu.com/alert/push"
    zhiban = get_zhiban_list(q_type)
    if is_phone_alert(zhiban, msg):
        print "is_phone_alert true"
        return True
    post_data = {
        "appId":"658",
        "token":"570e4ec2833bd8bc0b3c9869",
        "alertList":[
            {"channel":"phone",
            "description":msg,
            "receiver":zhiban
            }
        ]
    }
     
    #r= requests.post(base_url, data=json.dumps(post_data))
    try:
        r =  urllib2.urlopen(base_url, data=json.dumps(post_data))
        ret = json.loads(r.read())
        print ret
        if ret["code"] == '1000':
            return True
        else:
            return False
    except Exception as e:
        print e
        return False
#get_zhiban_list()

#phone_alert()
#print is_phone_alert('caoxuehui', '新浪财经美股实时英文代码', 24*60*60)

