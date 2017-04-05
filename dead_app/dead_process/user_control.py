#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: user_control.py
Author: work(work@baidu.com)
Date: 2017/03/28 15:47:33
"""
import time
from datetime import datetime,timedelta
import os
import sys
import urllib2
import urllib
import json
import subprocess
import re
#from models import *
from django.contrib.auth import *
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.simplejson import dumps
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from common import *
#from POP import POP
import random
import string
import optparse
import socket
#import dwInterface
from django.db.models import Q
import MySQLdb;

reload(sys)
sys.setdefaultencoding('utf-8')


class UserControl(object):
    """
        UserControl,user apply / approve .
    """
    def __init__(self):
        """init
        """
        pass

    def user_apply(self, tag, attrs):
        """user_apply
        """
        #result = "success"
        #return HttpResponse(json.dumps({'result':result}))
        pass
        
        
    def user_approve(self, tag, attrs):
        """user_approve
        Args:
        Returns:
        """
        pass
