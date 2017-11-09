import csv
import numpy as np
import sys


def main():
	lookup = sys.argv[1]
	in_data = sys.argv[2]
	out_data = sys.argv[3]
	lookup = np.load(lookup)
	with open(in_data, 'rb') as csvfile:
		reader = csv.reader(csvfile) # content should just be a single column of voltage values
		voltages = []
		for row in reader:
			voltages += [row[0]] # just in case
		voltages = np.array(voltages, dtype=np.float64)
	positions = []
	for v in voltages:
		positions += [lookup[0, np.argmin(np.abs(lookup[1] - v))]]
		# let's jsut look at the first one for now. Is simpler than averaging positions for all occurences.
	# positions = np.array(positions) not really necessary
	with open(out_data, 'w+') as outfile:
		writer = csv.writer(outfile)
		for pos in positions:
			writer.writerow([pos])



if __name__ == '__main__':
	main()