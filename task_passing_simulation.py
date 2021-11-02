#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 14:29:07 2021

@author: carolineskalla
"""

#imports
import numpy as np
import matplotlib.pyplot as plt
import math
import generate_agents
import generate_tasks
import calc_fd
import complete_tasks

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
adivvals = np.logspace(-1, 3, 20)
gdivvals = np.logspace(-1, 3, 10)
print(adivvals)
print("\n")
print(gdivvals)
stop = 500

#choose aDiv and gDiv from above options
adiv = 15 #high IFD
gdiv = 20
#46

#gen agents
agents = generate_agents.gen_agents(numfuncs, numagents, [adiv, agspread], (np.exp(-(np.array(range(0, numfuncs))**2/gdiv)))/sum(np.exp(-(np.array(range(0, numfuncs))**2/gdiv))), anorm)
#Calculate and store diversity values
dfd, ifd = calc_fd.calc_fd(agents) 
#generate tasks
tasks = generate_tasks.gen_tasks(numfuncs, numtasks, tnorm)

complete_tasks.solve(agents, tasks, close_agents_size)

