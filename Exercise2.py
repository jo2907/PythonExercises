#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 11:58:42 2023

@author: joparker
"""
import numpy as np 
# Q2a - dot product of two vectors
a = [1,2]
b = [6,5,4]
avec = np.array(a)
bvec = np.array(b)
def dotvec(a,b):
    if len(a) == len(b):
        dp = np.dot(a,b)
        return dp
    else:
        print("Error: vector lengths must be the same")
        
       

print(dotvec(avec,bvec))

# Q2b - product of matrices
A = np.array([ [1, 2],[3,4],[5,6]]) 
B = np.array([ [5, 6,8],[7,8,9]]) 
def matrixmultip(a,b):

    # if no. of rows of a == no. of cols of b
    if A.shape[1] == B.shape[0]:
        product = np.matmul(a,b)
        return product
    else:
        print("Error: Incorrect matrix dimensions")

print(matrixmultip(A,B))