#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 10:50:57 2021

@author: carolineskalla
"""

import numpy as np
    
def euc_dist(list1, list2, a1, a2):
    #get agents 
    agent1 = list1[a1]
    agent2 = list2[a2]
    # finding sum of squares
    sum_sq = np.sum(np.square(agent1 - agent2))
 
    # Doing squareroot and
    # printing Euclidean distance
    #print(np.sqrt(sum_sq))
    return np.sqrt(sum_sq)
    
def gen_dist_matrix(agents):
    matrix = np.zeros((len(agents), (len(agents))))
    
    for i in range(len(agents)):
        for j in range(i, len(agents)):
            if(i == j):
                matrix[i][j] = 0
            else:
                d = euc_dist(agents, agents, i, j)
                matrix[i][j] = d
                matrix[j][i] = d
    return(matrix)

#determines the close agents once at the beginning of the simulation
def close_agents(agents, close_agent_size):
    dist_matrix = gen_dist_matrix(agents)
    close_agent_matrix = np.array((len(agents), close_agent_size))
    #sort the distance matrix
    for a_ind in range(len(agents)):
        close_agents = np.argsort(dist_matrix[a_ind])
        #find three agent candidates
        agent_circle = close_agents[0:3]
        close_agent_matrix[a_ind].append(agent_circle)
    return close_agent_matrix
        
    
    

    
    
    
    