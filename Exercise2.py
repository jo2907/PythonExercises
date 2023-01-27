#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 11:58:42 2023

@author: joparker
"""
import numpy as np 
a = [1,2,3]
b = [6,5,4]
avec = np.array(a)
bvec = np.array(b)
def dotvec(a,b):
    dp = np.dot(a,b)
    return dp

print(dotvec(avec,bvec))
