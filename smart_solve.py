#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 15:41:37 2021

@author: carolineskalla
"""

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

#import all code files
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
import assign_tasks2
import solve2
import calc_threshold
import solve3
import assign3

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

"""

#Parameters
adivvals = np.logspace(-1, 3, 50)
gdivvals = np.logspace(-1, 3, 30)
numfuncs = 9
numagents = 9
numtasks = 100
agspread = 10
anorm = 10
tnorm = 10
numrepeats = 20
stop = 500
max_agents_to_task = numagents/10
sim_threshold = 0.25 #similarity threshold - could be changed later??
#sim_threshold = 0 #full communication
#sim_threshold = float('inf')
def run_sim(adivvals, gdivvals, numfuncs, numagents, numtasks, agspread, anorm, tnorm, numrepeats, stop, sim_threshold, max_agents_to_task):
    
    

    DFD = np.zeros((50,30))
    IFD = np.zeros((50,30))
    minsn = np.zeros((50, 30))
    maxsn = np.zeros((50, 30))
    meansn = np.zeros((50, 30)) #time
    meannt = np.zeros((50, 30)) #num tasks solved
    
    
    #begin simulation
    ai = 0
    for adiv in adivvals:
        gi = 0   
        for gdiv in gdivvals:
            #generate agents
            agents = generate_agents.gen_agents(numfuncs, numagents, [adiv, agspread], (np.exp(-(np.array(range(0, numfuncs))**2/gdiv)))/sum(np.exp(-(np.array(range(0, numfuncs))**2/gdiv))), anorm)
            if 0 < sim_threshold <= 1:
                s_t = calc_threshold.calc_threshold(agents, sim_threshold)
            else:
                s_t = sim_threshold
            #Calculate and store diversity values
            [DFD[ai, gi], IFD[ai, gi]] = calc_fd.calc_fd(agents)
            nt = np.zeros(numrepeats)
            sn = np.zeros(numrepeats)
            for ridx in range(numrepeats):
                #create abandon timer
                #abandon_timer = np.zeros(len(agents))
                #Generate tasks
                tasks = generate_tasks.gen_tasks(numfuncs, numtasks, tnorm)
                #ASSIGN TASKS
                #index = assign3.init_assign_tasks(agents, tasks, s_t, max_agents_to_task, abandon_timer)
                #WORK ON TASKS
                sn[ridx], nt[ridx] = solve3.complete_tasks(agents, tasks, stop, s_t,max_agents_to_task)    
                #save results for trial
                minsn[ai, gi] = min(sn)
                maxsn[ai, gi] = max(sn)
                meansn[ai, gi] = np.mean(sn)
                meannt[ai, gi] = np.mean(nt)
        
            gi+=1
        ai+=1
    return IFD, DFD, meansn, meannt

x = run_sim(adivvals, gdivvals, numfuncs, numagents, numtasks, agspread, anorm, tnorm, numrepeats, stop, sim_threshold, max_agents_to_task)

def plotting(IFD, DFD, meansn, meannt):
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

    #Time veiw 1
    plt.xlabel('IFD',fontsize=10)
    plt.ylabel('DFD',fontsize=10)
    axes.set_zlabel('Time', fontsize=10)
    plt.title("No Information Sharing")
    plt.figtext(.5, 0.0, "threshold = "  + ", num tasks = " + str(numtasks) +  ", num agents = " + str(numagents) + ", Emergency stop = " + str(stop) + ", num repeats = " + str(numrepeats), ha="center", fontsize=10)
    plt.show()


    #Time veiw 2
    fig2 = plt.figure()
    axes = fig2.gca(projection ='3d')
    axes.plot_surface(DFD, IFD, meansn)
    
    plt.xlabel('DFD',fontsize=10)
    plt.ylabel('IFD',fontsize=10)
    axes.set_zlabel('Time', fontsize=10)
    plt.title("No Information Sharing")
    plt.figtext(.5, 0.0, "threshold = " + str(sim_threshold) + ", num tasks = " + str(numtasks) +  ", num agents = " + str(numagents) + ", Emergency stop = " + str(stop) + ", num repeats = " + str(numrepeats), ha="center", fontsize=10)
    plt.show()
    
    #Num tasks veiw 1
    fig2 = plt.figure()
    axes = fig2.gca(projection ='3d')
    axes.plot_surface(IFD, DFD, meannt)
    
    plt.xlabel('IFD',fontsize=10)
    plt.ylabel('DFD',fontsize=10)
    axes.set_zlabel('Number of tasks completed', fontsize=10)
    plt.title("No Information Sharing")
    plt.figtext(.5, 0.0, "threshold = " + str(sim_threshold) + ", num tasks = " + str(numtasks) +  ", num agents = " + str(numagents) + ", Emergency stop = " + str(stop) + ", num repeats = " + str(numrepeats), ha="center", fontsize=10)
    plt.show()
    
    #Num tasks veiw 2
    fig2 = plt.figure()
    axes = fig2.gca(projection ='3d')
    axes.plot_surface(DFD, IFD, meannt)
    
    plt.xlabel('DFD',fontsize=10)
    plt.ylabel('IFD',fontsize=10)
    axes.set_zlabel('Number of tasks completed', fontsize=10)
    plt.title("No Information Sharing")
    plt.figtext(.5, 0.0, "threshold = " + str(sim_threshold) + ", num tasks = " + str(numtasks) +  ", num agents = " + str(numagents) + ", Emergency stop = " + str(stop) + ", num repeats = " + str(numrepeats), ha="center", fontsize=10)
    plt.show()
    
    
    
   

  

plotting(x[0], x[1], x[2], x[3])   
