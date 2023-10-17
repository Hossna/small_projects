#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 13:40:30 2022

@author: hossna
"""
#Find the smallest positive number missing from an unsorted array
def smallest_intiger(A):
    size_A=len(A)
    new_array=np.array(range(1,size_A+1))
    smallest=0
    for num in new_array:
        if not num in A:
            smallest=num
            return(smallest)
            break#it does not break too with return it also works
            #sys.exit() #this is not good!!
import numpy as np   
#import sys         
A=np.array([-1,-2])
B=np.array([6,2,3,4,1,1])  
C=np.array([2,3,7,6,8,-1,-10,15])  
D=np.array([1,1,0,-1,-2])                  
print("the smallest positive integir is missing in an unsortted array A:", smallest_intiger(A))
print("the smallest positive integir is missing in an unsortted array B:", smallest_intiger(B))
print("the smallest positive integir is missing in an unsortted array C:", smallest_intiger(C))
print("the smallest positive integir is missing in an unsortted array D:", smallest_intiger(D))


def minpositive(A):
  
    size_A = len(A)
    N = set(range(1, size_A+2))
    return min(N-set(A)) #gets the min value using the N integers
#set A = {10, 20, 30, 40, 80}
#set B = {100, 30, 80, 40, 60}

#set A - set B = {10, 20}
#set B - set A = {100, 60}

#Explanation: A - B is equal to the elements present in A but not in B
#             B - A is equal to the elements present in B but not in A






