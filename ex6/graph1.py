#!/usr/local/bin/python3
# Creator: Irina Golovko
# Name: graph1.py
# Description: Creating a graph of the blue squares 
# of the odd numbers between 1 and 100 
# Date: July 15, 2018


import numpy as np
import matplotlib.pyplot as plt

t = np.arange(1, 100, 2)

plt.plot(t, t**2, 'bs')
plt.title('Graph of odd numbers between 1 and 100')
plt.ylabel('Odd numbers')
plt.show()
