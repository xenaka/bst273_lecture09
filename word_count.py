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

#-------------------------------------------------------------------------------
# our code for analyzing the data
#-------------------------------------------------------------------------------
args = parser.parse_args()
print(args)
print(args.data_file)
