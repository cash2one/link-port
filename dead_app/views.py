# Create your views here.
#-*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context,loader
from django.contrib.auth.decorators import login_required
from django.db import connection
from models import *
import collections
import math
import json
import sys
import os

from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
import MySQLdb

import time
from datetime import datetime,timedelta

from .dead_process.message_control import MessageControl

reload(sys)
sys.setdefaultencoding('utf-8')
# Create your views here.

@login_required
def index(request):
    username = request.user.username
    d = {"username":username}
    return render_to_response('apply.html', {"username":username} )

@login_required
def apply(request):
    """
    用户申请，提供用户名、申请原因、用户分类、url配额、站点配额 
    """
    username = request.user.username
    d = {"username":username}
    #user_conf = {}
    #user_conf['name'] = "test"
    #user_conf['reason'] = "用户测试"
    #user_conf['level'] = "线上服务"
    #user_conf['url_count'] = "1000000"
    #user_conf['site_count'] = {"www.baidu.com":"100000","www.iqiyi.com":"50000"}
    return render_to_response('apply.html', {"username":username})
    
@login_required
def submitapply(request):
    """
        提交用户申请的，用户名、申请原因、用户分类、url配额、站点配额
    """
    username = request.user.username
    d = {"username":username}
    result = ""
    #获取数据
    du_name = request.POST.get('name')
    du_reason = request.POST.get('reason')
    du_level = request.POST.get('level')
    duu_week_url_count = request.POST.get('week_url_count')
    
    du_apply_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+28800))
    
    #保存数据
    deaduser = DeadUser()
    deaduser.du_name = du_name
    deaduser.du_reason = du_reason
    deaduser.du_level = du_level
    deaduser.du_apply_time = du_apply_time
    deaduser.du_ispass = '2'
    deaduser.save()

    deaduserurl = DeadUserUrlCenter()
    deaduserurl.duu_user_name = deaduser
    deaduserurl.duu_week_url_count = duu_week_url_count
    deaduserurl.save()

    
    #site文件处理
    dus_site_file =  request.FILES.get("sitefile", None)
    if dus_site_file:
        baseDir = os.path.dirname(os.path.abspath(__name__))
        sitedir = os.path.join(baseDir,'dead_app','usersite')
        sitefilepath = os.path.join(sitedir,dus_site_file.name)
        sitefilew = open(sitefilepath,'w')
        for chrunk in dus_site_file.chunks():
            sitefilew.write(chrunk)
        sitefilew.close()
        sitefiler = open(sitefilepath,'r')
        #site存储
        while 1:
            lines = sitefiler.readlines(10000)
            if not lines:
                 break
            for line in lines:
                site_list = line.split(" ")
                dus_day_site_name = site_list[0]
                dus_day_site_count = site_list[1]
                result = result + dus_day_site_name + ',' + dus_day_site_count + ','
                deadusersite =  DeadUserSiteCenter()
                deadusersite.dus_user_name = deaduser
                deadusersite.dus_day_site_name = dus_day_site_name
                deadusersite.dus_day_site_count = dus_day_site_count
                deadusersite.save()

    #debug
    #if dus_site_file:
    #    result = result + str(du_name)+','+str(du_reason)+','+str(du_level)+','+str(duu_week_url_count)
    #else:
    #    result = "empty"
    #调用sendmail接口，通知审批人
    title = "deadlink平台配额申请审核"
    content = "<b>产品线"+du_name+"提交了配额申请，请尽快进行审核.</b>"+"<br><a href=http://cp01-spimon.epc.baidu.com:8222/person?du_id="+str(deaduser.du_id)+">点击此处进行审核</a><br>"
    receiver_path = "dead_workspace/approvers.conf"
    receiver_file = open(receiver_path,'r')
    receiver = ""
    while 1:
        line = receiver_file.readline()
        line = line.replace("\n","")
        if line:
            receiver = receiver + line +";"
        else:
            break
    email = MessageControl()
    email.set_to_mail(title, content,receiver)

    result = deaduser.du_id
    #return render_to_response('apply.html', {"username":username})
    return HttpResponse(json.dumps({'result':result}))


@login_required
def person(request):
    #用户管理（所有提交配额列表）
    username = request.user.username
    d = {"username":username}
    
    du_id = request.GET.get('du_id')
    
    pass_listing = []
    nopass_listing = []
    waitpass_listing = []
    timenow = (datetime.now() + timedelta(days=-30)).date()
    if du_id:
        deaduser_lists = DeadUser.objects.filter(du_id=du_id)
    else:
        deaduser_lists = DeadUser.objects.filter(du_apply_time__gt=timenow)
    pass_lists = deaduser_lists.filter(du_ispass = '1')
    nopass_lists = deaduser_lists.filter(du_ispass = '0')
    waitpass_lists = deaduser_lists.filter(du_ispass ='2') 
    for deaduser_list in pass_lists:
        deaduser_dict = {}
        deaduserurl_lists = deaduser_list.deaduserurl.all()
        deadusersite_lists = deaduser_list.deadusersite.all()
        deaduser_dict = copydeaduser(deaduser_dict,deaduser_list,deaduserurl_lists,deadusersite_lists)
        pass_listing.append(deaduser_dict)
    
    for deaduser_list in nopass_lists:
        deaduser_dict = {}
        deaduserurl_lists = deaduser_list.deaduserurl.all()
        deadusersite_lists = deaduser_list.deadusersite.all()
        deaduser_dict = copydeaduser(deaduser_dict,deaduser_list,deaduserurl_lists,deadusersite_lists)
        nopass_listing.append(deaduser_dict)

    for deaduser_list in waitpass_lists:
        deaduser_dict = {}
        deaduserurl_lists = deaduser_list.deaduserurl.all()
        deadusersite_lists = deaduser_list.deadusersite.all()
        deaduser_dict = copydeaduser(deaduser_dict,deaduser_list,deaduserurl_lists,deadusersite_lists)
        waitpass_listing.append(deaduser_dict)

    #审核人
    approver_file = open("dead_workspace/approvers.conf","r")
    approver = approver_file.read()
    approver = approver.replace("\n","")

    return render_to_response('person_admin.html', {'pass_listing':pass_listing,'nopass_listing':nopass_listing,'waitpass_listing':waitpass_listing,"approver":approver,"username":username})

def copydeaduser(deaduser_dict,deaduser_list,deaduserurl_lists,deadusersite_lists):
    #将三个表中的数据进行连接
    deadusersite_str = ""
    deadusersite_per = []
    deaduser_dict['item_id'] = deaduser_list.du_id
    deaduser_dict['item_name'] = deaduser_list.du_name
    deaduser_dict['item_reason'] = deaduser_list.du_reason
    deaduser_dict['item_level'] = deaduser_list.du_level
    deaduser_dict['item_ispass'] = deaduser_list.du_ispass
    deaduser_dict['item_token'] = deaduser_list.du_token
    for deaduserurl_list in deaduserurl_lists:
        deaduser_dict['item_week_url_count'] = deaduserurl_list.duu_week_url_count
        deaduser_dict['item_week_url_use'] = deaduserurl_list.duu_week_url_use
        deaduser_dict['item_week_url_surplus'] = deaduserurl_list.duu_week_url_surplus
    for deadusersite_list in deadusersite_lists:
        deadusersite_dict = {}
        deadusersite_dict['site_name'] = deadusersite_list.dus_day_site_name
        deadusersite_dict['site_count'] = deadusersite_list.dus_day_site_count
        deadusersite_dict['site_use'] = deadusersite_list.dus_day_site_use
        deadusersite_dict['site_surplus'] = deadusersite_list.dus_day_site_surplus
        deadusersite_per.append(deadusersite_dict)
        deadusersite_str = deadusersite_str + deadusersite_list.dus_day_site_name + ':' + deadusersite_list.dus_day_site_count + ';'
    deaduser_dict['item_site'] = deadusersite_str
    deaduser_dict['item_site_per'] = deadusersite_per
    return deaduser_dict


@login_required
def person_detail(request):
    #用户申请详情，pass&nopass&waitpass
    username = request.user.username
    d = {"username":username}
    du_id = request.GET.get('du_id')
    deaduser_dict = detail(du_id)
    return render_to_response('person_detail.html', {'deaduser_dict':deaduser_dict})

def detail(du_id):
    deaduser_dict = {}
    try:
        deaduser_list = DeadUser.objects.get(du_id = du_id)
    except:
        deaduser_list = None
        
    if deaduser_list:
        deaduserurl_lists = deaduser_list.deaduserurl.all()
        deadusersite_lists = deaduser_list.deadusersite.all()
        deaduser_dict = copydeaduser(deaduser_dict,deaduser_list,deaduserurl_lists,deadusersite_lists)

    return deaduser_dict
    
@login_required
def approve(request):
    #审核
    username = request.user.username
    d = {"username":username}
    du_id = request.GET.get('du_id')
    flag = request.GET.get('flag')
    du_approve_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+28800))
    result = 'success'
    try:
        deaduser = DeadUser.objects.get(du_id = du_id)
        if flag == '1':
            deaduser.du_ispass = '1'
            deaduser.du_approve_time = du_approve_time
        elif flag == '0':
            deaduser.du_ispass = '0'
            deaduser.du_approve_time = du_approve_time
        deaduser.save()
    except:
        result='fail'
    return HttpResponse(json.dumps({'result':result}))
    #return render_to_response('approve.html', d )

@login_required
def person_search(request):
    #查找
    searchkey = request.GET.get('searchkey')
    pass_listing = []
    nopass_listing = []
    waitpass_listing = []
    deaduser_lists = DeadUser.objects.filter(Q(du_name__contains=searchkey))
    pass_lists = deaduser_lists.filter(du_ispass = '1')
    nopass_lists = deaduser_lists.filter(du_ispass = '0')
    waitpass_lists = deaduser_lists.filter(du_ispass ='2') 
    for deaduser_list in pass_lists:
        deaduser_dict = {}
        deaduserurl_lists = deaduser_list.deaduserurl.all()
        deadusersite_lists = deaduser_list.deadusersite.all()
        deaduser_dict = copydeaduser(deaduser_dict,deaduser_list,deaduserurl_lists,deadusersite_lists)
        pass_listing.append(deaduser_dict)
    
    for deaduser_list in nopass_lists:
        deaduser_dict = {}
        deaduserurl_lists = deaduser_list.deaduserurl.all()
        deadusersite_lists = deaduser_list.deadusersite.all()
        deaduser_dict = copydeaduser(deaduser_dict,deaduser_list,deaduserurl_lists,deadusersite_lists)
        nopass_listing.append(deaduser_dict)

    for deaduser_list in waitpass_lists:
        deaduser_dict = {}
        deaduserurl_lists = deaduser_list.deaduserurl.all()
        deadusersite_lists = deaduser_list.deadusersite.all()
        deaduser_dict = copydeaduser(deaduser_dict,deaduser_list,deaduserurl_lists,deadusersite_lists)
        waitpass_listing.append(deaduser_dict)

    return render_to_response('person_admin.html', {'pass_listing':pass_listing,'nopass_listing':nopass_listing,'waitpass_listing':waitpass_listing})
    

@login_required
def cancel_approve(request):
    username = request.user.username
    d = {"username":username}
    du_id = request.GET.get('du_id')
    result = "success"
    try:
        del_deaduser = DeadUser.objects.get(du_id=du_id)
        del_deaduserurl = del_deaduser.deaduserurl.all()
        del_deadusersite = del_deaduser.deadusersite.all()
        del_deadusersite.delete()
        del_deaduserurl.delete()
        del_deaduser.delete()
    except:
        result = "fail"
    return HttpResponse(json.dumps({'result':result}))

@login_required
def remind_approve(request):
    username = request.user.username
    d = {"username":username}
    du_id = request.GET.get('du_id')
    result = "success"
    try:
        rem_deaduser = DeadUser.objects.get(du_id=du_id)
    except:
        result = "fail"
        rem_deaduser = None
    if rem_deaduser:
        #调用sendmail接口，通知审批人
        title = "deadlink平台配额申请审核提醒"
        content = "<b>产品线"+rem_deaduser.du_name+"发起了审核提醒，请尽快进行审核.</b>"+"<br><a href=http://cp01-spimon.epc.baidu.com:8222/person?du_id="+str(du_id)+">点击此处进行审核</a><br>"
        content_hi = "产品线"+rem_deaduser.du_name+"发起了审核提醒，请尽快到下面地址进行审核：http://cp01-spimon.epc.baidu.com:8222/person?du_id="+str(du_id)
        receiver_path = "dead_workspace/approvers.conf"
        receiver_file = open(receiver_path,'r')
        receiver = ""
        while 1:
            line = receiver_file.readline()
            line = line.replace("\n","")
            if line:
                receiver = receiver + line +";"
            else:
                break
        receiver_hi = receiver.replace("@baidu.com","")
        email = MessageControl()
        email.set_to_mail(title, content,receiver)
        email.set_to_sms(content_hi,receiver_hi)
        email.set_to_hi(content_hi,receiver_hi)
    return HttpResponse(json.dumps({'result':result}))
    
@login_required
def modify_apply(request):
    username = request.user.username
    d = {"username":username}
    du_id = request.GET.get('du_id')
    deaduser_dict = {}
    try:
        deaduser_list = DeadUser.objects.get(du_id = du_id)
    except:
        deaduser_list = None
    if deaduser_list:    
        deaduserurl_lists = deaduser_list.deaduserurl.all()
        deadusersite_lists = deaduser_list.deadusersite.all()
        deaduser_dict = copydeaduser(deaduser_dict,deaduser_list,deaduserurl_lists,deadusersite_lists)
    
    #return render_to_response('modify_apply.html', {'deaduser_dict':deaduser_dict})
    return HttpResponse(json.dumps({'result':result}))

@login_required
def modify_submit(request):
    """
        提交用户申请的，用户名、申请原因、用户分类、url配额、站点配额
    """
    username = request.user.username
    d = {"username":username}
    result = ""
    #获取数据
    du_id = request.POST.get('id')
    du_name = request.POST.get('name')
    du_reason = request.POST.get('reason')
    du_level = request.POST.get('level')
    duu_week_url_count = request.POST.get('week_url_count')
    
    du_apply_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+28800))
    
    #保存数据
    deaduser = DeadUser.objects.get(du_id=du_id)
    deaduser.du_name = du_name
    deaduser.du_reason = du_reason
    deaduser.du_level = du_level
    deaduser.du_apply_time = du_apply_time
    deaduser.du_ispass = '2'
    deaduser.save()

    deaduserurl_list = deaduser.deaduserurl.all()
    for deaduserurl in deaduserurl_list:
        deaduserurl.duu_user_name = deaduser
        deaduserurl.duu_week_url_count = duu_week_url_count
        deaduserurl.save()

    deadusersite_list = deaduser.deadusersite.all()
    #site文件处理
    dus_site_file =  request.FILES.get("sitefile", None)
    if dus_site_file:
        deadusersite_list.delete()
        baseDir = os.path.dirname(os.path.abspath(__name__))
        sitedir = os.path.join(baseDir,'dead_app','usersite')
        sitefilepath = os.path.join(sitedir,dus_site_file.name)
        sitefilew = open(sitefilepath,'w')
        for chrunk in dus_site_file.chunks():
            sitefilew.write(chrunk)
        sitefilew.close()
        sitefiler = open(sitefilepath,'r')
        #site存储
        while 1:
            lines = sitefiler.readlines(10000)
            if not lines:
                 break
            for line in lines:
                site_list = line.split(" ")
                dus_day_site_name = site_list[0]
                dus_day_site_count = site_list[1]
                result = result + dus_day_site_name + ',' + dus_day_site_count + ','
                deadusersite =  DeadUserSiteCenter()
                deadusersite.dus_user_name = deaduser
                deadusersite.dus_day_site_name = dus_day_site_name
                deadusersite.dus_day_site_count = dus_day_site_count
                deadusersite.save()

    #debug
    if dus_site_file:
        result = result + str(du_name)+','+str(du_reason)+','+str(du_level)+','+str(duu_week_url_count)
    else:
        result = "empty"
    #调用sendmail接口，通知审批人
    title = "deadlink平台配额修改审核"
    content = "<b>产品线"+du_name+"修改了配额申请，请尽快进行审核.</b>"+"<br><a href=http://cp01-spimon.epc.baidu.com:8222/person?du_id="+str(deaduser.du_id)+">点击此处进行审核</a><br>"
    receiver_path = "dead_workspace/approvers.conf"
    receiver_file = open(receiver_path,'r')
    receiver = ""
    while 1:
        line = receiver_file.readline()
        line = line.replace("\n","")
        if line:
            receiver = receiver + line +";"
        else:
            break
    email = MessageControl()
    email.set_to_mail(title, content,receiver)

    result = du_id
    #return render_to_response('apply.html', {"username":result})
    return HttpResponse(json.dumps({'result':result}))


@login_required
def hisjob(request):
    username = request.user.username
    d = {"username":username}
    return render_to_response('hisjob.html', d )

@login_required
def submit(request):
    username = request.user.username
    d = {"username":username}
    return render_to_response('submit.html', d )

@login_required
def detailjob(request):
    username = request.user.username
    d = {"username":username}
    return render_to_response('detailjob.html', d )

@login_required
def person_nopass(request):
    username = request.user.username
    d = {"username":username}
    return render_to_response('person_nopass.html', d )


@login_required
def person_pass(request):
    username = request.user.username
    d = {"username":username}
    return render_to_response('person_pass.html', d )
