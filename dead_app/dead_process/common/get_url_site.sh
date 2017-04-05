#!/bin/bash


function Usage()
{
    echo "Usage: sh get_url_site.sh urlfile "
}

function get_site()
{
    awk '{
        if($1~/http:\/\//){
            url=substr($1,8);
        }else if($1~/https:\/\//){
            url=substr($1,9);
        }
        else{
            url=$1;
        }
        if(url!=""){
            split(url,a,"/");
            print a[1];
        }
    }' $urlfile &> $sitefile
    if [ -s $sitefile ];then
        cat $sitefile | sort -n | uniq -c | awk '{print $2,$1}' &> $sitecountfile
    else
        touch $sitecountfile 
    fi
}

if [ $# -ne 1 ];then
    Usage
    exit 1
else
    urlfile=$1
    sitefile=$urlfile.site
    sitecountfile=$urlfile.site.count
    get_site
fi


