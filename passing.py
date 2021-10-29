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

def scan_close_agents(agents, a_ind, dist_matrix, close_agents_size):
        #print("current agent: agent #", a_ind)

        #sort the distance matrix
        close_agents = np.argsort(dist_matrix[a_ind])
        
        #find three agent candidates
        agent_circle = close_agents[0:3]
        #print("agent circle is:", agent_circle)
        #pick a random agent from the small cirle to pass the task to
        p = np.array([1/6, 2/6, 3/6])
        a_ind = np.random.choice(agent_circle, replace=True, p=p)
        #print("passes to: agent #", a_ind)
        #agent_task_dist = similarity.euc_dist(agents, tasks, a_ind, 0)
        #print("new agent task distance:", agent_task_dist)
       # print("\n")
        return a_ind
    
    
def get_new_task(i, a_ind, tasks):
    #identify which tasks are not taken
    unclaimed = []
    for t in range(len(tasks)):
        if t not in a_ind:
            unclaimed.append(t)
    unclaimed = np.array(unclaimed)
    #task_candidates[np.all(a_ind != task_candidates)]
    #a_ind2 = copy.deepcopy(a_ind) + np.zeros((range(len(a_ind), len(tasks))))
    #np.argsort(a_ind2)
    
   # unclaimed =  task candidates
    unclaimed_uncomplete = unclaimed[np.any(tasks[unclaimed] > 0)]
    unclaimed_uncomplete = [ta for ta in unclaimed if np.any(ta > 0)]
    unclaimed_uncomplete = np.array(unclaimed_uncomplete)
    print("unclaimed:", unclaimed_uncomplete)
    if len(unclaimed_uncomplete) == 0:
        return -1
    else:
        return unclaimed_uncomplete[random.randint(0, len(unclaimed_uncomplete) -1)]
        
        
        
        
    

            