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
adivvals = 10**(np.linspace(0.1, 0.2, 20)*(np.linspace(-6, 7, 20)))
gdivvals = 10**(0.2*np.linspace(-3, 5, 10))
print(adivvals)
print("\n")
print(gdivvals)
stop = 500
#fixed_threshold = 1
#relative_threshold = 0.8

#choose aDiv and gDiv from above options
#adiv = 15 #high IFD
#gdiv = 2
#46

#avg number of friends among team of agents
num_friends = np.zeros((20,10))
IFD = np.zeros((20,10))
DFD = np.zeros((20,10))
ai = 0

for adiv in adivvals:
    gi = 0
    for gdiv in gdivvals:
        #gen agents
        agents = generate_agents.gen_agents(numfuncs, numagents, [adiv, agspread], (np.exp(-(np.array(range(0, numfuncs))**2/gdiv)))/sum(np.exp(-(np.array(range(0, numfuncs))**2/gdiv))), anorm)
#Calculate and store diversity values
        [DFD[ai, gi], IFD[ai, gi]] = calc_fd.calc_fd(agents)
#generate tasks
#tasks = generate_tasks.gen_tasks(numfuncs, numtasks, tnorm)

#complete_tasks.solve(agents, tasks, close_agents_size)
        relative_threshold = IFD[ai, gi]

        num_friends[ai][gi] = similarity.display_small_circles(agents, relative_threshold)
        gi+=1
    ai+=1
    
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
im = ax.scatter(IFD, DFD, num_friends, c=num_friends, cmap='summer')
#summer, viridis, magma
plt.title("Average number of agents willing to share information with across team", size=8)
ax.set_xlabel('IFD')
ax.set_ylabel('DFD')
ax.set_zlabel('Average number of agents')
plt.figtext(.5, -0.05,  "Parameters:  Total number of agents =  " + str(numagents) + ", Fixed similarity threshold = " + str(relative_threshold), ha="center", fontsize=10)
#fig.colorbar(fig, ax=ax)
plt.colorbar(im, ax=ax,label="Average number of agents", orientation="vertical", pad = 0.15)
#plt.show()
#plt.savefig('information_sharing6.png')
plt.show()
"""
# rotate the axes and update
for angle in range(0, 360):
    ax.view_init(30, angle)
    plt.draw()
    plt.pause(.001)
"""
