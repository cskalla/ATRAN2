#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 17:57:27 2021

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
import complete_tasks


#Parameters
#adivvals = np.logspace(-1, 3, 20)
#gdivvals = np.logspace(-1, 3, 10)


adivvals = 10**(np.linspace(0.1, 0.2, 40)*(np.linspace(-6, 7, 40)))
gdivvals = 10**(0.2*np.linspace(-3, 5, 20))


numfuncs = 9
numagents = 10
numtasks = 10
agspread = 10
anorm = 10
tnorm = 10
numrepeats = 10
stop = 500
#max_agents_to_task = numagents/10
#sim_threshold = 0.25 #similarity threshold - could be changed later??
#sim_threshold = 0 #full communication
#sim_threshold = float('inf')
def run_sim(adivvals, gdivvals, numfuncs, numagents, numtasks, agspread, anorm, tnorm, numrepeats, stop):
    
    

    DFD = np.zeros((40,20))
    IFD = np.zeros((40,20))
    minsn = np.zeros((40, 20))
    maxsn = np.zeros((40, 20))
    meansn = np.zeros((40, 20)) #time
    meannt = np.zeros((40, 20)) #num tasks solved
    meannp = np.zeros((40, 20)) #num passes
    
    
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
            npass = np.zeros(numrepeats)
            for ridx in range(numrepeats):
                #create abandon timer
                #abandon_timer = np.zeros(len(agents))
                #Generate tasks
                tasks = generate_tasks.gen_tasks(numfuncs, numtasks, tnorm)
                #ASSIGN TASKS
                #index = assign3.init_assign_tasks(agents, tasks, s_t, max_agents_to_task, abandon_timer)
                #WORK ON TASKS
                sn[ridx], nt[ridx], npass[ridx] = complete_tasks.solve(agents, tasks)    
                #save results for trial
                minsn[ai, gi] = min(sn)
                maxsn[ai, gi] = max(sn)
                meansn[ai, gi] = np.mean(sn)
                meannt[ai, gi] = np.mean(nt)
                meannp[ai, gi] = np.mean(npass)
                
        
            gi+=1
        ai+=1
    return IFD, DFD, meansn, meannt

x = run_sim(adivvals, gdivvals, numfuncs, numagents, numtasks, agspread, anorm, tnorm, numrepeats, stop)

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
    plt.title("Agents Pass to small circle")
    plt.figtext(.5, 0.0, "num tasks = " + str(numtasks) +  ", num agents = " + str(numagents) + ", Emergency stop = " + str(stop) + ", num repeats = " + str(numrepeats), ha="center", fontsize=10)
    plt.show()


    
    #Num tasks veiw 1
    fig2 = plt.figure()
    axes = fig2.gca(projection ='3d')
    axes.plot_surface(IFD, DFD, meannt)
    
    plt.xlabel('IFD',fontsize=10)
    plt.ylabel('DFD',fontsize=10)
    axes.set_zlabel('Number of tasks completed', fontsize=10)
    plt.title("Agents Pass to small circle")
    plt.figtext(.5, 0.0,  + ", num tasks = " + str(numtasks) +  ", num agents = " + str(numagents) + ", Emergency stop = " + str(stop) + ", num repeats = " + str(numrepeats), ha="center", fontsize=10)
    plt.show()
    
   
    
    
   

  

plotting(x[0], x[1], x[2], x[3])   
