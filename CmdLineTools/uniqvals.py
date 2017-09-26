#!/c/ProgramData/Miniconda3/python
import argparse
import sys
from tqdm import tqdm

parser = argparse.ArgumentParser(description = "Parse file and get unique values based on keys", 
        usage="cat <file> | uniqvals.py -s, -c 2,3,4 -v 1 > results.txt")
parser.add_argument('infile', nargs='?', type = argparse.FileType('r'),
        default = sys.stdin)
parser.add_argument('outfile', nargs = '?', type = argparse.FileType('w'),
        default = sys.stdout)
parser.add_argument('-s', '--sep', default = ",", help = "column seperator")
parser.add_argument('-c', '--cols', required=True, help = "columns for which to use as keys")
parser.add_argument('-v', '--values', required=True, help = "columns for which to use as values")



## columns : Provider_SK,lname,fname,tin,providername,state,zipcode,phone
def parseColArg(cols):
    ''' return a list '''
    cols2Keep = [(int(i)-1) for i in cols.split(',')]
    return cols2Keep

#keys = [1,2,3,4,5,6,7]


def readData(infile, cols, values):
    data = {}
    for line in tqdm(infile):
        recs = line.strip().split(",")
        key = [recs[i] for i in cols]
        vals = [recs[i] for i in values]
        key = ",".join(key)
        currdata = data.get(key, [])
        currdata += vals
        data[key] = currdata
    return data

def writeOut(data):
    for k, vals in data.items():
        n = str(len(vals))
        #providersk = "|".join([str(sk) for sk in vals])
        providersk = str(vals) ## keep it as a list
        out = k + "," + n + "," + providersk
        print(out)

if __name__ == "__main__":
    args = parser.parse_args()
    cols = parseColArg(args.cols)
    values = parseColArg(args.values)
    results = readData(args.infile, cols, values)
    writeOut(results)
    sys.exit(1)

