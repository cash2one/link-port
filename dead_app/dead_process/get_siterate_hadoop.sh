#!/bin/bash

#cat part-00799 | python redis_control.py 
hadoop fs -ls /user/rd/chenping01/site_value2int | while read line
do
    file=`echo $line | awk '{print $NF}'`
    echo $file
    hadoop fs -cat $file | python redis_control.py
done    
