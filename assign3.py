#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 16:37:33 2021

@author: carolineskalla
"""

import numpy as np
import random
import similarity
from more_itertools import sort_together

#retun a random unclaimed task or -1
def new_rand_task(i, agents, tasks, indices, threshold, max_agents_to_task, abandon_timer):
    #identify unclaimed tasks
    unclaimed_t_ind = check_unclaimed(agents, tasks, indices)
    if len(unclaimed_t_ind) > 0:
        #pick a random unclaimed task
        ind = random.randint(0,len(unclaimed_t_ind)-1)
        return unclaimed_t_ind[ind]
        
    else:
        return -1
    

def init_assign_tasks(agents, tasks, threshold, max_agents_to_task, abandon_timer):
    #agents are randomly assigned to tasks
  
    #tasks can only have one agent, some agents may not have a task
    #index will contain min(len(tasks),len(agents)) number of ints between 0 and len(tasks), and if there are more 
    #index = [random.randint(0,len(tasks)-1) for i in range(len(agents))]
    #options = np.array(range(0, len(tasks)))
    #
    #if len(agents) <= len(tasks):
        #pick random indeices of tasks
        #indices = np.random.choice(options, len(agents))
    #else:
        #pick len(task) number tasks and assign to agents, otherwise fill with nan
       # l = [i for i in range(0, len(tasks))]
        #print(l)
        #random.shuffle(l)
       # print(l)
   indices = [-1 for i in range(len(agents))]
      
   for j in range(len(agents)):
            #print("hi2")
        indices[j] = new_rand_task(j, agents, tasks, indices, threshold, max_agents_to_task, abandon_timer)
            
        #indices[len(tasks)] = new_task(len(tasks), agents, tasks, indices, threshold)
        #indices[len(tasks) + 1] = new_task(len(tasks + 1), agents, tasks, indices, threshold)
   random.shuffle(indices)
   return indices



#helper functions

#finds the tasks that are not currently assigned to agents
def check_unclaimed(agents, tasks, indices):
    unclaimed_t_ind = []
    task_ind = [i for i in range(0, len(tasks))]
    for t in task_ind:
        #if no agents are working on task t
        if indices.count(t) < 1:
            unclaimed_t_ind.append(t)
    return unclaimed_t_ind

#find the agents that are currently stuck on their task
def stuck_agents(agents, tasks, indices, abandon_timer):
    stuck_agents = []
    for i in range(len(agents)):
        if abandon_timer[i] > 1:
            stuck_agents.append(i)
    return stuck_agents


#finds the euclidian distance between an agent and a task    
def agent_task_sim(agents, tasks, a_ind, t_ind):
    #get agents 
    agent = agents[a_ind]
    task = tasks[t_ind]
    # finding sum of squares
    sum_sq = np.sum(np.square(agent - task))
 
    # Doing squareroot and
    # printing Euclidean distance
    #print(np.sqrt(sum_sq))
    return np.sqrt(sum_sq)

#returns the indices of any other agents working on the task
def is_compatible(agents, indices, i, t_ind, threshold):
    if indices.count(t_ind) < 1:
        return True
    else:
        a_ind = agents_on_task(indices, t_ind)        
        sims = np.zeros(len(a_ind))
        j = 0
        for a in a_ind:
            sims[j] = similarity.euc_dist(agents, i, a)
            j+=1
        #check to see if all agents working on this task pass the similarity threshold
        if np.all(sims < threshold):
            return True
        else:
            return False
  
#returns a list of agents that are currently working on a task
def agents_on_task(indices, t_ind):
    
    agt_list = []
    
    for i in range(len(indices)) :
        if indices[i] == ( t_ind) :
            agt_list.append(i)
    return agt_list
