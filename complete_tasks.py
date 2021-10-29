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

def solve(agents, tasks):
    
    #print("task:", tasks)
    
    #allocate agents to tasks
    #a_ind = np.random.choice(np.arange(0,len(tasks)-1), size=(len(tasks)))
    ###########
    #fill indices array with -1s
    index = np.arange(len(agents))
    index.fill(-1)
    a_ind = np.random.choice(np.arange(len(tasks)), size =len(index))
    #random.shuffle(index)
    #give a task to 
    ###########
    
    #print("First agent assigned:", a_ind)
    
    #find the euclidean distance between the task and the agent
    #agent_task_dist = similarity.euc_dist(agents, tasks, a_ind, 0)
    #generate distance matrix
    dist_matrix = similarity.gen_dist_matrix(agents)
    #calculate a similarity threshold
    #threshold = calc_threshold.calc_threshold(agents, 0.65)
    close_agents_size = 3
    #replace zeros with inf so that agents won't pass to themselves
    dist_matrix[dist_matrix == 0] = float('inf')
    stop = 500
    
    num_passes = 0
    
    time = 0
    #complete tasks
    while np.any([np.any(task > 0) for task in tasks]) and time != stop:
        
        #print("time step:", time)
        #repeat for each task
        for i in range(len(a_ind)):
            """
            #scan agents to pass
            candidate = passing.scan_close_agents(agents, i, dist_matrix, close_agents_size)
            #if the candidate is closer to the task then pass it
            if similarity.euc_dist(agents, tasks, i, a_ind[i]) > similarity.euc_dist(agents, tasks, candidate, a_ind[i]):
                print("passed from", i, "to", candidate)
                curr_task = a_ind[i]
                a_ind[i] = a_ind[candidate]
                
                #swap tasks
                #cand_task = np.where(a_ind == candidate)
                #cand_task = a_ind[candidate]
                a_ind[candidate] = curr_task
                num_passes += 1
               
                continue
            """
            progress = copy.deepcopy(tasks[i])
            #locs = np.where(tasks == progress)
            
            #agents work
            tasks[a_ind[i]] = tasks[a_ind[i]] - agents[i]
            #set negative values to 0 
            tasks[a_ind[i]][tasks[a_ind[i]] < 0] = 0
            
            #if task is complete, cut loop
            if np.all(tasks[a_ind[i]] == 0):
                #unassign completed task
                a_ind[i] = -1
                #assign new task to agent
                a_ind[i] = passing.get_new_task(i, a_ind, tasks)
                
                continue
        
            #check if the agent is stuck and force pass
            change = progress - tasks[a_ind[i]]
            #print("task status:", tasks[a_ind[i]])
            #print("change:", change)
            if np.all(change < 1):
                #scan agents to pass
                #print("agent", i, " is stuck")
                candidate = passing.scan_close_agents(agents, i, dist_matrix, close_agents_size)
                #swap tasks
                cand_task = a_ind[candidate]
                a_ind[candidate] = a_ind[i]
                a_ind[i] = cand_task
                #print("task was passed to", a_ind[i])
                num_passes += 1
                
        time += 1
    #print("Sim end!")
    #print("time:",time)
    #print("num passes:", num_passes)
    num_task_completed = 0
    for task in tasks:
        if (np.all(task <= 0)):
            num_task_completed += 1
    #print("num tasks completed",num_task_completed)
    return time, num_task_completed, num_passes
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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