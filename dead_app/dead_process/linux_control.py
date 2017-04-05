#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: linux_control.py
Author: work(work@baidu.com)
Date: 2017/03/28 15:47:33
"""
import os
import sys
import re
import subprocess
import logging
import log
reload(sys)
sys.setdefaultencoding('utf-8')


class LinuxControl(object):
    """
        LinuxControl, dead with linux commond 
    """
    def __init__(self):
        """init
        """
        pass

    def run_shell(self, cmd):
        """user_apply
        Args: shell_file
        Returns: NULL
        """
        sp = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE)
        out = sp.communicate()
        res = out[0]
        return res


