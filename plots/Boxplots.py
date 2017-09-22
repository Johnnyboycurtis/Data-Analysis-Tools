#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 16:23:23 2016

@author: jonathan
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import pandas as pd



  
def boxplot(dataframe, linewidth=2, fontsize = 14, xlabel=None, ylabel=None, title=None):
    ax_tuple = dataframe.boxplot(return_type = 'both', fontsize = fontsize)
    axes = ax_tuple[0]
    dict_features = ax_tuple[1]
    for x in dict_features.keys():
        category = dict_features[x]
        for ax in category:
            plt.setp(ax, linewidth=2)
            if x == 'fliers':
                plt.setp(ax, marker= 'x', markerfacecolor = 'gray', markersize = 10)
    for tick in axes.yaxis.get_major_ticks():
        tick.label.set_fontsize(fontsize)
    axes.set_xlabel(xlabel, fontsize = fontsize)
    axes.set_ylabel(ylabel, fontsize = fontsize)
    axes.set_title(title, fontsize = fontsize)
    return axes

    
## examples    
data = np.square(np.random.normal(2,3,(40,3)))
df = pd.DataFrame(data = data, columns = list('abc'))


boxplot(df, linewidth = 2, xlabel="x-axis", ylabel="y-axis", title="Boxplot")




import seaborn as sns

ax_sns = sns.boxplot(data = df)
ax_sns.set_xlabel("x-axis here", fontdict = {'fontsize': 16})
for tick in ax_sns.yaxis.get_major_ticks():
    tick.label.set_fontsize(14)
for tick in ax_sns.xaxis.get_major_ticks():
    tick.label.set_fontsize(14)
    
