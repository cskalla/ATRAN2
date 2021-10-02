#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 10:50:57 2021

@author: carolineskalla
"""

import numpy as np


def similar(agent1, agent2):
    print("agent1", agent1)
    print("agent2", agent2)
    #use the shorter length (smaller number of skills)
    length = min(len(agent1), len(agent2))
    print("length", length)
    count = 0
    for i in range(length):
        print(agent1[i])
        print(agent2[i])
        if (agent1[i] > 0) and (agent2[i] > 0):
            count += 1
    return(count/length)
    
    
"""        
x = np.array([1,1,1])  
y = np.array([0.5,0,0])
similar(x,y)
"""