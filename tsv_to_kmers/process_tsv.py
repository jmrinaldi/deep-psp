#!/usr/bin/env python

import argparse

"""
File: process_tsv.py

Get the specified annotation regions from a uniprot TSV and
write them to a file.

"""

def main() :
	"""
	Read command line arguments and invoke filterTSV()
	"""

	parser = argparse.ArgumentParser(description='Filter a uniprot TSV based on annotation')
	parser.add_argument('--inputTSV', help='input TSV file', required=True)
	parser.add_argument('--outputTSV', help='output TSV file', required=True)
	parser.add_argument('--annot', help='annotation to select', required=True)
	parser.add_argument('--minlen', help='minimum length', required=True)
	parser.add_argument('--maxlen', help='maximum length', required=True)
	args = parser.parse_args()

	filterTSV(annot=args.annot, maxlen=args.maxlen, minlen=args.minlen,
		input_tsv=args.inputTSV, output_path=args.outputTSV)

def filterTSV(annot, maxlen, minlen, input_tsv, output_path) :

	"""
	Get all of the specified annotation regions from a TSV that have
	minlen <= length <= maxlen. Write them to a TSV file.
	"""

	with open(output_path, 'w') as out_f :
		for line in open(input_tsv) :
			l = line.strip().split('\t')
			if len(l) < 6 or l[1] != annot : continue
			start = int(l[3])
			stop = int(l[4])
			length = stop - start
			if length < minlen or length > maxlen : continue
			seq = l[5][start-1:stop-1] # positions are 1-based
			out_f.write('%s\t%s\t%s\t%s' % (l[0], l[1], l[2], seq))

if __name__ == '__main__' : main()