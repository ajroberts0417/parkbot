#!/usr/bin/python

import argparse
import json

# create an argparser for the CLI tool https://docs.python.org/3.3/library/argparse.html
parser = argparse.ArgumentParser(description='parkbot is a CLI for querying parking spots.')

# add the data_path as a required argument, and a bunch of optional query parameters
parser.add_argument('data_path', metavar='data_path', type=str, action='store',
                   help='a path to the data, in JSON format')
parser.add_argument('-l', '--locate', dest='locate', action='store', type=str,
                   help='gives all the parking spots in the state (e.g. `$ parkbot data.json -l AZ`')
parser.add_argument('-lte', '--find_price_hourly_lte', dest='find_price_hourly_lte', action='store', type=int,
                   help='Finds all parking spots with hourly price <= given price IN CENTS (e.g. `$ parkbot data.json -lte 200`')
parser.add_argument('-gt', '--find_price_hourly_gt', dest='find_price_hourly_gt', action='store', type=int,
                   help='Finds all parking spots with hourly price > given price IN CENTS (e.g. `$ parkbot data.json -gt 200`')


# get all the args from the command line and store them in a NameSpace object
args = parser.parse_args()

# read from the data file given, and query the data based on the CLI arguments
with open(args.data_path, 'r') as data_file:
    data = json.load(data_file)

    if getattr(args, 'locate', None):
        data = [i for i in data if i['address']['state'] == args.locate]
    if getattr(args, 'find_price_hourly_lte', None):
        data = [i for i in data if i['price_hourly'] <= args.find_price_hourly_lte]
    if getattr(args, 'find_price_hourly_gt', None):
        data = [i for i in data if i['price_hourly'] > args.find_price_hourly_gt]

    # print the final result to stdout
    print([i['name'] for i in data])
