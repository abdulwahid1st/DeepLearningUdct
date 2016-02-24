# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 06:53:05 2016

@author: abdul
"""

"""Softmax."""

scores = [3.0, 1.0, 0.2]

import numpy as np

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    res = np.exp(x) / np.sum(np.exp(x), axis=0);
    print (res);
    return res;
    
print(softmax(scores))

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()