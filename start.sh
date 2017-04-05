#!/bin/bash
datenow=`date "+%Y%m%d"`
ps -ef | grep 8222 | grep -v grep | awk '{print $2}' | xargs kill -9

nohup python manage.py runserver 0.0.0.0:8222 &>log/log.$datenow &
