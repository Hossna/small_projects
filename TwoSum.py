#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 16:23:21 2022

@author: hossna
"""

#Given an array of integers nums and an integer target, return indices 
#of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, 
#and you may not use the same element twice.

#You can return the answer in any order.
class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i
nums=[4,3,5]
target=9
out=Solution()
d=out.twoSum(nums,target)
print(d)
        
#  Other solutions:
############################################################################

#class Solution:
        #def twoSum(self, nums: List[int], target: int) -> List[int]:
        #the arrow (->) allows us to type hint the return type, which 
        #is a list containing integers.
def twoSum(nums,target):
    #d=[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if target==nums[i]+nums[j]:
                #d.append(nums[i])
                #d.append(nums[j])
                return ([nums[i],nums[j]])
    #return d       
                    
#nums = [1,2,3,4,5,6,7,8,9,10]
#nums = [2,3,4,4,6,8,9,10]
#target = 8

#print("mine",twoSum(nums,target)) 

#  Other solutions:
############################################################################

