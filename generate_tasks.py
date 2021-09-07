#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 15:57:41 2021

@author: carolineskalla
"""
import random
import numpy as np

def gen_tasks(nfuncs, ntasks, tnorm):
    """
    function tasks = GenTask(nf, nt, no)

    %% Generate tasks
    tasks = rand(nt, nf);
    tasks = tasks./sum(tasks, 2)*no;

end
    """


    tasks = np.random.rand(ntasks,nfuncs)

    tasks = (np.divide(tasks.T,np.sum(tasks, axis=1)).T)*tnorm
    return tasks

    
#t = gen_tasks(9,10,10)