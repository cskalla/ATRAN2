#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 10:50:57 2021

@author: carolineskalla
"""

import numpy as np
import passing
import random
import calc_threshold
    
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

def euc_dist_array(list1, list2, t):
        task = list2[t]
        sum_sq = np.sum(np.square(list1 - task))
        return np.sqrt(sum_sq)
        
def gen_euc_dist_matrix(agents):
   
    a, b= np.meshgrid(agents,agents)
    c = np.sum((a - b)**2)
    
    
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
    #matrix[matrix == 0] = float('inf')
    return(matrix)

    #array version
    #d1 = np.arange(len(agents))

#determines the close agents once at the beginning of the simulation
def close_agents(agents, close_agent_size, dist_matrix):
   # dist_matrix = gen_dist_matrix(agents)
    close_agent_matrix = np.zeros((len(agents),close_agent_size))
    #sort the distance matrix
    for a_ind in range(len(agents)):
        close_agents = np.argsort(dist_matrix[a_ind])
        #find three agent candidates
        
        #add some probabilty to close agents
        choices = np.arange(len(agents))
        p=passing.pass_prob(len(choices))
        close_ind = np.random.choice(choices, replace=False, p=p)
        agent_circle = close_agents[close_ind]
        
        #agent_circle = close_agents[0:close_agent_size]
        close_agent_matrix[a_ind] = agent_circle
    return close_agent_matrix

def display_small_circles(agents, relative_threshold):
    threshold = calc_threshold.calc_threshold(agents, relative_threshold)
    #threshold = relative_threshold
    len_circle = np.zeros((len(agents)))
    print("threshold:", threshold)
    #get distance matrix
    matrix = gen_dist_matrix(agents)
    print(matrix)
    for i in range(len(matrix)):
        print("Agent:", i)
        close_friends = matrix[i]
        print(close_friends)
        close_friends = close_friends[close_friends < threshold]
        print("Close friends:", len(close_friends))
        len_circle[i] = len(close_friends)
    return np.mean(len_circle)

def return_small_circles(i, agents, relative_threshold, dist_matrix):
    
    #threshold = calc_threshold.calc_threshold(agents, relative_threshold)
    #threshold = relative_threshold
    #len_circle = np.zeros((len(agents)))
    #print("threshold:", threshold)
  
  
    close_friends = dist_matrix[i]
    #print(close_friends)
    options = np.arange(len(close_friends))
    close_friends = options[close_friends < relative_threshold]
    #print("Close friends:", len(close_friends))
    #len_circle[i] = len(close_friends)
    #return np.mean(len_circle)
    return close_friends
    
   
#generate close agent matrix using a threshold (no fixed size, based on similarity)
def close_agents_from_threshold(i,agents, relative_threshold):  
    threshold = calc_threshold.calc_threshold(agents, relative_threshold)
    #threshold = relative_threshold
    dist_matrix = gen_dist_matrix(agents)
    close_agents = np.argsort(dist_matrix[i])
    #close_agent_matrix.fill(float('inf'))
    indices = np.arange((len(close_agents)))
    close_agents = indices[close_agents[indices] < threshold]
    return close_agents
    
    
    

    
    
    
    