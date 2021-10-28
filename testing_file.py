#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 16:56:38 2021

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

#Parameters:
#Number of functions
numfuncs = 9;
#Number of agents
numagents = 10;
#Number of tasks
numtasks = 10;
#Diversity jitter
agspread = 10;
#Agent total skill strength
anorm = 10;
tnorm = 10;
#numrepeats = 10;
#EmergencyStop = 5e2;
adivvals = np.logspace(-1, 3, 20)
gdivvals = np.logspace(-1, 3, 10)
print(adivvals)
print("\n")
print(gdivvals)
stop = 500

#choose aDiv and gDiv from above options
adiv = 100 #high IFD
gdiv = 1
#46

#Generate agents
#DFD = np.zeros((20,10))
#IFD = np.zeros((20,10))


agents = generate_agents.gen_agents(numfuncs, numagents, [adiv, agspread], (np.exp(-(np.array(range(0, numfuncs))**2/gdiv)))/sum(np.exp(-(np.array(range(0, numfuncs))**2/gdiv))), anorm)
        #Calculate and store diversity values
        #[DFD[ai, gi], IFD[ai, gi]] = calc_fd.calc_fd(agents)
#print("agents \n")
#print(agents)  
dfd, ifd = calc_fd.calc_fd(agents)  
#print("DFD:", dfd) 
#print("IFD:", ifd) 

#generate tasks
tasks = generate_tasks.gen_tasks(numfuncs, numtasks, tnorm)

#######
#Plotting Network
# libraries
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
 
# I build a data set: 10 individuals and 5 variables for each
#ind1=[5,10,3,4,8,10,12,1,9,4]
#ind5=[1,1,13,4,18,5,2,11,3,8]
"""
#num_agents
n= 10
"""
#find pairs of agents
a1 = []
a2 = []
for i in range(len(agents)):
    for j in range(len(agents)):
        a1.append(i)
        a2.append(j)
        
print(a1)
print(a2)

#a1 = np.arange(len(agents))
#a2 = np.arange(len(agents))
print(len(a1))
print(len(a2))
    
def euc_dist(agents, a1, a2):
    #get agents 
    agent1 = agents[a1]
    agent2 = agents[a2]
    # finding sum of squares
    sum_sq = np.sum(np.square(agent1 - agent2))
 
    # Doing squareroot and
    # printing Euclidean distance
    #print(np.sqrt(sum_sq))
    return np.sqrt(sum_sq)

#find euclidean distances between agents
def gen_dist_matrix(agents):
    matrix = np.zeros((len(agents), (len(agents))))
    
    for i in range(len(agents)):
        for j in range(i, len(agents)):
            if(i == j):
                matrix[i][j] = 0
            else:
                d = euc_dist(agents, agents, i, j)
                matrix[i][j] = d
                matrix[j][i] = d
    return(matrix)
    
dist_matrix = gen_dist_matrix(agents)

print(len(dist_matrix.flatten()))
#df = pd.DataFrame({ 'A':a1, 'B':a2 + np.random.randint(10, size=(10)) , 'C':ind1 + np.random.randint(10, size=(10)) , 'D':ind1 + np.random.randint(5, size=(10)) , 'E':ind1 + np.random.randint(5, size=(10)), 'F':ind5, 'G':ind5 + np.random.randint(5, size=(10)) , 'H':ind5 + np.random.randint(5, size=(10)), 'I':ind5 + np.random.randint(5, size=(10)), 'J':ind5 + np.random.randint(5, size=(10))})
 
# Calculate the correlation between individuals. We have to transpose first, because the corr function calculate the pairwise correlations between columns.
#corr = df.corr()
df = pd.DataFrame({'A1':a1, 'A2':a2, 'dist':dist_matrix.flatten()})
filtered_df = df[df.dist != 0]
print(filtered_df)
# Transform it in a links data frame (3 columns only):
#links = corr.stack().reset_index()
#links.columns = ['agent1', 'agent2', 'value']
#print(links)
# Keep only correlation over a threshold and remove self correlation (cor(A,A)=1)
#links_filtered=links.loc[ (links['value'] > 0.8) & (links['var1'] != links['var2']) ]
 
ax = plt.figure(figsize=(10,5))
# Build your graph
G=nx.from_pandas_edgelist(filtered_df, 'A1', 'A2')
 
# Plot the network:
nx.draw(G, with_labels=True, node_color='red', node_size=400, edge_color='black', linewidths=.1, font_size=8)
#ax.plt.gca()
plt.title('Euclidean distance between agents', size=20)