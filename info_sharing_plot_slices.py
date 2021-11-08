#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 13:15:43 2021

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
import matplotlib.patches as mpatches

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
num_friends = np.zeros((20))
#adiv = adivvals[0]
#ifd = 0.28
gdiv = gdivvals[6]
DFD = np.zeros((20))
IFD = np.zeros((20))

ai = 0

for adiv in adivvals:

    #gen agents
    agents = generate_agents.gen_agents(numfuncs, numagents, [adiv, agspread], (np.exp(-(np.array(range(0, numfuncs))**2/gdiv)))/sum(np.exp(-(np.array(range(0, numfuncs))**2/gdiv))), anorm)
    #Calculate and store diversity values
    [DFD[ai], IFD[ai]] = calc_fd.calc_fd(agents)
    #generate tasks
    #tasks = generate_tasks.gen_tasks(numfuncs, numtasks, tnorm)

    #complete_tasks.solve(agents, tasks, close_agents_size)
    relative_threshold = IFD[ai]
    #relative_threshold = 0.3

    num_friends[ai] = similarity.display_small_circles(agents, relative_threshold)
    ai+=1

avg_dfd = np.mean(DFD) 
m, b = np.polyfit(IFD, num_friends,1)   
fig = plt.figure()
plt.clf()
plt.scatter(IFD, num_friends, c=num_friends, cmap='summer')
plt.plot(IFD, m*IFD + b, color='black')
plt.xlabel('IFD',fontsize=10)
plt.ylabel('Average number of agents',fontsize=10)
plt.title("Average number of agents willing to share information with across team", size=8)
plt.figtext(.5, -0.05,  "Parameters:  Total number of agents =  " + str(numagents) + ", Fixed similarity threshold = " + str(relative_threshold) + ", Average DFD = " + str(avg_dfd), ha="center", fontsize=10)
#fig.colorbar(fig, ax=ax)
plt.colorbar(label="Average number of agents", orientation="vertical", pad = 0.15)
#add rectangle
left, bottom, width, height = (0.2, 3,0.4,5)
rect=mpatches.Rectangle((left,bottom),width,height, 
                        fill=False,
                        color="black",
                       linewidth=1)
                       #facecolor="red")
plt.gca().add_patch(rect)
plt.show()
    
    
