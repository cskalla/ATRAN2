#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 10:20:03 2021

@author: carolineskalla
"""

import numpy as np
import matplotlib.pyplot as plt
"""
#create matrices
m1 = np.arange(5)
m2 = np.arange(5)

print("m1:", m1)
print("m2:", m2)

#element wise multiplication

print(m1*m2)

#exponent
y = 10**m1
print(y)

adivvals = 10**(np.linspace(0.1, 0.2, 20)*np.linspace(-6, 7, 20))
gdivvals = 10**(0.2*np.linspace(-3, 5, 10))
print("adivvals:", adivvals)
print("gdivvals:", gdivvals)

plt.plot(np.arange(20), adivvals, gdivvals)
"""
"""
num_close_agents = 6
x = np.exp(-(np.arange(num_close_agents)**2)/3)
y = x/np.sum(x)
print(y[::-1])
print(sum(y))
"""
agents = np.array([[1,1], [1,1,]])
a_ind = np.array([[0,1], [1,1]])

x = (agents-a_ind)
print(x)
y = np.any(x > 0, axis = 1)
print(y)
print(a_ind[y])
