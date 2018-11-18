#!/usr/local/bin/python3
# Creator: Irina Golovko
# Name: graph2.py
# Description: Using different line style,
# colors and markers in matplotlib.
# Date: July 15, 2018


import numpy as np
import matplotlib.pyplot as plt
# evenly sampled time at 200ms intervals using np.arrange: 
# Read the documentation: https://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html
t = np.arange(0., 5., 0.2) 
# yellow line style "- -" , cyan filled plus and magenta stars
plt.plot(t, t, 'y:', t, t**2, 'cP', t, t**3, 'm*')
plt.show()
