#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 11:08:04 2021

@author: carolineskalla
"""
import numpy as np
import alt_assign_tasks


def solve_tasks(agents, tasks, index, stop):
    time = 0
    #check to see if all tasks are complete
    print("entering while loop")
    abandon_timer = np.zeros(len(agents))
    
    #continue until all tasks are negative or reach emergency stop
    while np.any([np.any(task > 0) for task in tasks]) and time != stop:
        #print("time = ", time)
        i = 0
        for a in agents:
            #if abandon timer is over threshold, agent finds new task
            if abandon_timer[i] <= 5:
                index[i] = alt_assign_tasks.new_task(agents, tasks)
                abandon_timer[i] = 0
            #if a task is entirely negative, assign agent new task
            if np.all(tasks[index[i]] < 0):
                index[i] = alt_assign_tasks.new_task(agents, tasks)
                abandon_timer[i] = 0
            print("agent works on task")
            oldTask = tasks[index[i]]
            #work
            tasks[index[i]]= tasks[index[i]]- agents[i]
            #if task has not changed, increase abandon timer
            if np.all(oldTask == tasks[index[i]]):
                abandon_timer[i] +=1
            
            print("task progress:", tasks)
            i+=1
        time += 1
    return time