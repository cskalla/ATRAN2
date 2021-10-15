#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 10:09:50 2021

@author: carolineskalla
"""
import generate_agents
import numpy as np
import similarity

#generate agents

#Parameters:
numfuncs = 9
numagents = 10
#gDiv = np.repeat(1/nfunc, 9)
gDiv = [1/numfuncs for i in range(0,9)]
anorm = 10; #The sum of capabilities of agents,
aDiv = [100,10]#This is where intra-agent diversity can be set: the higher, the more diverse
tnorm = 10
numtasks=100
stop = 5000


#generate agents
agents = generate_agents.gen_agents(numfuncs, numagents, aDiv, (np.exp(-(np.array(range(0, numfuncs))**2/gDiv)))/sum(np.exp(-(np.array(range(0, numfuncs))**2/gDiv))), anorm)
#print("agent1", agents[0]) #print first agent
print(agents)

#generate similarity matrix
similarity.gen_dist_matrix(agents)