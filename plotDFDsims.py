#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 13:14:27 2021

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

#IFD will be held constant
adiv = 20
#adivvals = 10**(np.linspace(0.1, 0.2, 40)*(np.linspace(-6, 7, 40)))
gdivvals = 10**(0.2*np.linspace(-3, 5, 20))


numfuncs = 9
numagents = 10
numtasks = 100
agspread = 10
anorm = 10
tnorm = 10
numrepeats = 5
stop = 500
close_agents_size = 2
#max_agents_to_task = numagents/10
#sim_threshold = 0.25 #similarity threshold - could be changed later??
#sim_threshold = 0 #full communication
#sim_threshold = float('inf')
def run_sim(adiv, gdivvals, numfuncs, numagents, numtasks, agspread, anorm, tnorm, numrepeats, stop, close_agents_size):
    
    

    DFD = np.zeros((20))
    IFD = 0
    minsn = np.zeros((20))
    maxsn = np.zeros((20))
    meansn = np.zeros((20)) #time
    sn_error = np.zeros((20))
    meannt = np.zeros((20)) #num tasks solved
    nt_error = np.zeros((20))
    meannp = np.zeros((20)) #num passes
    
    
    #begin simulation
    gi = 0   
    for gdiv in gdivvals:
        #generate agents
        agents = generate_agents.gen_agents(numfuncs, numagents, [adiv, agspread], (np.exp(-(np.array(range(0, numfuncs))**2/gdiv)))/sum(np.exp(-(np.array(range(0, numfuncs))**2/gdiv))), anorm)
        
        #Calculate and store diversity values
        [DFD[gi], IFD] = calc_fd.calc_fd(agents)
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
            sn[ridx], nt[ridx], npass[ridx] = complete_tasks.solve(agents, tasks, close_agents_size)    
            #save results for trial
        minsn[gi] = np.min(sn)
        maxsn[gi] = np.max(sn)
        meansn[gi] = np.mean(sn) #mean time
        #find error for time
        #time_diff = sn - meansn[gi]
        #time_sqq = time_diff**2
        sn_error[gi] = np.std(sn)
        
        meannt[gi] = np.mean(nt) #mean num tasks
        #find error for num tasks
        #tasks_diff = nt - meannt[gi]
        #tasks_sqq = tasks_diff**2
        nt_error[gi] = np.std(nt)
        
        meannp[gi] = np.mean(npass) #mean num passes
            
    
        gi+=1
    return IFD, DFD, meansn, meannt, sn_error, nt_error

x = run_sim(adiv, gdivvals, numfuncs, numagents, numtasks, agspread, anorm, tnorm, numrepeats, stop, close_agents_size)

def plotting(IFD, DFD, meansn, meannt, sn_error, nt_error, numtasks, numagents, stop, numrepeats, close_agents_size):
    
    #dfd is x axes and y is time taken
    #plt.plot(DFD, meansn, linestyle='--', marker='o', color='b', label='line with marker')
    plt.scatter(DFD, meansn)
    plt.errorbar(DFD, meansn, yerr=sn_error, color='red', marker='o', capsize=5, capthick=1, ecolor='black')
    #plt.errorbar(DFD, meansn, yerr=sn_error)
    #Time veiw 1
    plt.xlabel('DFD',fontsize=10)
    plt.ylabel('Time taken to complete all tasks',fontsize=10)
    
    plt.title("Agents pass to small circle")
    plt.figtext(.5, 0.0, "IFD = " + str(IFD) + ", num tasks = " + str(numtasks) +  ", num agents = " + str(numagents) + ", small circle size = " + str(close_agents_size) + ", Max time = " + str(stop) + ", num repeats = " + str(numrepeats), ha="center", fontsize=10)
    plt.show()
    
  
    
    #dfd is x axes and y is time taken
    #plt.plot(DFD, meansn, linestyle='--', marker='o', color='b', label='line with marker')
    plt.scatter(DFD, meannt)
    plt.errorbar(DFD, meannt, yerr=nt_error, color='red', marker='o', capsize=5, capthick=1, ecolor='black')
    #plt.errorbar(DFD, meannt, yerr=nt_error)
    #Time veiw 1
    plt.xlabel('DFD',fontsize=10)
    plt.ylabel('Number of tasks completed',fontsize=10)
    
    plt.title("Agents pass to small circle")
    plt.figtext(.5, 0.0, "IFD = " + str(IFD) + ", num tasks = " + str(numtasks) +  ", num agents = " + str(numagents) + ", small circle size = " + str(close_agents_size) + ", Max time = " + str(stop) + ", num repeats = " + str(numrepeats), ha="center", fontsize=10)
    plt.show()
    
    
    
    
    
    
   


  
    
    
   

  

plotting(x[0], x[1], x[2], x[3], x[4], x[5], numtasks, numagents, stop, numrepeats, close_agents_size)  