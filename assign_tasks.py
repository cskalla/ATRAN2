#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 13:22:38 2021

@author: carolineskalla
"""
import random
def assign_tasks(agents, tasks):
    #agents are randomly assigned to tasks 
    #all agents get a task and agents can get the same task right now
    index = [random.randint(0,len(tasks)-1) for i in range(len(agents))]
    return index