#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 14:32:28 2021

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
from scipy.interpolate import griddata
from mpl_toolkits import mplot3d
from matplotlib import cm

#Parameters
numfuncs = 9
numagents = 10
numtasks = 100
agspread = 10
anorm = 10
tnorm = 10
numrepeats = 5
stop = 5e2
gdiv = gDiv = [1/numfuncs for i in range(0,9)]
adivvals = np.logspace(-1, 3, 20)

IFD = np.zeros(20)
DFD = np.zeros(20)
minsn = np.zeros((20))
maxsn = np.zeros((20))
meansn = np.zeros((20))

#begin simulation
ai = 0
for adiv in adivvals:   
    #generate agents
    agents = generate_agents.gen_agents(numfuncs, numagents, [adiv, agspread], (np.exp(-(np.array(range(0, numfuncs))**2/gdiv)))/sum(np.exp(-(np.array(range(0, numfuncs))**2/gdiv))), anorm)
    #Calculate and store diversity values
    DFD[ai], IFD[ai] = calc_fd.calc_fd(agents)
    
    sn = np.zeros(numrepeats)
    for ridx in range(numrepeats):
        #Generate tasks
        tasks = generate_tasks.gen_tasks(numfuncs, numtasks, tnorm)
        #Assign tasks to agents
        index = assign_tasks.assign_tasks(agents, tasks)
        #work on tasks
        sn[ridx] = simple_solve.solve_tasks(agents, tasks, index, stop)    
    #save results for trial
    minsn[ai] = min(sn)
    maxsn[ai] = max(sn)
    meansn[ai] = np.mean(sn)
    
      
    ai+=1
    
plt.scatter(IFD, meansn)
plt.xlabel('IFD',fontsize=10)
plt.ylabel('Time',fontsize=10)
plt.title("IFD vs Time")
plt.figtext(.5, 0.0, "DFD = " + str(np.mean(DFD)) + "stop = " + str(stop) + ", num tasks = " + str(numtasks) +  ", num agents = " + str(numagents) + ", num repeats = " + str(numrepeats), ha="center", fontsize=10)
plt.show()
