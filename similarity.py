#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 10:50:57 2021

@author: carolineskalla
"""

import numpy as np


def similar(agent1, agent2):
   # print("agent1", agent1)
    #print("agent2", agent2)
    #use the shorter length (smaller number of skills)
    length = min(len(agent1),len(agent2))
    #print("length", length)
    count = 0
    for i in range(length):
       # print(agent1[i])
        #print(agent2[i])
        if (agent1[i] > 0) and (agent2[i] > 0):
            count += 1
    return(count/length)
    
    
"""        
x = np.array([1,1,1])  
y = np.array([0.5,0,0])
similar(x,y)
"""

#tests whether two agents have the same DFD
def DFD_similar(agent1, agent2):
    #get agent1's dominant function
    a1_df_ind = np.argmax(agent1)
    #get agent2's dominat function
    a2_df_ind = np.argmax(agent2)
    #compare
    
    if (np.array_equal(a1_df_ind, a2_df_ind, equal_nan=False)):
        return True
    #return T or F
    else:
        return False
    
    
def euc_dist(agents, a1, a2):
    #get agents 
    agent1 = agents[a1]
    agent2 = agents[a2]
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
                d = euc_dist(agents, i, j)
                matrix[i][j] = d
                matrix[j][i] = d
    return(matrix)
    

    
    
    
    