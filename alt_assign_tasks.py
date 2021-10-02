#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 11:13:01 2021

@author: carolineskalla
"""

import random

def init_assign_tasks(agents, tasks):
    #agents are randomly assigned to tasks 
    #all agents get a task and agents can get the same task 
    index = [random.randint(0,len(tasks)-1) for i in range(len(agents))]
    
    return index


def new_task(agents, tasks):
    #agents are randomly assigned to tasks 
    #all agents get a task and agents can get the same task right now
    index = random.randint(0,len(tasks)-1)
    
    return index