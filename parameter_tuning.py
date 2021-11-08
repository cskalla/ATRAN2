#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 13:50:52 2021

@author: carolineskalla
"""

#determine the approprate adiv and gdiv values for the IFD and DFD ranges provided in Bunderson and Sutcliffe
#imports
import numpy as np
import matplotlib.pyplot as plt
import math
import generate_agents
import generate_tasks
import calc_fd
import complete_tasks
import similarity
from matplotlib import cm

#Parameters:
#Number of functions
numfuncs = 9;
#Number of agents
numagents = 10;
#Number of tasks
numtasks = 100;
#Diversity jitter
agspread = 10;
#Agent total skill strength
anorm = 10;
tnorm = 10;
close_agents_size = 3
#numrepeats = 10;
#EmergencyStop = 5e2;
adivvals = 10**(np.linspace(0.1, 0.2, 20)*(np.linspace(-2, 7, 20)))
gdivvals = 10**(0.2*np.linspace(-1, 6, 20))

adiv = adivvals[2]
num_friends = np.zeros((20))
IFD = np.zeros((20))
DFD = np.zeros((20))
gi = 0

for gdiv in gdivvals:

        #gen agents
    agents = generate_agents.gen_agents(numfuncs, numagents, [adiv, agspread], (np.exp(-(np.array(range(0, numfuncs))**2/gdiv)))/sum(np.exp(-(np.array(range(0, numfuncs))**2/gdiv))), anorm)
#Calculate and store diversity values
    [DFD[gi], IFD[gi]] = calc_fd.calc_fd(agents)
#generate tasks
#tasks = generate_tasks.gen_tasks(numfuncs, numtasks, tnorm)

#complete_tasks.solve(agents, tasks, close_agents_size)
        #relative_threshold = IFD[ai, gi]

        #num_friends[ai][gi] = similarity.display_small_circles(agents, relative_threshold)
   
    gi+=1
plt.clf()
plt.plot(adivvals, DFD)
plt.show()
    
