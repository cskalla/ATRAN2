#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 10:09:13 2021

@author: carolineskalla
"""
import assign_tasks2

#agents can only pass to another agent that doesn't have a task

def pass_task(agents, tasks,indices, i, threshold):
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
                if len(num_a) <= max_agents_to_task:
                    return t2
        #agent will remain with no task
        return -1
    