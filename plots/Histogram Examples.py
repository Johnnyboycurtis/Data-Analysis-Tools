#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 18:43:03 2016

@author: jonathan
"""

import os
os.chdir("/home/jonathan/PyDATools/plots")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.available
plt.style.use('ggplot')
import Histograms


df = pd.DataFrame(data=np.random.randn(10, 3), columns = list('abc'))

axes = df.hist(bins = 20, xlabel = "gjhk")
#plt.show()

        
        
        
    
        
a = np.random.normal(size=200)
b = np.random.normal(size=200)
c = np.random.rand(100)

fig1 = plt.figure()
ax1 = fig1.add_subplot(1, 1, 1)
n, bins, patches = ax1.hist(a)
ax1.set_xlabel('Angle a (degrees)')
ax1.set_ylabel('Frequency')

fig2 = plt.figure()
ax2 = fig2.add_subplot(1, 1, 1)
n, bins, patches = ax2.hist(b)
ax2.set_xlabel('Angle b (degrees)')
ax2.set_ylabel('Frequency')



fig = plt.figure()
ax1 = fig.add_subplot(3, 1, 1)
ax2 = fig.add_subplot(3, 1, 2)
ax3 = fig.add_subplot(3, 2, 1)

n, bins, patches = ax1.hist(a)
ax1.set_xlabel('Angle a (degrees)')
ax1.set_ylabel('Frequency')

n, bins, patches = ax2.hist(b)
ax2.set_xlabel('Angle b (degrees)')
ax2.set_ylabel('Frequency')


n, bins, patches = ax3.hist(c)
ax3.set_xlabel('Angle c (degrees)')
ax3.set_ylabel('Frequency')







###HISTOGRAMS OF INSULIN DELIVER IN PERCENTAGE OF BOLUSSIZE
cols = df.columns
x = 2
y = 2
fig,ax=plt.subplots(x,y,figsize=(20,10))

i = 0
axes = [m for m in ax.flat]
stuff = map(None, cols, axes) ## function = None

for xy in stuff:
    col = xy[0]
    if col == None:
        fig.delaxes(xy[1])
    else:
        axis = xy[1]
        data = df[col]
        axis.hist(data)
        axis.set_title(col)




## run the following as a single block
ax = Histograms.plot_histograms(df, 2, 2)
    
g = np.repeat('x-axis', 3)
h = np.repeat('y-axis', 3)
j = np.repeat(None, 3)

Histograms.apply_titles(g, h, j, ax)




# Make a normed histogram. It'll be multiplied by 100 later.
ax = df.hist(column = 'a', bins=50, normed=True)

# Create the formatter using the function to_percent. This multiplies all the
# default labels by 100, making them all percentages
formatter = Histograms.FuncFormatter(Histograms.to_percent)

# Set the formatter
#plt.gca().yaxis.set_major_formatter(formatter)
ax[0][0].yaxis.set_major_formatter(formatter)

#plt.show()
    
    