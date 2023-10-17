#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 21:42:28 2022

@author: hossna
"""
##Write a function to find the longest common prefix string amongst
# an array of strings.#If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs: return ''
        s_min=min(strs)
        s_max=max(strs)
        for i,items in enumerate(s_min):
            if items != s_max[i]:
                return s_min[:i]
        return s_min

#a=["Hossna","Sayeh","Elly"]
#b=["Mike","Babak","Ali"]
#x=zip(a,b)
strs=["flight","flow","flee","f"]
out=Solution()
print(out.longestCommonPrefix(strs))
#for i,b in enumerate(zip(*strs)):
#    print("i",i)
#    print("b",b)
print("min",min(strs))
print("max",max(strs))

#print(list(x))
#print(tuple(x))        