#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 16:10:30 2021

@author: carolineskalla
"""
import numpy as np
import random
import similarity
from more_itertools import sort_together

def init_assign_tasks(agents, tasks, threshold, max_agents_to_task, abandon_timer):
    #agents are randomly assigned to tasks
  
    #tasks can only have one agent, some agents may not have a task
    #index will contain min(len(tasks),len(agents)) number of ints between 0 and len(tasks), and if there are more 
    #index = [random.randint(0,len(tasks)-1) for i in range(len(agents))]
    #options = np.array(range(0, len(tasks)))
    #
    #if len(agents) <= len(tasks):
        #pick random indeices of tasks
        #indices = np.random.choice(options, len(agents))
    #else:
        #pick len(task) number tasks and assign to agents, otherwise fill with nan
       # l = [i for i in range(0, len(tasks))]
        #print(l)
        #random.shuffle(l)
       # print(l)
   indices = [-1 for i in range(len(agents))]
      
   for j in range(len(agents)):
            #print("hi2")
            indices[j] = new_task(j, agents, tasks, indices, threshold, max_agents_to_task, abandon_timer)
            
        #indices[len(tasks)] = new_task(len(tasks), agents, tasks, indices, threshold)
        #indices[len(tasks) + 1] = new_task(len(tasks + 1), agents, tasks, indices, threshold)
        
   return indices


#picks the most qualfied agent
def new_task(i, agents, tasks, indices, threshold, max_agents_to_task, abandon_timer):
    
    #identify stuck agents
    sa = stuck_agents(agents, tasks, indices, abandon_timer)
    if len(sa) > 0:
        #find the similarity between the tasks at the stuck agents and the current agent
        sa_ind = [indices[t] for t in sa]
        t_sim = []
        for t in sa_ind:
            t_sim.append(agent_task_sim(agents, tasks, i, t))
        #sort the unclaimed tasks by similarity
        srt = sorted(list(zip(t_sim, sa_ind)), reverse=False)
        unzip_srt_list = [[ i for i, j in srt ],[ j for i, j in srt ]]
        sorted_tasks = unzip_srt_list[1]
        #go through ranked task and check compatibility with other agents
        for t2 in sorted_tasks:
            if is_compatible(agents, indices, i, t2, threshold):
                num_a = agents_on_task(indices, t2)
                if len(num_a) < max_agents_to_task:
                    return t2  
    
    #identify unclaimed tasks
    unclaimed_t_ind = check_unclaimed(agents, tasks, indices)
    if len(unclaimed_t_ind) > 0:
        #calculate similarity between task and agent
        t_sim = []
        for t3 in unclaimed_t_ind:
            t_sim.append(agent_task_sim(agents, tasks, i, t3))
        
        #sort the unclaimed tasks by similarity
        #srt = sorted(list(zip(t_sim, unclaimed_t_ind)), reverse=False)
        #unzip_srt_list = [[ i for i, j in srt ],[ j for i, j in srt ]]
        #sorted_unclaimed_tasks = unzip_srt_list[1]
    
        #find the min of t_sim (the task with the smallest distance)
        min_ind = unclaimed_t_ind[t_sim.index(min(t_sim))]
        #return 88
        return min_ind
    else:
        task_ind = [i for i in range(0, len(tasks))]
        t_sim = []
        for t in task_ind:
            t_sim.append(agent_task_sim(agents, tasks, i, t))
        #sort the unclaimed tasks by similarity
        srt = sorted(list(zip(t_sim, task_ind)), reverse=False)
        unzip_srt_list = [[ i for i, j in srt ],[ j for i, j in srt ]]
        sorted_tasks = unzip_srt_list[1]
        #go through ranked task and check compatibility with other agents
        for t2 in sorted_tasks:
            if is_compatible(agents, indices, i, t2, threshold):
                num_a = agents_on_task(indices, t2)
                if len(num_a) < max_agents_to_task:
                    #return 88
                    return t2
        #agent will remain with no task
        return -1
    

#finds the tasks that are not currently assigned to agents
def check_unclaimed(agents, tasks, indices):
    unclaimed_t_ind = []
    task_ind = [i for i in range(0, len(tasks))]
    for t in task_ind:
        #if no agents are working on task t
        if indices.count(t) < 1:
            unclaimed_t_ind.append(t)
    return unclaimed_t_ind

#find the agents that are currently stuck on their task
def stuck_agents(agents, tasks, indices, abandon_timer):
    stuck_agents = []
    for i in range(len(agents)):
        if abandon_timer[i] > 1:
            stuck_agents.append(i)
    return stuck_agents


#finds the euclidian distance between an agent and a task    
def agent_task_sim(agents, tasks, a_ind, t_ind):
    #get agents 
    agent = agents[a_ind]
    task = tasks[t_ind]
    # finding sum of squares
    sum_sq = np.sum(np.square(agent - task))
 
    # Doing squareroot and
    # printing Euclidean distance
    #print(np.sqrt(sum_sq))
    return np.sqrt(sum_sq)

#returns the indices of any other agents working on the task
def is_compatible(agents, indices, i, t_ind, threshold):
    if indices.count(t_ind) < 1:
        return True
    else:
        a_ind = agents_on_task(indices, t_ind)        
        sims = np.zeros(len(a_ind))
        j = 0
        for a in a_ind:
            sims[j] = similarity.euc_dist(agents, i, a)
            j+=1
        #check to see if all agents working on this task pass the similarity threshold
        if np.all(sims < threshold):
            return True
        else:
            return False
  
#returns a list of agents that are currently working on a task
def agents_on_task(indices, t_ind):
    
    agt_list = []
    
    for i in range(len(indices)) :
        if indices[i] == ( t_ind) :
            agt_list.append(i)
    return agt_list

    
    
         
            
            
    