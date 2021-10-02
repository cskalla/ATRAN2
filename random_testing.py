#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 13:04:32 2021

@author: carolineskalla
"""
"""
import random
import numpy as np
import math
#Parameters:
#Number of functions
numfuncs = 9;
#Number of agents
numagents = 100;
#Number of tasks
numtasks = 10;
#Diversity jitter
agspread = 10;
#Agent total skill strength
anorm = 10;
gdivvals = np.logspace(-1, 3, 10)

for gdiv in gdivvals:
    
#gdiv = gdivvals[0] #testing
#exp((-(0:par.numfuncs-1).^2)/gdiv)
    x = (np.exp(-(np.array(range(0, numfuncs))**2/gdiv)))/sum(np.exp(-(np.array(range(0, numfuncs))**2/gdiv)))
    #print("x:", x)
    #print("x sum: ", sum(x))
    y=x/sum(x)
    #print("y:",y)
    #print("y sum: ", sum(y))
    
    #domf = np.random.choice(9, numagents, replace=True, p=x)
    #print(domf)
    

#agents and tasks    
agents = np.array([[1,1,1],[1,1,1]])
tasks = np.array([[3,3,3], [3,3,3]])
#agents are randomly assigned to tasks (agents can get the same task right now)
index = [random.randint(0,len(tasks[0])-1) for i in range(len(agents))]
time = 0
#check to see if all tasks are complete
while np.any([np.any(task > 0) for task in tasks]) or time == 10:
    i = 0
    for a in agents:
        tasks[index[i]]= tasks[index[i]]- agents[i]
        i+=1
    time += 1
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
print("agent1", agents[0])
print("agent2", agents[1])
print(similarity.similar(agents[0], agents[1]))
#Calculate and store diversity values
#[DFD, IFD] = calc_fd.calc_fd(agents)


#Generate tasks
#tasks = generate_tasks.gen_tasks(numfuncs, numtasks, tnorm)
#Assign tasks to agents
#index = assign_tasks.init_assign_tasks_comm(agents, tasks)
#work on tasks
#score = simple_solve.solve_tasks_comm(agents, tasks, index, stop)    



"""
 #generate agents
agents = generate_agents.gen_agents(numfuncs, numagents, aDiv, (np.exp(-(np.array(range(0, numfuncs))**2/gDiv)))/sum(np.exp(-(np.array(range(0, numfuncs))**2/gDiv))), anorm)
#Calculate and store diversity values
[DFD,IFD] = calc_fd.calc_fd(agents)

tasks = generate_tasks.gen_tasks(numfuncs, numtasks, tnorm)
#Assign tasks to agents
index = assign_tasks.assign_tasks(agents, tasks)
#work on tasks
print("calling simple solve")
t = simple_solve.solve_tasks(agents, tasks, index, stop)  
"""
"""
agents =np.array([[1,1,1], [1,1,1], [1,1,1]])

teamSum = 0
for a in agents:
    agentSum = 0
    agentTotal = sum(a)
    for skill in a:
        percent = skill/agentTotal
        agentSum += (percent**2)
    teamSum += (1 - agentSum)
IFD = teamSum/len(agents)
"""