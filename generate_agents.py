#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 12:45:18 2021

@author: carolineskalla
"""
import numpy as np
import numpy.matlib
import random
import matplotlib.pyplot as plt


def gen_agents(nfunc, nagent, aDiv, gDiv, anorm):
    """
    #Parameters:
    nfunc = 9
    nagent = 100
    #gDiv = np.repeat(1/nfunc, 9)
    gDiv = [1/nfunc for i in range(0,9)]
    anorm = 10; #The sum of capabilities of agents,
    aDivm = 100; #This is where intra-agent diversity can be set: the higher, the more diverse
    aDivd = 10; #This introduces some spread into inta-agent diversity (so that IDA is not the same for all agents)
    """
    
    #Generate Agents
    #print("\n")
    #choosing a dominant function for each agent
    x = np.matlib.repmat(range(0, nfunc), nagent, 1)
    #choosing a dominant function for each agent
    #print(gDiv)
    #print(sum(gDiv))
    domf = np.random.choice(np.arange(nfunc), nagent, replace=True, p=gDiv)
    #print(domf)
    #initialize agents - adding jitter
    agents = np.exp((-(x)**2)/aDiv[0]+(aDiv[0]*aDiv[1]/100*random.randint(0,nagent)-aDiv[1]/200))
    #normalize to anorm value
    agents = (np.divide(agents.T,np.sum(agents, axis=1)).T)*anorm
    
    #mix up functions so different skills have different strengths
    for aidx in range(nagent):
        #for each row in agent matrix mix up the order of the row elements
        agents[aidx, :] = agents[aidx, np.random.permutation(len(agents[aidx,:]))]
        #put the dom function in the correct position
        swp = agents[aidx,domf[aidx]]; #old value
       # print(swp)
        m = max(agents[aidx,:])
        #print(m)
        l = np.where(agents[aidx,:] == np.amax(agents[aidx,:])) 
        #print(l[0][0])
        agents[aidx,domf[aidx]] = m
        agents[aidx, l[0][0]] = swp
        
        
    return agents

#a = gen_agents()
    
"""
%% Plot agents for checking
if par.debug
    numagents = size(agents, 1);
    DF = NaN(numagents,1);
    colors = jet(numagents);
    figure
    hold on
    for aidx = 1:numagents
        plot(agents(aidx, :), '*', 'Color', colors(aidx,:));
        DF(aidx) = find(agents(aidx,:) == max(agents(aidx, :))); %This finds the dominant function
        %     fprintf('%i\n', DF(aidx))
    end
    tabulate(DF)
    clear colors aidx DF
end
"""
"""
Not finished:
debug = True
if debug:
    numagents = len(agents[0])
    an_array = np.empty((nagent,0))
    an_array[:] = np.NaN
   
    for i in range(1, nagent) :
        x=np.full((1,nagent), i, dtype=int)
        plt.scatter(x, agents[i, :])
       
        #domf[aidx]
"""      