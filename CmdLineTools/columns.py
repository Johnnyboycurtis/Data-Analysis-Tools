#!/c/ProgramData/Miniconda3/python

import sys
import argparse

parser = argparse.ArgumentParser(description = "Process text files with deliminators (e.g. csv files)", 
        usage="zcat <file> | columns.py | less -S")
parser.add_argument('infile', nargs='?', type = argparse.FileType('r'),
        default = sys.stdin)
parser.add_argument('outfile', nargs = '?', type = argparse.FileType('w'),
        default = sys.stdout)
parser.add_argument('--sep', default = '|',
        help = 'Seperator for your file')
parser.add_argument('--cols', default = None, 
        help = "Select which columns you'd like to see")


def parseColArg(cols):
    ''' return a list '''
    cols2Keep = [(int(i)-1) for i in cols.split(',')]
    return cols2Keep


def readData(data, sep, outfile, cols=None):
    for i, line in enumerate(data):
        recs = line.strip().split(sep)
        if i == 0:
            ## annotate the column
            recs = [str(i+1) + ':' + rec for i,rec in enumerate(recs)]
        if cols:
            ## get subset of columns
            tmp = [col.ljust(10, " ") for i,col in enumerate(recs) if i in cols]
            out = "\t|".join(tmp)
        else:
            out = "\t|".join([rec.ljust(10, " ") for rec in recs])
        ## then write to stdout
        try:
            outfile.write(out + "\n")
        except OSError:
            sys.exit(1)


if __name__ == "__main__":
    args = parser.parse_args()
    if args.cols:
        cols = parseColArg(args.cols)
    else:
        cols = None
    readData(args.infile, args.sep, args.outfile, cols)
    sys.exit(1)

