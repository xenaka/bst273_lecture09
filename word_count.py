#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser( description="" )
#add argument
parser.add_argument(
	"data_file",
	help="path to the file we want to read",
)

#-------------------------------------------------------------------------------
# Are there other arguments we need?
#-------------------------------------------------------------------------------

args = parser.parse_args( )
fh = open(args.data_file)

print("the fh is",fh)

lines = 0  #want it to be a number
words = 0
chars = 0

for line in fh:
	#print(line) for verification
#-------------------------------------------------------------------------------
# our code for analyzing the data
#-------------------------------------------------------------------------------

#TO VERIFY at the beginning
##args = parser.parse_args()
#print(args)
#print(args.data_file)
