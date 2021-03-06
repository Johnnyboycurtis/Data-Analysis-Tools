#!/c/ProgramData/Miniconda3/python

import sys
from tqdm import tqdm
import argparse
import googlemaps
import pandas as pd

parser = argparse.ArgumentParser(description = "Geocode addresses", 
        usage = "cat <file> | geocode.py -s, -c 2,3,5 -k C:/Users/JaneDoe/api-key.txt > results.txt")
parser.add_argument('infile', nargs='?', type = argparse.FileType('r'),
        default = sys.stdin)
parser.add_argument('outfile', nargs = '?', type = argparse.FileType('w'),
        default = sys.stdout)
parser.add_argument('-s', '--sep', default = ",", help = "column seperator")
parser.add_argument('-c', '--cols', required=True, help = "columns for which to use as address components")
parser.add_argument('-k', '--key', type = argparse.FileType('r'),
        default = "L:/googlemaps-api-key.txt", help = "Google Maps API Key file location (required)")

def parseColArg(cols):
    ''' return a list '''
    cols2Keep = [(int(i)-1) for i in cols.split(',')]
    return cols2Keep

def geocode(client, address):
    gresult = client.geocode(address)
    #print(type(gresult), len(gresult), file=sys.stderr)
    gresult = gresult[0]
    try:
        formatted_address = gresult['formatted_address']
        geometry = gresult['geometry'] ## dictionary
        location = geometry['location'] ## location: {'lat': 26.6332603, 'lng': -81.9558283}
        location['formatted_address'] = formatted_address
        location['original_address'] = address
    except TypeError:
        location = {'lat': '', 'lng': '', 'formatted_address': '', 'original_address': ''}
    return location

def processData(data, cols, sep, client, outfile):
    results = []
    for line in tqdm(data):
        line = line.strip().split(sep)
        address = [line[i] for i in cols]
        address = " ".join(address)
        if len(address) > 2:
            #print(address, file=sys.stderr)
            results.append( geocode(client, address) )
        else:
            results.append({'lat': '', 'lng': '', 'formatted_address': '', 'original_address': ''})
            print("problem with " + str(line), file=sys.stderr)
    df = pd.DataFrame(results)
    #df.to_csv("geocode-results.txt", sep="\t")
    df.to_csv(outfile, sep="\t", index_label="Index")
    sys.exit(1)
    #return df



if __name__ == "__main__":
    args = parser.parse_args()
    key = args.key.readline().strip()
    print("key" + str(key), file=sys.stderr)
    gmaps = googlemaps.Client(key = key)
    cols = parseColArg(args.cols)
    processData(args.infile, cols = cols, sep = args.sep, client= gmaps, outfile=args.outfile)



