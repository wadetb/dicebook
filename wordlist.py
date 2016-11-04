#!/usr/bin/python3

with open('eff_short_wordlist_2_0.txt', 'r') as f:
	words = [l.strip().split('\t') 
		     for l in f.readlines()]

wrap=100

for w in words:
	print(w[0], w[1], '\\\\')
