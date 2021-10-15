#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 13:22:59 2021

@author: carolineskalla
"""
import numpy as np
import assign_tasks
import math
import random
import copy
import similarity

def solve_tasks_comm(agents, tasks, indices, stop):
    time = 0
    #check to see if all tasks are complete
    #print("entering while loop")
    abandon_timer = np.zeros(len(agents))
    orig_tasks = copy.deepcopy(tasks)
    tasks_solved = np.zeros(len(tasks))
    
    #continue until all tasks are negative or reach emergency stop
    while np.any([np.any(task > 0) for task in tasks]) and time != stop:
        #print("time = ", time)
        i = 0
        for a in agents:
            
            #check if agent has task
            if indices[i] != -1: 
                
                #if abandon timer is over threshold, agent abandons
                if abandon_timer[i] >= 1:
                    
                    #before abandoning, attempt to pass
                    #ntry = 5 #how many agents to try passing to before abandoning
                    #generate list of agents to pass to
                    #picka random agent
                    a_ind = random.randint(0, len(agents)-1)
                    indices[a_ind] = indices[i]
                    indices[i] = -1
                    abandon_timer[i] = 0
                    """
                    #erase task progress
                    tasks[indices] = orig_tasks[indices]
                    abandon_timer[i] = 0
                    indices[i] = -1 #set back to NaN
                    """
                #if a task is entirely negative, mark complete
                elif np.all(tasks[indices[i]] < 0):    
                    tasks_solved[indices[i]] = 1
                    indices[i] = -1 #set back to NaN
                    abandon_timer[i] = 0
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
                indices[i] = assign_tasks.new_task_nocomm(agents, tasks, indices)
            i+=1
        time += 1
     #sum up the number of tasks solved
    num_tasks_solved = np.sum(tasks_solved)
    return time, num_tasks_solved


def solve_tasks_nocomm(agents, tasks, indices, stop):
    time = 0
    #check to see if all tasks are complete
    #print("entering while loop")
    abandon_timer = np.zeros(len(agents))
    orig_tasks = copy.deepcopy(tasks)
    
    
    #continue until all tasks are negative or reach emergency stop
    while np.any([np.any(task > 0) for task in tasks]) and time != stop:
        #print("time = ", time)
        i = 0
        for a in agents:
            
            #check if agent has task
            if indices[i] != -1: 
                
                #if abandon timer is over threshold, agent abandons
                if abandon_timer[i] >= 5:
                    #erase task progress
                    tasks[indices] = orig_tasks[indices]
                    abandon_timer[i] = 0
                    indices[i] = -1 #set back to NaN
                    
                #if a task is entirely negative, mark complete
                elif np.all(tasks[indices[i]] < 0):                   
                    indices[i] = -1 #set back to NaN
                    abandon_timer[i] = 0
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
                indices[i] = assign_tasks.new_task_nocomm(agents, tasks, indices)
            i+=1
        time += 1
    return time

def solve_tasks_sim_comm(agents, tasks, indices, stop, sim_threshold):
    time = 0
    tasks_solved = np.zeros(len(tasks))
    #check to see if all tasks are complete
    #print("entering while loop")
    abandon_timer = np.zeros(len(agents))
    orig_tasks = copy.deepcopy(tasks)
    
    
    #continue until all tasks are negative or reach emergency stop
    while np.any([np.any(task > 0) for task in tasks]) and time != stop:
        #print("time = ", time)
        i = 0
        for a in agents:
            
            #check if agent has task
            if indices[i] != -1: 
                
                #if abandon timer is over threshold, agent abandons
                if abandon_timer[i] >= 1:
                    
                    #before abandoning, attempt to pass
                    ntry = 5 #how many agents to try passing to before abandoning
                    #generate list of agents to pass to
                    #picka random agent
                    #a_ind = random.randint(0, len(agents)-1)
                    #indices[a_ind] = indices[i]
                    #indices[i] = -1
                    #try passing tasks to ntry agents
                    shuffled_agents = np.array(range(len(agents)))
                    for j in range(ntry):
                        a_ind = shuffled_agents[i]
                        #sim = similarity.similar(a, agents[a_ind])
                        sim = similarity.euc_dist(agents, i, a_ind)
                        if sim < sim_threshold:
                            indices[a_ind] = indices[i]
                            abandon_timer[i] = 0
                            break
                        #if task was not passed to any of agents
                        elif(j== ntry-1):
                           #erase task progress
                           tasks[indices[i]] = orig_tasks[indices[i]]
                           abandon_timer[i] = 0
                           indices[i] = -1 #set back to 0
                            
                            
                    #abandon_timer[i] = 0
                    """
                    #erase task progress
                    tasks[indices] = orig_tasks[indices]
                    abandon_timer[i] = 0
                    indices[i] = -1 #set back to NaN
                    """
                #if a task is entirely negative, mark complete
                elif np.all(tasks[indices[i]] < 0):  
                    #make sure task is 1 in task_solved array
                    tasks_solved[indices[i]] = 1
                    indices[i] = -1 #set back to NaN
                    abandon_timer[i] = 0
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
                indices[i] = assign_tasks.new_task_simcomm(i, agents, tasks, indices, sim_threshold)
            i+=1
        time += 1
    #sum up the number of tasks solved
    num_tasks_solved = np.sum(tasks_solved)
    return time, num_tasks_solved

##########################################
def solve_tasks_DFD_sim_comm(agents, tasks, indices, stop):
    time = 0
    tasks_solved = np.zeros(len(tasks))
    #check to see if all tasks are complete
    #print("entering while loop")
    abandon_timer = np.zeros(len(agents))
    orig_tasks = copy.deepcopy(tasks)
    
    
    #continue until all tasks are negative or reach emergency stop
    while np.any([np.any(task > 0) for task in tasks]) and time != stop:
        #print("time = ", time)
        i = 0
        for a in agents:
            
            #check if agent has task
            if indices[i] != -1: 
                
                #if abandon timer is over threshold, agent abandons
                if abandon_timer[i] >= 1:
                    
                    #before abandoning, attempt to pass
                    ntry = 5 #how many agents to try passing to before abandoning
                    #generate list of agents to pass to
                    #picka random agent
                    #a_ind = random.randint(0, len(agents)-1)
                    #indices[a_ind] = indices[i]
                    #indices[i] = -1
                    #try passing tasks to ntry agents
                    shuffled_agents = np.array(range(len(agents)))
                    for j in range(ntry):
                        a_ind = shuffled_agents[i]
                        sim = similarity.DFD_similar(a, agents[a_ind])
                        #if sim returns true, pass task
                        if sim:
                            indices[a_ind] = indices[i]
                            abandon_timer[i] = 0
                            break
                        #if task was not passed to any of agents
                        else: #sim returned false
                           #erase task progress
                           tasks[indices[i]] = orig_tasks[indices[i]]
                           abandon_timer[i] = 0
                           indices[i] = -1 #set back to 0
                            
                            
                    #abandon_timer[i] = 0
                    """
                    #erase task progress
                    tasks[indices] = orig_tasks[indices]
                    abandon_timer[i] = 0
                    indices[i] = -1 #set back to NaN
                    """
                #if a task is entirely negative, mark complete
                elif np.all(tasks[indices[i]] < 0): 
                    #make sure task is 1 in task_solved array
                    tasks_solved[indices[i]] = 1
                    indices[i] = -1 #set back to NaN
                    abandon_timer[i] = 0
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
                indices[i] = assign_tasks.new_task_DFD_simcomm(i, agents, tasks, indices)
            i+=1
        time += 1
    #sum up the number of tasks solved
    num_tasks_solved = np.sum(tasks_solved)
    return time, num_tasks_solved 