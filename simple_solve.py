#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 13:22:59 2021

@author: carolineskalla
"""
import numpy as np
import assign_tasks

def solve_tasks(agents, tasks, index, stop):
    time = 0
    #check to see if all tasks are complete
    print("entering while loop")
    while np.any([np.any(task > 0) for task in tasks]) and time != stop:
        print("time = ", time)
        i = 0
        for a in agents:
            if np.all(tasks[index[i]] < 0):
                index[i] = assign_tasks.new_task(agents, tasks)
            print("agent works on task")
            tasks[index[i]]= tasks[index[i]]- agents[i]
            print("task progress:", tasks)
            i+=1
        time += 1
    return time