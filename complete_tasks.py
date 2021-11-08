#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 18:05:50 2021

@author: carolineskalla
"""

#function handles the whole simulation
import numpy as np
import random
import similarity
import calc_threshold
import passing
import copy

def solve(agents, tasks, close_agents_size):
    
    #calculate relative threshold
    threshold = calc_threshold.calc_threshold(agents, close_agents_size)
    #calculate the distances between the agents 
    dist_matrix = similarity.gen_dist_matrix(agents)
    
    #allocate agents to tasks
    a_ind = np.random.choice(np.arange(0,len(agents)-1), size=(len(tasks)))
  
  
    stop = 2000
    tasks_completed = 0
    time = 0
    #complete tasks
    while len(tasks) > 0 and time != stop:
        
        #for each time step:
        
        #mark progress
        progress = copy.deepcopy(tasks)
        #tasks work
        tasks = tasks - agents[a_ind,:]
        #tasks[tasks < 0] = 0 #set negative values to 0
        tasks = np.where(tasks < 0, 0, tasks)
        
        #check if any tasks are stuck
        t = np.arange(len(tasks))
        stuck_tasks = t[np.all(progress - tasks < 1, axis = 1)] #returns t or f for every index of task array
        print("stuck tasks: ",stuck_tasks)
        
        #find a new agent for stuck tasks
        a_ind = passing.pass_new_agent(tasks, agents, a_ind, stuck_tasks, threshold, dist_matrix)
        print("a_ind:", a_ind)
        
        #check for completed tasks
        finished = np.all(tasks <= 0, axis = 1).transpose()
        print("num finished tasks", len(tasks[finished]))
        
        #increase completed tasks counter
        tasks_completed += len(tasks[finished])
        
        if len(tasks[finished] > 0):
            #erase tasks
            tasks = np.delete(tasks, t[finished], axis=0)
            #erase task in a_ind to free agent
            a_ind = np.delete(a_ind, t[finished], axis=0)
        
      
        
                
        time += 1
    #print("Sim end!")
    #print("time:",time)
    #print("num passes:", num_passes)
    """
    num_task_completed = 0
    
    for task in tasks:
        if (np.all(task <= 0)):
            num_task_completed += 1
            
     """       
   
    
    #print("num tasks completed",tasks_completed)
    return time, tasks_completed
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
"""
def complete_tasks(agents, tasks, stop):
  
    
    time = 0 #tracks time in simulation
    tasks_solved = np.zeros(len(tasks)) #tracks which tasks have been solved
    #abandon_timer = np.zeros(len(agents)) #tracks how long agents have been working on a task
    #orig_tasks = copy.deepcopy(tasks) #a copy of the origional state of the task list
    
    
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
                    #abandon_timer[i] = 0
                    #look for new task
                    indices[i] = assign3.new_rand_task(i, agents, tasks, indices, threshold, max_agents_to_task, abandon_timer)
                else:
                    #agents work
                    oldTask = tasks[indices[i]]
                    tasks[indices[i]]= tasks[indices[i]]- agents[i]
                    #if task has not changed, increase abandon timer
                         #abandon_timer[i] +=1
                
                #print("task progress:", tasks)
            #if agent doesn't have task
            else:
                indices[i] = assign3.new_rand_task(i, agents, tasks, indices, threshold, max_agents_to_task, abandon_timer)
            i+=1
        time += 1
    #sum up the number of tasks solved
    num_tasks_solved = np.sum(tasks_solved)
    print(tasks)
    return time, num_tasks_solved
"""