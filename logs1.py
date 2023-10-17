#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 18:20:03 2022

@author: hossna
"""
#Consider the standard web log file in assets/logdata.txt. This file records 
#the access a user makes when visiting a web page (like this one!). 
#Each line of the log has the following items:

#    a host (e.g., '146.204.224.152')
#    a user_name (e.g., 'feest6811' note: sometimes the user name is missing! In this case, use '-' as the value for the username.)
#    the time a request was made (e.g., '21/Jun/2019:15:45:24 -0700')
#    the post request type (e.g., 'POST /incentivize HTTP/1.1' note: not everything is a POST!)

#Your task is to convert this into a list of dictionaries, where each dictionary looks like the following:

#example_dict = {"host":"146.204.224.152", 
#                "user_name":"feest6811", 
#                "time":"21/Jun/2019:15:45:24 -0700",
#                "request":"POST /incentivize HTTP/1.1"}

import re
with open("new.txt", "r") as file:
    logdata = file.read()
    pattern="""
    (?P<host>\d*\.\d*\.\d*\.\d*)
    (\s\-\s)
    (?P<user_name>(\-|\w*))
    (\s\[)
    (?P<time>\d*\/\w*\/\d*\:\d*\:\d*\:\d*\s\-\d*) 
    (\]\s)
    (?P<request>\".*?\")""" #match everything between ""
    
    keys=('host','user_name','time','request')#keys of dictionary should be immutable like tupale
    value1=[]
    value2=[]
    value3=[]
    value4=[]
    result={}
    
  
    for item in re.finditer(pattern,logdata,re.VERBOSE):
        value1.append(item.groupdict()['host'])
        value2.append(item.groupdict()['user_name'])
        value3.append(item.groupdict()['time'])
        value4.append(item.groupdict()['request'])

result={keys[0]:value1,keys[1]:value2,keys[2]:value3,keys[3]:value4}#tuple starts from 0
#result={'host':value1}


      
print(result)