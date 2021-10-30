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
#adivvals = np.logspace(-1, 3, 50)
#gdivvals = np.logspace(-1, 3, 50)

"""
exp_array = np.linspace(0.1, 0.2, 20)*np.linspace(-6, 7, 20)
base_array = np.zeros(20)
base_array.fill(10)
adivvals = np.power(base_array, exp_array)
"""
adivvals = 10**(np.linspace(0.1, 0.2, 20)*np.linspace(-6, 7, 20))
gdivvals = 10**(0.2*np.linspace(-3, 5, 10))
"""
exp_array2 = 0.2*np.logspace(-3, 5, 10)
base_array2 = np.zeros(10)
base_array2.fill(10)
gdivvals = np.power(base_array2, exp_array2)
"""
#adivvals = np.larray(range(0.1, 1000, ))
#gdivvals = np.logspace(-1, 3, 10)


#Generate agents
DFD = np.zeros((20,10))
IFD = np.zeros((20,10))

ai = 0
for adiv in adivvals:
    gi = 0   
    for gdiv in gdivvals:
        agents = generate_agents.gen_agents(numfuncs, numagents, [adiv, agspread], (np.exp(-(np.arange(numfuncs)**2)/gdiv))/np.sum(np.exp(-(np.arange(numfuncs)**2/gdiv))), anorm)
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