#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 17:04:46 2021

@author: carolineskalla
"""
import similarity
import numpy as np

def calc_threshold(agents, threshold):
    matrix = similarity.gen_dist_matrix(agents)
    a_min = np.amin(matrix)
    a_max = np.amax(matrix)
    
    #0.7 would indicate that the threshold is at the 70% of the range of distances
    t = a_min + (threshold*(a_max - a_min))
    
    return t
    
    