#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 20:34:04 2021

@author: carolineskalla
"""
#Testing: passing illustration - agents in a network are connected to each other. Any two agents are connected if the euclidean distance 
#between their skill vectors is below a threshold t. In this simulation we will see  if the task reaches the best suited agent
#(the one with the smallest distance), if it reaches a more suited agent, or if it gets stuck with a sub par agent.
#We hope to see how the threshold affects the task pairing, how the diversity of the team might influence the threshold
#and thus the pairing quality, and how cases of particular team composition might affect the results.

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
import pandas as pd

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
#print(adivvals)
#print("\n")
#print(gdivvals)
stop = 2000


#choose aDiv and gDiv from above options
adiv = adivvals[5]
gdiv = gdivvals[8]

#generate agents
agents = generate_agents.gen_agents(numfuncs, numagents, [adiv, agspread], (np.exp(-(np.array(range(0, numfuncs))**2/gdiv)))/sum(np.exp(-(np.array(range(0, numfuncs))**2/gdiv))), anorm)
#calculate a similarity matrix
sim_matrix = similarity.gen_dist_matrix(agents)
print(sim_matrix)
table = pd.DataFrame(sim_matrix)
print(table)
#calculate initial connections
close_agent_size = 5
connections_matrix = pd.DataFrame(similarity.close_agents(agents, close_agent_size, sim_matrix))
print(connections_matrix)
#generate one task

#task starts at random location of agent network

#agent scans its connection and look to see if there is an agent better suited to the task, if there is the task gets passed

