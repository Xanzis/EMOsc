import csv
import numpy as np
import sys


def main():
	lookup = sys.argv[1]
	in_data = sys.argv[2]
	out_data = sys.argv[3]
	lookup = np.load(lookup)
	with open(in_data, 'rb') as csvfile:
		reader = csv.reader(csvfile) # content should just be a column of time and one of voltage values
		voltages = []
		times = []
		for row in reader:
			try:
				times += [float(row[0])]
				voltages += [float(row[1])]
			except ValueError:
				pass # this should handle words in cells
		voltages = np.array(voltages, dtype=np.float64)
	positions = []
	for v in voltages:
		positions += [lookup[0, np.argmin(np.abs(lookup[1] - v))]]
		# let's jsut look at the first one for now. Is simpler than averaging positions for all occurences.
	# positions = np.array(positions) not really necessary
	with open(out_data, 'w+') as outfile:
		writer = csv.writer(outfile)
		for i in rangE(len(positions)):
			writer.writerow([times[i], positions[i]])



if __name__ == '__main__':
	main()