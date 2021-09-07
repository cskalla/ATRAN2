#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 13:22:59 2021

@author: carolineskalla
"""
import numpy as np

def solve_tasks(agents, tasks, index, stop):
    time = 0
    #check to see if all tasks are complete
    while np.any([np.any(task > 0) for task in tasks]) or time != stop:
        i = 0
        for a in agents:
            tasks[index[i]]= tasks[index[i]]- agents[i]
            i+=1
        time += 1
    return time