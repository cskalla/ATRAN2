#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 09:25:19 2022

@author: carolineskalla
"""

#plots the maximum distance between agents on a team across IFD DFD plane


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
import timeit
import similarity

#Parameters
#adivvals = np.logspace(-1, 3, 20)
#gdivvals = np.logspace(-1, 3, 10)


adivvals = 10**(np.linspace(0.1, 0.2, 20)*(np.linspace(-6, 7, 20)))
gdivvals = 10**(0.2*np.linspace(-3, 5, 10))


numfuncs = 9
numagents = 100
numtasks = 10
agspread = 10
anorm = 10
tnorm = 10
numrepeats = 100
stop = 500
#close_agent_size = 3
#max_agents_to_task = numagents/10
#sim_threshold = 0.25 #similarity threshold - could be changed later??
#sim_threshold = 0 #full communication
#sim_threshold = float('inf')
def run_sim(adivvals, gdivvals, numfuncs, numagents, numtasks, agspread, anorm, tnorm, numrepeats, stop):
    
    

    DFD = np.zeros((20,10))
    IFD = np.zeros((20,10))
    distances = np.zeros((20, 10))
  
    
    start = timeit.default_timer()
    #begin simulation
    ai = 0
    for adiv in adivvals:
        gi = 0   
        for gdiv in gdivvals:
            #generate agents
            agents = generate_agents.gen_agents(numfuncs, numagents, [adiv, agspread], (np.exp(-(np.array(range(0, numfuncs))**2/gdiv)))/sum(np.exp(-(np.array(range(0, numfuncs))**2/gdiv))), anorm)
            
            #Calculate and store diversity values
            [DFD[ai, gi], IFD[ai, gi]] = calc_fd.calc_fd(agents)
            #relative_threshold = IFD[ai, gi]
            matrix = similarity.gen_dist_matrix(agents)
            a_max = np.amax(matrix)
            distances[ai][gi] = a_max
            
              
               
                
        
            gi+=1
        ai+=1
        
        #print(stop-start)
    return IFD, DFD, distances
stop = timeit.default_timer()
x = run_sim(adivvals, gdivvals, numfuncs, numagents, numtasks, agspread, anorm, tnorm, numrepeats, stop)

def plotting(IFD, DFD, distances):
    #surface plot
    # target grid to interpolate to
    xi = np.arange(0,1.01,0.0001)
    yi = np.arange(0,1.01,0.0001)
    xi,yi = np.meshgrid(xi,yi)

    # interpolate
    zi = griddata((IFD.flatten(),DFD.flatten()),distances.flatten(),(xi,yi),method='linear')
  
    fig2 = plt.figure()
    axes = fig2.gca(projection ='3d')
    axes.plot_surface(IFD, DFD, distances, cmap='GnBu_r')

    #Time veiw 1
    plt.xlabel('IFD',fontsize=10)
    plt.ylabel('DFD',fontsize=10)
    axes.set_zlabel('Max distance between any two agents', fontsize=10)
    plt.title("Max distances between any two agents")
    plt.figtext(.5, 0.0, "num tasks = " + str(numtasks) +  ", num agents = " + str(numagents) + ", Emergency stop = " + str(stop) + ", num repeats = " + str(numrepeats), ha="center", fontsize=10)
    plt.show()


    
    
    
   
  
  

plotting(x[0], x[1], x[2])


 