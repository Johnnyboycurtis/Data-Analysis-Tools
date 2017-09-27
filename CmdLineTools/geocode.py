import sys
from tqdm import tqdm
import argparse
import googlemaps

parser = argparse.ArgumentParser(description = "Geocode addresses", 
        usage = "cat <file> | geocode.py -s, -c 2,3,5 -k C:/Users/Jonathan/googlemaps-api-key.txt > results.txt")
parser.add_argument('infile', nargs='?', type = argparse.FileType('r'),
        default = sys.stdin)
parser.add_argument('outfile', nargs = '?', type = argparse.FileType('w'),
        default = sys.stdout)
parser.add_argument('-s', '--sep', default = ",", help = "column seperator")
parser.add_argument('-c', '--cols', required=True, help = "columns for which to use as address components")
parser.add_argument('-k', '--key', type = argparse.FileType('r'), required = True,
        default = "L:/googlemaps-api-key.txt", help = "Google Maps API Key file location")

def parseColArg(cols):
    ''' return a list '''
    cols2Keep = [(int(i)-1) for i in cols.split(',')]
    return cols2Keep

def geocode(client, address):
    gresult, = client.geocode(address)
    formatted_address = gresult['formatted_address']
    geometry = gresult['geometry'] ## dictionary
    location = geometry['location'] ## location: {'lat': 26.6332603, 'lng': -81.9558283}
    location['formatted_address'] = formatted_address
    return location

def processData(data, cols, sep, client):
    results = []
    for line in tqdm(data):
        line = line.strip().split(sep)
        address = [line[i] for i in cols]
        address = " ".join(address)
        resuls.append( geocode(client, address) )
    df = pd.DataFrame(results)
    return df



if __name__ == "__main__":
    args = parser.parse_args()
    key = args.key.readline().strip()



