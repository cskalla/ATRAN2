#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import generate_agents
"""
Created on Sat Sep  4 15:21:29 2021

@author: carolineskalla

function [DFD, IFD] = CalcFD(agents)

%% Calculate DFD
maxDFD = 1-1/size(agents, 2); %This is the maxmial value DFD can take.
[~, I] = max(agents, [], 2);
T = tabulate(I);
DFD = 1 - sum((T(:,3)/100).^2); %This is the first formula in the Bunderson & Sutcliffe, 2002 paper
DFD = DFD/maxDFD; %This is the normalization they mention on page 885 below the formula

%% Calculate IFD
% First calculate IFDS
IFDS = 1 - sum((agents./sum(agents,2)).^2, 2);
IFD = mean(IFDS);

end
"""
#generate agents for testing
#agents = generate_agents.gen_agents()


def calc_fd(agents):


    #TESTING AS NOT FUNCTION
     #Calculate DFD
    maxDFD = 1 - (1/len(agents)) #This is the maxmial value DFD can take.
    #Find maximum function of agents
    # [~, I] = max(agents, [], 2)
    I = [0]*len(agents)
    for a in range(len(agents)):
        m = max(agents[a,:])
        I[a] = np.where(agents[a,:] == np.amax(agents[a,:]))      
    #T = tabulate(I);
    T = np.array(np.unique(I, return_counts=True)).T
    
    DFD = 1 - sum((T[:,1]/len(agents))**2) #This is the first formula in the Bunderson & Sutcliffe, 2002 paper
    DFD = DFD/maxDFD #This is the normalization they mention on page 885 below the formula


    """
    %% Calculate IFD
    % First calculate IFDS
    IFDS = 1 - sum((agents./sum(agents,2)).^2, 2);
    IFD = mean(IFDS);
    fprintf('Group-average intrapersonal dominant functional diversity of this group of agents is: %0.4f\n', IFD)
    clear IFDS
    """
    #Calculate IFD
    #IFDS = 1 - sum((agents./sum(agents,2)).^2, 2)
    #IFDS = 1 - agents/agents.sum(axis=1)
    IFDS = 1 - np.array([sum(((a/sum(a))**2)) for a in agents])
    IFD = np.mean(IFDS)
    return [DFD, IFD]

#x= calc_fd(np.array([[0.4,0.6,0,0], [0,0,0.6, 0.4]]))