#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 15:36:11 2021

@author: carolineskalla
"""
import numpy as np
import matplotlib.pyplot as plt
import generate_agents
import calc_fd



team1 = np.array([[10,0,0,0,0,0,0,0,0],[10,0,0,0,0,0,0,0,0],[10,0,0,0,0,0,0,0,0],[10,0,0,0,0,0,0,0,0]])
team2 = np.array([[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1]])
team3 = np.array([[10,0,0,0,0,0,0,0,0],[0,10,0,0,0,0,0,0,0],[0,0,10,0,0,0,0,0,0],[0,0,0,10,0,0,0,0,0]])
team4 = np.array([[1.1,1,1,1,1,1,1,1,1],[1,1.1,1,1,1,1,1,1,1],[1,1,1.1,1,1,1,1,1,1],[1,1,1,1.1,1,1,1,1,1]])
team5 = np.array([[5,1,0,2,0,3,0,0,0],[2,0,0,1,1,1,1,1,1],[0,10,0,0,0,0,0,0,0],[7,0,0,3,0,0,0,0,0]])

#def place_on_plane(agents):
teams = [team1, team2, team3, team4, team5]   

IFD =  np.zeros(len(teams))
DFD = np.zeros(len(teams))
i = 0
for team in teams:
    DFD[i], IFD[i] = calc_fd.calc_fd(team)
    i+=1




fig, ax = plt.subplots()
ax.scatter(IFD, DFD, color='black')
# plt.scatter(x, y, marker='o');
# fig.scatter(IFD, DFD)
ax.set_xlabel('IFD', size=14)
ax.set_ylabel('DFD', size=14)
ax.set_title('IFD-DFD Plane', y= 1.07, size=18)
plt.show


#annotate points
plt.annotate("Team 1", (IFD[0] + 0.01, DFD[0] + 0.04))
plt.annotate("Team 2", (IFD[1] - 0.09, DFD[1] + 0.05))
plt.annotate("Team 3", (IFD[2] + 0.03, DFD[2] - 0.02))
plt.annotate("Team 4", (IFD[3] - 0.08, DFD[3] - 0.08))
plt.annotate("Team 5", (IFD[4] + 0.02, DFD[4] + 0.05))

#legend
textstr = "Team Composition\n\n"
for i in range(len(teams)):
    textstr += ("Team " + str(i + 1) + ":\n")
    for j in range(len(teams[i])):
        textstr += "A" + str(j+1) + (str(teams[i][j]) + "\n")

props = dict(boxstyle='square', facecolor='white', alpha=0.5)
ax.text(1.05, 1, textstr, transform=ax.transAxes, fontsize=7.8,
        horizontalalignment="left",verticalalignment='top', bbox=props)
 


#place_on_plane(agents)

        