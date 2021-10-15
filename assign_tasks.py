#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 13:22:38 2021

@author: carolineskalla
"""
import random
import numpy as np
import similarity
#simulation where communication is allowed
def init_assign_tasks_comm(agents, tasks):
    #agents are randomly assigned to tasks
  
    #all agents get a task and agents can get the same task 
    index = [random.randint(0,len(tasks)-1) for i in range(len(agents))]

    return index

#simulation where communication is not allowed (at all)
def init_assign_tasks_nocomm(agents, tasks):
    #agents are randomly assigned to tasks
  
    #tasks can only have one agent, some agents may not have a task
    #index will contain min(len(tasks),len(agents)) number of ints between 0 and len(tasks), and if there are more 
    #index = [random.randint(0,len(tasks)-1) for i in range(len(agents))]
    options = np.array(range(0, len(tasks)))
    #
    if len(agents) <= len(tasks):
        #pick random indeices of tasks
        indices = np.random.choice(options, len(agents))
    else:
        #pick len(task) number tasks and assign to agents, otherwise fill with nan
        l = [i for i in range(0, len(tasks))]
        print(l)
        random.shuffle(l)
        print(l)
        indices = l + [-1 for i in range(len(tasks), len(agents))]
        
    return indices

def new_task_comm(agents, tasks, index):
    #agents are randomly assigned to tasks 
    taskLoc = random.randint(0,len(tasks)-1)
    return taskLoc
            
        

def new_task_nocomm(agents, tasks, indices):
    #agents are randomly assigned to tasks 
    #shuffle task indices for random selection
    randTasks = [i for i in range(0, len(tasks))]
    random.shuffle(randTasks)
   
    for i in range(0, len(randTasks)):
        taskLoc = randTasks[i]
    #taskLoc = random.randint(0,len(tasks)-1)
    #figure out if any other agents already are working on this task
        a = np.where(indices == taskLoc)
        if len(a[0]) <= 1:
            return taskLoc     
    return -1

def new_task_simcomm(i, agents, tasks, indices, threshold):
    #agents are randomly assigned to tasks 
    #shuffle task indices for random selection
    randTasks = [i for i in range(0, len(tasks))]
    random.shuffle(randTasks)
   
    for i in range(0, len(randTasks)):
        taskLoc = randTasks[i]
    #taskLoc = random.randint(0,len(tasks)-1)
    #figure out if any other agents already are working on this task
        a = np.where(indices == taskLoc)
        if len(a[0]) <= 1:
            return taskLoc  
        else:
            sims = np.zeros(len(a[0]))
            h = 0
            for ag in a[0]:
                sims[h] = similarity.similar(agents[i], agents[ag])
                h+=1
            #check to see if all agents working on this task pass the similarity threshold
            if np.all(sims >= threshold):
                return taskLoc
            
            
    return -1


def new_task_DFD_simcomm(i, agents, tasks, indices):
    #agents are randomly assigned to tasks 
    #shuffle task indices for random selection
    randTasks = [i for i in range(0, len(tasks))]
    random.shuffle(randTasks)
   
    for i in range(0, len(randTasks)):
        taskLoc = randTasks[i]
    #taskLoc = random.randint(0,len(tasks)-1)
    #figure out if any other agents already are working on this task
        a = np.where(indices == taskLoc)
        if len(a[0]) <= 1:
            return taskLoc  
        else:
            sims = np.zeros(len(a[0]))
            h = 0
            for ag in a[0]:
                sims[h] = similarity.DFD_similar(agents[i], agents[ag])
                h+=1
            #check to see if all agents working on this task pass the similarity threshold
            if np.all(sims == True):
                return taskLoc
            
            
    return -1


