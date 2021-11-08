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
import calc_threshold

#find agents for stuck agents to pass to
def pass_new_agent(tasks, agents, a_ind, stuck_tasks, threshold, dist_matrix):
    #for each stuck task:
    for task in stuck_tasks:
        #identify current agent
        a_i = a_ind[task]
        #identify agents that the current agent is willing to talk to
        close_friends = similarity.return_small_circles(a_i, agents, threshold, dist_matrix)
        print("close_friends", close_friends)
        #identify which of these agents are not busy
        free_friends = close_friends[np.invert(np.isin(close_friends, a_ind))]
        print("free friends", free_friends)
        if len(free_friends) == 0:
            continue
        #choose the one that is closest to the task
        distances = similarity.euc_dist_array(agents[free_friends], tasks, task)
        a_ind[task] = free_friends[np.argmin(distances)]
        
    #return new a_ind
    return a_ind
    

def pick_close_agent(a_ind, close_agent_matrix, close_agents_size, tasks, task_ind):
        #print("current agent: agent #", a_ind)

        #sort the distance matrix
        #close_agents = np.argsort(dist_matrix[a_ind])
        
        #find three agent candidates
        #agent_circle = close_agents[0:3]
        #print("agent circle is:", agent_circle)
        #pick a random agent from the small cirle to pass the task to
        
        #Passes to most dissimilar agent
        agent_circle = close_agent_matrix[a_ind]
        #print(close_agent_matrix)
        #print(agent_circle)
        """
        p = pass_prob(close_agents_size)
        a_ind = np.random.choice(agent_circle, replace=True, p=p)
        """
        a_ind = agent_task_dist(agent_circle, tasks, task_ind)
        #pass to most qualified agent
        
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
    unclaimed = task_options[np.invert(np.isin(task_options, a_ind))]
    #task_candidates[np.all(a_ind != task_candidates)]
    #a_ind2 = copy.deepcopy(a_ind) + np.zeros((range(len(a_ind), len(tasks))))
    #np.argsort(a_ind2)
    
   # unclaimed =  task candidates
    unclaimed_uncomplete = unclaimed[np.any(tasks[unclaimed] > 0, axis = 1)]
    #unclaimed_uncomplete = [ta for ta in unclaimed if np.any(ta > 0)]
    #unclaimed_uncomplete = np.array(unclaimed_uncomplete)
    #print("unclaimed:", unclaimed_uncomplete)
    if len(unclaimed_uncomplete) == 0:
        #print("1")
        return -1
    else:
        task = unclaimed_uncomplete[random.randint(0, len(unclaimed_uncomplete) -1)]
        print(task)
        #return unclaimed_uncomplete[random.randint(0, len(unclaimed_uncomplete) -1)]
        return task
        
def pass_prob(close_agents_size):  
    
    x = np.exp(-(np.arange(close_agents_size)**2)/3)
    y = x/np.sum(x)
    return y[::-1]   

#returns the indice of the most qaulified agent
def agent_task_dist(agent_circle, tasks, task_ind):
    #make array of distances between task and agents in close circle
    agent_order = similarity.euc_dist_array(agent_circle, tasks, task_ind)
    a_ind = np.argmin(agent_order)
    return a_ind
    
    
