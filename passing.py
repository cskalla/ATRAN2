#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 17:11:24 2021

@author: carolineskalla
"""
import numpy as np
import random
import similarity
import copy

def pick_close_agent(a_ind, close_agent_matrix, close_agents_size):
        #print("current agent: agent #", a_ind)

        #sort the distance matrix
        #close_agents = np.argsort(dist_matrix[a_ind])
        
        #find three agent candidates
        #agent_circle = close_agents[0:3]
        #print("agent circle is:", agent_circle)
        #pick a random agent from the small cirle to pass the task to
        
        agent_circle = close_agent_matrix[a_ind]
        #print(close_agent_matrix)
        #print(agent_circle)
        p = pass_prob(close_agents_size)
        a_ind = np.random.choice(agent_circle, replace=True, p=p)
        #print(a_ind)
        #print("passes to: agent #", a_ind)
        #agent_task_dist = similarity.euc_dist(agents, tasks, a_ind, 0)
        #print("new agent task distance:", agent_task_dist)
       # print("\n")
        return int(a_ind)
    
    
def get_new_task(i, a_ind, tasks):
    #identify which tasks are not taken
    """
    unclaimed = []
    for t in range(len(tasks)):
        if t not in a_ind:
            unclaimed.append(t)
    unclaimed = np.array(unclaimed)
    """
    task_options = np.arange(len(tasks))
    unclaimed = task_options[np.isin(task_options, a_ind)]
    #task_candidates[np.all(a_ind != task_candidates)]
    #a_ind2 = copy.deepcopy(a_ind) + np.zeros((range(len(a_ind), len(tasks))))
    #np.argsort(a_ind2)
    
   # unclaimed =  task candidates
    unclaimed_uncomplete = unclaimed[np.any(tasks[unclaimed] > 0)]
    unclaimed_uncomplete = [ta for ta in unclaimed if np.any(ta > 0)]
    unclaimed_uncomplete = np.array(unclaimed_uncomplete)
    #print("unclaimed:", unclaimed_uncomplete)
    if len(unclaimed_uncomplete) == 0:
        return -1
    else:
        return unclaimed_uncomplete[random.randint(0, len(unclaimed_uncomplete) -1)]
        
def pass_prob(close_agents_size):   
    x = np.exp(-(np.arange(close_agents_size)**2)/3)
    y = x/np.sum(x)
    return y[::-1]   
        
        
    

            