#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 17:52:37 2021

@author: carolineskalla

Description: generate agent teams and show where they are on the DFD IFD plane. Prerequisite to basic simulation.
"""
import numpy as np

import matplotlib.pyplot as plt
import math
import generate_agents
import calc_fd

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
#tnorm = 10;
#numrepeats = 10;
#EmergencyStop = 5e2;
adivvals = np.logspace(-1, 3, 50)
gdivvals = np.logspace(-1, 3, 50)

#adivvals = np.larray(range(0.1, 1000, ))
#gdivvals = np.logspace(-1, 3, 10)


#Generate agents
DFD = np.zeros((50,50))
IFD = np.zeros((50,50))

ai = 0
for adiv in adivvals:
    gi = 0   
    for gdiv in gdivvals:
        agents = generate_agents.gen_agents(numfuncs, numagents, [adiv, agspread], (np.exp(-(np.array(range(0, numfuncs))**2/gdiv)))/sum(np.exp(-(np.array(range(0, numfuncs))**2/gdiv))), anorm)
        #Calculate and store diversity values
        [DFD[ai, gi], IFD[ai, gi]] = calc_fd.calc_fd(agents)
        gi+=1
    ai+=1
    
#try flatten 
flatDFD = DFD.flatten()
flatIFD = IFD.flatten()
#Plot agent diversity
#fig = plt.figure()
#ax = fig.add_subplot(projection='3d')
plt.scatter(flatIFD, flatDFD)
plt.xlabel('IFD')
plt.ylabel('DFD')
plt.title('DFD IFD Plane')
#ax.set_zlabel('Set to 0')