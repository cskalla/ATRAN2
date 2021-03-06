#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:22:50 2021

@author: carolineskalla
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 15:58:38 2021

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
numagents = 9
numtasks = 100
agspread = 10
anorm = 10
tnorm = 10
numrepeats = 20
stop = 500

sim_threshold = 1

adivvals = np.logspace(-1, 3, 20)
gdivvals = np.logspace(-1, 3, 10)

DFD = np.zeros((20,10))
IFD = np.zeros((20,10))
minsn = np.zeros((20, 10))
maxsn = np.zeros((20, 10))
meansn = np.zeros((20, 10))
#finding the mean num tasks solved
meannt = np.zeros((20, 10))



#begin simulation
ai = 0
for adiv in adivvals:
    gi = 0   
    for gdiv in gdivvals:
        #generate agents
        agents = generate_agents.gen_agents(numfuncs, numagents, [adiv, agspread], (np.exp(-(np.array(range(0, numfuncs))**2/gdiv)))/sum(np.exp(-(np.array(range(0, numfuncs))**2/gdiv))), anorm)
        #Calculate and store diversity values
        [DFD[ai, gi], IFD[ai, gi]] = calc_fd.calc_fd(agents)
        nt = np.zeros(numrepeats)
        sn = np.zeros(numrepeats)
        for ridx in range(numrepeats):
            #Generate tasks
            tasks = generate_tasks.gen_tasks(numfuncs, numtasks, tnorm)
            #Assign tasks to agents
            index = assign_tasks.init_assign_tasks_nocomm(agents, tasks)
            #work on tasks
            sn[ridx], nt[ridx] = simple_solve.solve_tasks_sim_comm(agents, tasks, index, stop, sim_threshold)    
        #save results for trial
        minsn[ai, gi] = min(sn)
        maxsn[ai, gi] = max(sn)
        meansn[ai, gi] = np.mean(sn)
        meannt[ai, gi] = np.mean(nt)
        
        gi+=1
    ai+=1
"""
#plot results
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
#ax.scatter(IFD,DFD, meansn)
ax.surface_plot(IFD, DFD, meansn, cmap=cm.coolwarm,linewidth=0, antialiased=False)
ax.set_xlabel('IFD')
ax.set_ylabel('DFD')
ax.set_zlabel('Set to 0')
"""

#surface plot
# target grid to interpolate to
xi = np.arange(0,1.01,0.0001)
yi = np.arange(0,1.01,0.0001)
xi,yi = np.meshgrid(xi,yi)

# interpolate
zi = griddata((IFD.flatten(),DFD.flatten()),meansn.flatten(),(xi,yi),method='linear')
fig2 = plt.figure()
axes = fig2.gca(projection ='3d')
axes.plot_surface(IFD, DFD, meansn)

#plt.plot(x,y,'k.')
plt.xlabel('IFD',fontsize=10)
plt.ylabel('DFD',fontsize=10)
axes.set_zlabel('Time', fontsize=10)
plt.title("Functional Diversity - Euclidian distance similarity based communication")
plt.figtext(.5, 0.0, "stop = " + str(stop) + ", num tasks = " + str(numtasks) +  ", num agents = " + str(numagents) + ", Emergency stop = " + str(stop) + ", num repeats = " + str(numrepeats), ha="center", fontsize=10)
plt.show()


#surface plot
# target grid to interpolate to
xi = np.arange(0,1.01,0.0001)
yi = np.arange(0,1.01,0.0001)
xi,yi = np.meshgrid(xi,yi)

# interpolate
zi = griddata((DFD.flatten(),IFD.flatten()),meansn.flatten(),(xi,yi),method='linear')
fig2 = plt.figure()
axes = fig2.gca(projection ='3d')
axes.plot_surface(DFD, IFD, meansn)

#plt.plot(x,y,'k.')
plt.xlabel('DFD',fontsize=10)
plt.ylabel('IFD',fontsize=10)
axes.set_zlabel('Time', fontsize=10)
plt.title("Functional Diversity - Euclidian distance similarity based communication")
plt.figtext(.5, 0.0, "stop = " + str(stop) + ", num tasks = " + str(numtasks) +  ", num agents = " + str(numagents) + ", Emergency stop = " + str(stop) + ", num repeats = " + str(numrepeats), ha="center", fontsize=10)
plt.show()



#####
#second plot
######
#surface plot
# target grid to interpolate to
xi = np.arange(0,1.01,0.0001)
yi = np.arange(0,1.01,0.0001)
xi,yi = np.meshgrid(xi,yi)

# interpolate
zi = griddata((IFD.flatten(),DFD.flatten()),meannt.flatten(),(xi,yi),method='linear')
fig2 = plt.figure()
axes = fig2.gca(projection ='3d')
axes.plot_surface(IFD, DFD, meannt)

#plt.plot(x,y,'k.')
plt.xlabel('IFD',fontsize=10)
plt.ylabel('DFD',fontsize=10)
axes.set_zlabel('Number of tasks solved', fontsize=10)
plt.title("Functional Diversity - Euclidian distance similarity based communication")
plt.figtext(.5, 0.0, "stop = " + str(stop) + ", num tasks = " + str(numtasks) +  ", num agents = " + str(numagents) + ", Emergency stop = " + str(stop) + ", num repeats = " + str(numrepeats), ha="center", fontsize=10)
plt.show()

#####
#second plot
######
#surface plot
# target grid to interpolate to
xi = np.arange(0,1.01,0.0001)
yi = np.arange(0,1.01,0.0001)
xi,yi = np.meshgrid(xi,yi)

# interpolate
zi = griddata((DFD.flatten(),IFD.flatten()),meannt.flatten(),(xi,yi),method='linear')
fig2 = plt.figure()
axes = fig2.gca(projection ='3d')
axes.plot_surface(DFD, IFD, meannt)
#plt.plot(x,y,'k.')
plt.xlabel('DFD',fontsize=10)
plt.ylabel('IFD',fontsize=10)
axes.set_zlabel('Number of tasks solved', fontsize=10)
plt.title("Functional Diversity - Euclidian distance similarity based communication")
plt.figtext(.5, 0.0, "stop = " + str(stop) + ", num tasks = " + str(numtasks) +  ", num agents = " + str(numagents) + ", Emergency stop = " + str(stop) + ", num repeats = " + str(numrepeats), ha="center", fontsize=10)
plt.show()
