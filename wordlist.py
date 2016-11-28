#!/usr/bin/python3
import sys

with open(sys.argv[1], 'r') as f:
	words = [l.strip().split('\t') 
		     for l in f.readlines()]

wrap=100

for w in words:
	print(w[0], w[1], '\\\\')
