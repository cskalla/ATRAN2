#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 10:47:09 2021

@author: carolineskalla
"""

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
numagents = 100;
#Number of tasks
numtasks = 10
#Diversity jitter
agspread = 10;
#Agent total skill strength
anorm = 10;
tnorm = 10;
#close_agents_size = 3
relative_threshold = 0.9

#numrepeats = 10;
#EmergencyStop = 5e2;
adivvals = 10**(np.linspace(0.1, 0.2, 20)*(np.linspace(-2, 7, 20)))
gdivvals = 10**(0.2*np.linspace(-3, 5, 10))
print(adivvals)
print("\n")
print(gdivvals)
stop = 2000


#choose aDiv and gDiv from above options
adiv = adivvals[5]
gdiv = gdivvals[8]


DFD = 0
IFD = 0


#gen agents
agents = generate_agents.gen_agents(numfuncs, numagents, [adiv, agspread], (np.exp(-(np.array(range(0, numfuncs))**2/gdiv)))/sum(np.exp(-(np.array(range(0, numfuncs))**2/gdiv))), anorm)
#Calculate and store diversity values
[DFD, IFD] = calc_fd.calc_fd(agents)
#generate tasks
tasks = generate_tasks.gen_tasks(numfuncs, numtasks, tnorm)

time, num_t = complete_tasks.solve(agents, tasks, relative_threshold)



"""
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
"""   