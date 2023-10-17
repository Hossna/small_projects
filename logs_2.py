#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 15:55:28 2022

@author: hossna
"""

import re
def logs():
    with open("logdata.txt", "r") as file:
        logdata = file.read()
         #the ?P indicates that this is an extension to basic regexes, 
         #and <name> is the dictionary
         # key we want to use wrapped in <>.
        pattern1="""
        (?P<host>\d*\.\d*\.\d*\.\d*)
        (\s\-\s)
        (?P<user_name>(\-|\w*))
        (\s)
        (?P<time>\[.*\])
        (\s)
        (?P<request>\".*\")"""
        pattern2="""
        (?P<host>.*)
        (\s\-\s)
        (?P<user_name>(\-|\w*))
        (\s\[)
        (?P<time>.*)
        (\]\s\")
        (?P<request>.*)
        (\"\s.*)"""
        result=[]
      
        for item in re.finditer(pattern2,logdata,re.VERBOSE):
            result.append(item.groupdict())
    return result

#print(logs())
assert len(logs()) == 979

one_item={'host': '146.204.224.152',
  'user_name': 'feest6811',
  'time': '21/Jun/2019:15:45:24 -0700',
  'request': 'POST /incentivize HTTP/1.1'}
assert one_item in logs(), "Sorry, this item should be in the log results, check your formating"