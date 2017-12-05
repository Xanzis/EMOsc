import sensorclass as sc
import numpy as np
import sys
import csv

def main(in_data, out_data, sensor_name):
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
	func = eval("sc.sensor" + sensor_name)
	print func
	for v in voltages:
		positions += [func(v)]
		# let's jsut look at the first one for now. Is simpler than averaging positions for all occurences.
	# positions = np.array(positions) not really necessary
	with open(out_data, 'w+') as outfile:
		writer = csv.writer(outfile)
		for i in range(len(positions)):
			writer.writerow([times[i], positions[i]])

if __name__ == "__main__":
	main(sys.argv[1], sys.argv[2], sys.argv[3])