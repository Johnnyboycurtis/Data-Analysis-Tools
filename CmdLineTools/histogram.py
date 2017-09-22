#!/c/ProgramData/Miniconda3/python


import sys
import operator
import argparse
import collections
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from bkcharts import Bar, output_file, show
from tqdm import tqdm



plt.style.use('ggplot')

parser = argparse.ArgumentParser(description = "Create a histogra/barplot of values")
parser.add_argument('infile', nargs='?', type = argparse.FileType('r'),
        default = sys.stdin)
parser.add_argument('outfile', nargs = '?', type = argparse.FileType('w'),
        default = sys.stdout)
parser.add_argument('--sortbyvals', action='store_true')
parser.add_argument('--density', action='store_true')
parser.add_argument('--plot', action='store_true')


def getCounts(data, sortedByVals=False):
    tmp = {} ## alternative: collections.defaultdict
    for line in tqdm(data):
        ## do something
        line = line.strip() ## remove any escape characters: \n, \t
        count = tmp.get(line, 0) ## get current count
        count += 1
        tmp[line] = count
    if sortedByVals:
        results = collections.defaultdict()
        sorted_vals = sorted(tmp.items(), key=operator.itemgetter(1))
        sorted_vals.sort(key = lambda y: y[1], reverse=True) ## sorts in place
        for key,val in sorted_vals:
            results[key] = val
    else:
        results = tmp
    return results
        


def plot(data, density, topN=20):
    '''data should be a dictionary'''
    keys = data.keys()
    vals = list(data.values())
    n = len(keys)
    if density:
        vals = np.array(vals)
        denom = np.sum(vals) ## denominator
        prop = vals / denom
        plt.bar(left = range(n), height = prop, width = 0.5, align = 'center')
        plt.xticks(range(n), keys)
        plt.xlabel("Values")
        plt.ylabel("Density")
    else:
        plt.bar(left = range(n), height = vals, width = 0.5, align = 'center')
        plt.xticks(range(n), keys, rotation = 'vertical')
        plt.xlabel("Values")
        plt.ylabel("Counts")
    if topN:
        plt.xlim((-1, topN))
    plt.savefig("test-figure.png")



def bokehbar(data):
    '''data should be a dictionary'''
    keys = data.keys()
    vals = list(data.values())
    n = len(keys)
    df = pd.DataFrame(data = list(zip(keys, vals)), columns = ['Value', 'Count'])
    p = Bar(df, 'Value', values='Count', title="Bar plot of values")
    #p = figure(plot_width=500, plot_height=300)
    #p = Bar(x=range(n), width=0.4, bottom=0,
    #    top = vals, color="firebrick")
    p.title.text = "Title With Options"
    p.xaxis.axis_label = 'Values'
    p.yaxis.axis_label = 'Counts'
    output_file('vbar2-test.html')
    show(p)


def textplot(data, outfile):
    '''data should be a dictionary'''
    keys = data.keys()
    vals = list(data.values())
    n = len(keys)
    length = max((len(k) for k in keys)) ## get length of keys
    length = max((length, 6))
    vals = np.array(vals)
    denom = np.sum(vals) ## denominator
    bars = ((vals / denom) * 50) // 1
    percents = np.round(vals / denom, 5) * 100

    ## write header
    header = "|".join(["field".ljust(length, " "), " "*50, "count", "percentage"])
    outfile.write(header + "\n")

    ## write data out to stdout
    outputdata = list(zip(keys, bars, vals, percents))
    outputdata.sort(key = lambda line: line[3], reverse = True)
    for k, prop, count, percent in outputdata:
        idx = k.ljust(length, " ")
        bar = ("="  * int(prop)).ljust(50, " ")
        count = str(count).ljust(5, " ")
        percent = str(percent).ljust(10, " ")
        line = "|".join([idx, bar, count, percent])
        outfile.write(line + "\n")
    

if __name__ == "__main__":
    args = parser.parse_args()
    results = getCounts(args.infile, args.sortbyvals)
    if args.plot:
        #plot(results, args.density)
        bokehbar(results)
    else:
        textplot(results, args.outfile)
    sys.exit(1)
