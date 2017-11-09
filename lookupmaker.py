import csv
import numpy as np
import sys

# program takes input where first column is z values (ideally in meters for later stuff but whatever) and second is voltages.

inloc = sys.argv[1] # Location of lookup table
outloc = sys.argv[2] # place to dump numpy array to

with open(inloc, 'rb') as csvfile:
	reader = csv.reader(csvfile)
	zs = []
	vs = []
	a = 0
	for row in reader:
		zs += [row[0]]
		vs += [row[1]]
	zarr = np.array(zs, dtype=np.float64)
	varr = np.array(vs, dtype=np.float64)
	lookup = np.array([zarr, varr])
	lookup.dump(outloc)