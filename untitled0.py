#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 09:33:21 2022

@author: carolineskalla
"""
import math 
import calc_fd 
#IFD ranges from 0 to 1
#DFD ranges from 0 to 1

"""
Parameters:
    - choose gen/spec
    - choose IFD/DFD
"""

#gs_ratio = 0.3 --> 3 generalists to 7 specialists
def gen_agents_1(gs_ratio, num_a):
    
    #calculate number of generalists
    num_g = math.ceil(gs_ratio * num_a)
    num_s = num_a - num_g
    
    
    
    