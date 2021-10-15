#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 15:00:23 2021

@author: carolineskalla
"""

import numpy as np
import numpy.matlib
import random
import math
import matplotlib.pyplot as plt
import generate_agents
import generate_tasks
import assign_tasks
import simple_solve
import calc_fd
import similarity
import assign_tasks2
import calc_threshold


#Parameters:
numfuncs = 9
numagents = 2
#gDiv = np.repeat(1/nfunc, 9)
#gDiv = [1/numfuncs for i in range(0,9)]
gDiv = [1, 0, 0, 0, 0, 0, 0, 0, 0]
anorm = 10; #The sum of capabilities of agents,
aDiv = [10,10]#This is where intra-agent diversity can be set: the higher, the more diverse
tnorm = 10
numtasks=10
stop = 5000
max_agents_to_task = numagents/10

threshold = float('inf') #full communicatiom
#threshold = sys.min #no communication
#threshold = 1 #calculate relative threshold

#print((np.exp(-(np.array(range(0, numfuncs))**2/gDiv)))/sum(np.exp(-(np.array(range(0, numfuncs))**2/gDiv))))


#generate agents
agents = generate_agents.gen_agents(numfuncs, numagents, aDiv, (np.exp(-(np.array(range(0, numfuncs))**2/gDiv)))/sum(np.exp(-(np.array(range(0, numfuncs))**2/gDiv))), anorm)
#create abandon timer
abandon_timer = np.zeros(len(agents))
#generate tasks
tasks = generate_tasks.gen_tasks(numfuncs, numtasks, tnorm)
#assign initial tasks
index = assign_tasks2.init_assign_tasks(agents, tasks, threshold, max_agents_to_task, abandon_timer)


matrix = similarity.gen_dist_matrix(agents)
print(matrix)

"""
option = assign_tasks2.new_task(3, agents, tasks, index, threshold, max_agents_to_task, abandon_timer)
print(option)
index[3] = option
print(assign_tasks2.agents_on_task(index, option))
option = assign_tasks2.new_task(4, agents, tasks, index, threshold, max_agents_to_task, abandon_timer)
print(option)
index[4] = option
print(assign_tasks2.agents_on_task(index, option))
option = assign_tasks2.new_task(5, agents, tasks, index, threshold, max_agents_to_task, abandon_timer)
print(option)
index[5] = option
print(assign_tasks2.agents_on_task(index, option))
"""
"""
for i in range(0, 20):
    option = assign_tasks2.new_task(i, agents, tasks, index, threshold, max_agents_to_task, abandon_timer)
    print(option)
    index[i] = option
    print(assign_tasks2.agents_on_task(index, option))
    print("unclaimed tasks:", assign_tasks2.check_unclaimed(agents, tasks, index))
"""    





