#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 17:06:59 2022

@author: hossna
"""
def reverseString(x):
    reverse=str(x)[::-1]
    return str(x)==reverse
x=120
print(reverseString(x))

def isPalindrome(x):
        temp = x
        reverse = 0
        while x > 0:
            reminder= x%10
            reverse=reverse*10+reminder
            x=x//10
            #reverse *= 10
            #reverse += x % 10
            #x //= 10
        return temp == reverse
x=111
#x//=10
print (isPalindrome(x))