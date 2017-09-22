#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 14:39:02 2016

@author: jonathan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.available
plt.style.use('ggplot')
import matplotlib
from matplotlib.ticker import FuncFormatter


## see: http://matplotlib.org/examples/pylab_examples/histogram_percent_demo.html
def to_percent(y, position):
    # Ignore the passed in position. This has the effect of scaling the default
    # tick locations.
    s = str(100 * y)

    # The percent symbol needs escaping in latex
    if matplotlib.rcParams['text.usetex'] is True:
        return s + r'$\%$'
    else:
        return s + '%'




def plot_histograms(df, x, y, probability = True, axisfontsize = 13):
    cols = df.columns
    fig,ax=plt.subplots(x,y,figsize=(20,10))
    axes = [m for m in ax.flat]
    stuff = map(None, cols, axes) ## function = None; will not work in Python3

    for xy in stuff:
        col = xy[0]
        if col == None:
            fig.delaxes(xy[1])
        else:
            axis = xy[1]
            data = df[col].dropna()
            if probability:
                w = np.ones(data.shape[0])/data.shape[0]
                data.hist(ax = axis, weights = w, xlabelsize = axisfontsize, ylabelsize = axisfontsize)
                axis.yaxis.set_major_formatter(formatter)
            else:
                data.hist(ax = axis) ## changed this from axis.hist(data)
            axis.set_title(col)
    return ax


def apply_titles(x_labels, y_labels, titles, axes):
    stuff = map(None, x_labels, y_labels, titles, axes)
    for s in stuff:
        ax = s[3]
        ax.set_xlabel(s[0])
        ax.set_ylabel(s[1])
        ax.set_title(s[2])
    return axes

    

    
    




    
    
    