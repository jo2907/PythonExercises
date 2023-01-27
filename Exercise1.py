#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 11:24:17 2023

@author: joparker
"""
from math import pi
N = 100
lst = []
for i in range (N):
    listx = 8/((4*i +1)*(4*i+3))
    lst.append(listx)

approxpi = sum(lst)
print(approxpi)
error = abs(pi - approxpi)
print(error)