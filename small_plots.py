#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 21:46:35 2021

@author: carolineskalla
"""

import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2)
#fig.suptitle('Horizontally stacked subplots')
ax1.axes.xaxis.set_ticks([])
ax1.axes.yaxis.set_ticks([])
ax2.axes.xaxis.set_ticks([])
ax2.axes.yaxis.set_ticks([])
#points
x = np.arange(0,100)
y = x
ax1.plot(x, y, color='black')
ax1.set_xlabel('IFD',size=14)
ax1.set_ylabel('Team Performance',size=14)
ax2.plot(x, -y,color='black')
ax2.set_xlabel('DFD', size=14)
ax2.set_ylabel('Team Performance', size=14)