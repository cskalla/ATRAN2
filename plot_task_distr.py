#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 09:56:52 2021

@author: carolineskalla
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 12:30:23 2021

@author: carolineskalla
"""
import matplotlib.pyplot as plt

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
import similarity
import assign_tasks2
import calc_threshold

#Parameters:
numfuncs = 9
numagents = 10
#gDiv = np.repeat(1/nfunc, 9)
#gDiv = [1/numfuncs for i in range(0,9)]
gDiv2 = 1.00000000e-01
gDiv1 = 1000
#gDiv = [1, 0, 0, 0, 0, 0, 0, 0, 0]
anorm = 10; #The sum of capabilities of agents,
aDiv1 = [1,10]#This is where intra-agent diversity can be set: the higher, the more diverse
aDiv2 = [100,10]
tnorm = 10
numtasks=100
stop = 5000

#generate agents
#agents = GenAgent(par.numfuncs, par.numagents, [adiv, par.agspread], exp((-(0:par.numfuncs-1).^2)/gdiv), par.anorm)
#agents1 = generate_agents.gen_agents(numfuncs, numagents, aDiv1, (np.exp(-(np.array(range(0, numfuncs))**2/gDiv1)))/sum(np.exp(-(np.array(range(0, numfuncs))**2/gDiv1))), anorm)
#agents2 = generate_agents.gen_agents(numfuncs, numagents, aDiv2, (np.exp(-(np.array(range(0, numfuncs))**2/gDiv2)))/sum(np.exp(-(np.array(range(0, numfuncs))**2/gDiv2))), anorm)
#agents = generate_agents.gen_agents(numfuncs, numagents, aDiv, (np.exp(-(np.array(range(0, numfuncs))**2/gDiv))), anorm)
#plot_skills_distr(agents)
#plot_skills_distr(agents)
#print((sum(np.exp(-(np.array(range(0, numfuncs))**2/gDiv)))))
#print((sum(np.exp(-(np.array(range(0, numfuncs))**2/gDiv)))/sum(np.exp(-(np.array(range(0, numfuncs))**2/gDiv)))))
tasks = generate_tasks.gen_tasks(numfuncs, numtasks, tnorm)

#each bar will be an agent, each section of the bar represents a functional area, the x axis will represent the skill strength of each functional area.




a_names = ["Agent 1", "Agent 2", "Agent 3", "Agent 4", "Agent 5", "Agent 6", "Agent 7", "Agent 8", "Agent 9", "Agent 10"]
n_t = [str(x) for x in range(100)]
print(n_t)
#input functional areas:
fa1 = tasks[:,0] 
fa2 = tasks[:,1] 
fa3 = tasks[:,2] 
fa4 = tasks[:,3] 
fa5 = tasks[:,4]
fa6 = tasks[:,5]
fa7 = tasks[:,6]
fa8 = tasks[:,7]
fa9 = tasks[:,8]


#fig = plt.figure()
#ax = fig.add_subplot(141)
fig = plt.figure(figsize=(20,20))
ax = fig.add_subplot(111)

#ax1.plot(x, y)
#ax2.plot(x, -y)
l = 0
lab = []
for i in range(len(tasks[0])):
    f = tasks[:,i]
    print(f)
    print("\n")
    lab.append(ax.barh(n_t, f, align='center', height=.25, left=l))
    l += f
    
"""
ax.barh(a_names, fa1, align='center', height=.25, label=fa1)
ax.barh(a_names, fa2, align='center', height=.25, left=fa1,label=fa2)
ax.barh(a_names, fa3, align='center', height=.25, left=fa1+fa2,label=fa3)
ax.barh(a_names, fa4, align='center', height=.25, left=fa1+fa2+fa3,label=fa4)
ax.barh(a_names, fa5, align='center', height=.25, left=fa1+fa2+fa3+fa4,label=fa5)
ax.barh(a_names, fa6, align='center', height=.25, left=fa1+fa2+fa3+fa4+fa5,label=fa6)
ax.barh(a_names, fa7, align='center', height=.25, left=fa1+fa2+fa3+fa4+fa5+fa6,label=fa7)
ax.barh(a_names, fa8, align='center', height=.25, left=fa1+fa2+fa3+fa4+fa5+fa6+fa7,label=fa8)
ax.barh(a_names, fa9, align='center', height=.25, left=fa1+fa2+fa3+fa4+fa5+fa6+fa7+fa8,label=fa9)
"""


"""
ax.barh(a_names, fa1, align='center', height=.25)
ax.barh(a_names, fa2, align='center', height=.25,label=fa2)
ax.barh(a_names, fa3, align='center', height=.25,label=fa3)
ax.barh(a_names, fa4, align='center', height=.25, label=fa4)
ax.barh(a_names, fa5, align='center', height=.25, label=fa5)
ax.barh(a_names, fa6, align='center', height=.25, label=fa6)
ax.barh(a_names, fa7, align='center', height=.25, label=fa7)
ax.barh(a_names, fa8, align='center', height=.25, label=fa9)
ax.barh(a_names, fa9, align='center', height=.25, label=fa9)
"""
#ax.set_yticks(n_t)
ax.set_xlabel('Required work in functional areas', fontsize= 35)
ax.set_ylabel('Tasks', fontsize= 35)
ax.set_title("Distribution of the required functional areas of tasks", fontsize=50)

ax.set_xticks([1,2,3,4,5,6,7,8,9,10])

#ax1.grid(True)
#ax.legend()
plt.tight_layout()
plt.margins(y=0.01,x = 0.01)
#plt.savefig('C:\\Data\\stackedbar.png')
labels = ['Functional area 0', 'Functional area 1', 'Functional area 2', 'Functional area 3', 'Functional area 4', 'Functional area 5', 'Functional area 6', 'Functional area 7', 'Functional area 8', 'Functional area 9']
#handles, labels = ax.get_legend_handles_labels()
fig.legend(lab, labels, loc='upper center', fontsize =35, bbox_to_anchor=(1.16, 0.98),
          fancybox=True, shadow=True, ncol=1)
plt.show()