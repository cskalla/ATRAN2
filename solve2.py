#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 08:43:15 2021

@author: carolineskalla
"""
import numpy as np
import copy
import assign_tasks2

def complete_tasks(agents, tasks, indices, stop, threshold, max_agents_to_task, abandon_timer):
    #check if agent has a task
    #if it does have a task check if task is not complete
        #check if abandon timer has run out
            #if so, try to pass task
                #pass
            #if not, abandon and erase progress
    #if has task but it is complete
    #mark as complete and 
        #if not, work on task
    #if agent has no task
    #call new task
    
    time = 0 #tracks time in simulation
    tasks_solved = np.zeros(len(tasks)) #tracks which tasks have been solved
   # abandon_timer = np.zeros(len(agents)) #tracks how long agents have been working on a task
    orig_tasks = copy.deepcopy(tasks) #a copy of the origional state of the task list
    
    
    #continue until all tasks are negative or reach emergency stop
    while np.any([np.any(task > 0) for task in tasks]) and time != stop:
        i = 0 #index of current agent
        for a in agents:
            
            #check if agent has task
            if indices[i] != -1: 
                #if a task is entirely negative, mark complete
                if np.all(tasks[indices[i]] < 0):  
                    #make sure task is 1 in task_solved array
                    tasks_solved[indices[i]] = 1
                    indices[i] = -1 #set back to -1 (indicating no task)
                    abandon_timer[i] = 0
                    #look for new task
                    indices[i] = assign_tasks2.new_task(i, agents, tasks, indices, threshold, max_agents_to_task, abandon_timer)
                else:
                    #agents work
                    oldTask = tasks[indices[i]]
                    tasks[indices[i]]= tasks[indices[i]]- agents[i]
                    #if task has not changed, increase abandon timer
                    if np.all(oldTask == tasks[indices[i]]):
                        abandon_timer[i] +=1
                
                #print("task progress:", tasks)
            #if agent doesn't have task
            else:
                indices[i] = assign_tasks2.new_task(i, agents, tasks, indices, threshold, max_agents_to_task, abandon_timer)
            i+=1
        time += 1
    #sum up the number of tasks solved
    num_tasks_solved = np.sum(tasks_solved)
    return time, num_tasks_solved
    