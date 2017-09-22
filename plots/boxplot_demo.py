"""
Demo of the new boxplot functionality
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import pandas as pd

# fake data
np.random.seed(937)
data = np.random.lognormal(size=(37, 4), mean=1.5, sigma=1.75)
labels = list('ABCD')
fs = 10  # fontsize

# demonstrate how to toggle the display of different elements:
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(6, 6))
axes[0, 0].boxplot(data, labels=labels)
axes[0, 0].set_title('Default', fontsize=fs)

axes[0, 1].boxplot(data, labels=labels, showmeans=True)
axes[0, 1].set_title('showmeans=True', fontsize=fs)

axes[0, 2].boxplot(data, labels=labels, showmeans=True, meanline=True)
axes[0, 2].set_title('showmeans=True,\nmeanline=True', fontsize=fs)

axes[1, 0].boxplot(data, labels=labels, showbox=False, showcaps=False)
axes[1, 0].set_title('Tufte Style \n(showbox=False,\nshowcaps=False)', fontsize=fs)

axes[1, 1].boxplot(data, labels=labels, notch=True, bootstrap=10000)
axes[1, 1].set_title('notch=True,\nbootstrap=10000', fontsize=fs)

axes[1, 2].boxplot(data, labels=labels, showfliers=False)
axes[1, 2].set_title('showfliers=False', fontsize=fs)

for ax in axes.flatten():
    ax.set_yscale('log')
    ax.set_yticklabels([])

fig.subplots_adjust(hspace=0.4)
plt.show()


# demonstrate how to customize the display different elements:
boxprops = dict(linestyle='--', linewidth=3, color='darkgoldenrod')
flierprops = dict(marker='o', markerfacecolor='green', markersize=12,
                  linestyle='none')
medianprops = dict(linestyle='-.', linewidth=2.5, color='firebrick')
meanpointprops = dict(marker='D', markeredgecolor='black',
                      markerfacecolor='firebrick')
meanlineprops = dict(linestyle='--', linewidth=2.5, color='purple')

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(6, 6))
axes[0, 0].boxplot(data, boxprops=boxprops)
axes[0, 0].set_title('Custom boxprops', fontsize=fs)

axes[0, 1].boxplot(data, flierprops=flierprops, medianprops=medianprops)
axes[0, 1].set_title('Custom medianprops\nand flierprops', fontsize=fs)

axes[0, 2].boxplot(data, whis='range')
axes[0, 2].set_title('whis="range"', fontsize=fs)

axes[1, 0].boxplot(data, meanprops=meanpointprops, meanline=False,
                   showmeans=True)
axes[1, 0].set_title('Custom mean\nas point', fontsize=fs)

axes[1, 1].boxplot(data, meanprops=meanlineprops, meanline=True, showmeans=True)
axes[1, 1].set_title('Custom mean\nas line', fontsize=fs)

axes[1, 2].boxplot(data, whis=[15, 85])
axes[1, 2].set_title('whis=[15, 85]\n#percentiles', fontsize=fs)

for ax in axes.flatten():
    ax.set_yscale('log')
    ax.set_yticklabels([])

fig.suptitle("I never said they'd be pretty")
fig.subplots_adjust(hspace=0.4)
plt.show()



d = np.square(np.random.randn(100))


plot2 = plt.boxplot(d)
for x in plot2.keys():
    print(x)
    plt.setp(plot2[x], linewidth=2)
    
plt.setp(plot2['fliers'],  markersize=10)




## pandas

d = np.random.normal(2,3,(100, 3))
df = pd.DataFrame(data = d, columns = list('abc'))

axes = df.boxplot(return_type='dict')
axes.keys()
for x in ['boxes', 'fliers', 'medians', 'means', 'whiskers', 'caps']:
    category = axes[x]
    for ax in category:
        print(x)
        plt.setp(ax, linewidth=2)
        if x == 'fliers':
            plt.setp(ax, marker= 'x', markerfacecolor = 'gray', markersize = 10)
    




import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import pandas as pd



data = np.random.normal(2,3,(40,3))

df = pd.DataFrame(data = data, columns = list('abc'))


ax_dict = df.boxplot(return_type='both')
axes = ax_dict[0]
dict_features = ax_dict[1]
## then for 
for tick in axes.xaxis.get_major_ticks():
    tick.label.set_fontsize(20)



ax_tuple = df.boxplot(return_type = 'both')
axes = ax_tuple[0]
dict_features = ax_tuple[1]
for x in dict_features.keys():
    category = dict_features[x]
    for ax in category:
        plt.setp(ax, linewidth=2)
        if x == 'fliers':
            plt.setp(ax, marker= 'x', markerfacecolor = 'gray', markersize = 10)
for tick in axes.yaxis.get_major_ticks():
    tick.label.set_fontsize(20)
