#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 16:46:05 2021

@author: carolineskalla
"""
import numpy as np
import similarity
#matrix array testing




agents = np.array([[0,0,0], [1,1,1], [2,2,2]])
x = agents[np.any(agents > 0, axis =1)]
print(x)







"""
x = np.zeros((2,2))
y = x + 2

z = x - y

x1 = np.arange(5)
y1 = np.arange(5)
z1 = x1 - y1[::-1]

z2 = x1[:] - y1

A = np.array([0,1,2])
agents = np.array([[0,0,0], [1,1,1], [2,2,2]])
a, b= np.meshgrid(A,A)
b.T
print(a)

print(b)
c = np.sqrt(np.sum((agents[a] - agents[b])**2, axis=0))
print(c)
#print(c**2)

matrix2 = similarity.gen_dist_matrix(agents)
print(matrix2)
"""