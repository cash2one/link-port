#! /usr/binv python
#coding=utf-8

"""docstring
"""

__revision__ = '0.1'

import subprocess
import os
import sys
import logging
import difflib
import threading
import time
import zipfile
from xml.dom import minidom

class TIMEOOUTCMD(threading.Thread):
    def __init__(self,command, cwd=None, input=None, env=None, logfn=None, errfn=None):
        threading.Thread.__init__(self)
        self.process=None
        self.ret=None
        self.stdout=None
        self.stderr=None
        self.cmd=command
        self.cwd=cwd
        self.input=input
        self.env=env
        self.logfn=logfn
        self.errfn=errfn

    def _target(self):
        self.process = subprocess.Popen(self.cmd, stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,
                             cwd=self.cwd, env=self.env, close_fds=True)
        self.stdout, self.stderr = self.process.communicate(self.input)
        self.ret = self.process.returncode
        #print self.cmd
        if self.logfn:
            with open(os.path.realpath(self.logfn),'w') as fd:
                fd.write(self.stdout)
        if self.errfn:
            with open(os.path.realpath(self.errfn),'w') as fd:
                fd.write(self.stderr)

    def run(self):
        apply(self._target)
        
def call_cmd(command, cwd=None, input=None, env=None, logfn=None, errfn=None, timeout=600):
    cmdobj=TIMEOOUTCMD(command,cwd=cwd,input=input,env=env,logfn=logfn,errfn=errfn)
    cmdobj.setDaemon(True)
    cmdobj.start()
    cmdobj.join(timeout)
    if cmdobj.is_alive():
        print "command %s thread still running in %s, terminating" %(command,timeout)
        cmdobj.process.terminate()
    if cmdobj.ret != 0:
        print "EXEC CMD FAIL:%s" %(command)
    return cmdobj.ret,cmdobj.stdout,cmdobj.stderr


def get_time_Section():
    time_now = time.time()
    c_time = time.strftime('%Y%m%d%H%M%S',time.localtime(time_now))
    s_time = time.strftime('%Y%m%d%H%M%S',time.localtime(time_now-60))
    s_time = s_time[0:-1]+"0"
    e_time = time.strftime('%Y%m%d%H%M%S',time.localtime(time_now-50))
    e_time = e_time[0:-1]+"0"
    return c_time,s_time,e_time

def trans_time_str(time_str):
    u = time.strptime(time_str,'%Y%m%d%H%M%S');
    usetime=time.strftime('%m-%d %H:%M:%S',u)
    return str(usetime)


def del_file_folder(src):
    '''delete files and folders'''
    if os.path.isfile(src):
        try:
            os.remove(src)
        except:
            return False
    elif os.path.isdir(src):
        for item in os.listdir(src):
            itemsrc=os.path.join(src,item)
            del_file_folder(itemsrc)
        try:
            os.rmdir(src)
        except:
            return False
    return True




def get_time_cur():
    time_now = time.time()
    c_time = time.strftime('%Y%m%d%H%M%S',time.localtime(time_now))
    return c_time



def get_module_list_conf(file_name=None):
    if file_name == None:
        logging.error("file name  is null!!!")
        return []
    module_list_conf = []
    fd = open(file_name,"r")
    lines = fd.readlines()
    for line in lines:
        line = line.strip("\n\t\r")
        module_dict=eval(line)
        module_list_conf.append(module_dict)
    return module_list_conf

def get_machine_dict(module_list):
    machine_dict={}
    for m in module_list:
        host=m["host"]
        if not machine_dict.has_key(host):
            machine_dict[host]=[]
        machine_dict[host].append(m)
            
    return machine_dict
        

def zip_file(src_file,dst_file):
    cmd = '''rm -rf %s && zip -r %s %s'''%(dst_file,src_file,dst_file)
    ret,stdout,stderr=call_cmd(command=cmd)
    if ret !=0:
        logging.error("cmd return  error!!!%s",cmd)
        return False
    return True



def analyze_casesuite_xml(file_path):
    ret_dict = {}
    fd= open(file_path)
    str_tmp = fd.read()
    casesuite_name = ""
    dom = minidom.parseString(str_tmp) 
    root = dom.firstChild      
    casesuite_name = root.getAttribute("name")
    casesuite_env = root.getAttribute("env")
    case_list=[]
    childs = root.childNodes    
    for child in childs:  
        if child.nodeType == child.TEXT_NODE:  
            pass  
        else:
            id=child.getAttribute('id')
            name=child.getAttribute('name')
            desp=child.getAttribute('desp')
            case_list.append({"id":id,"name":name,"desp":desp})
    ret_dict["suite_name"]=casesuite_name
    ret_dict["env"]=casesuite_env
    ret_dict["cases"]=case_list
    return ret_dict
