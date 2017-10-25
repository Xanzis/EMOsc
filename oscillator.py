from matplotlib import pyplot as plt
import numpy as np

class Osc:
	g = 9.8
	nturns = 100
	area = 0.0028
	muzero = 1.25 * 10 ** -6
	br = 1.2 # or this
	d = 0.0254 # length of magnet. For these things, see my notes
	r = 0.011
	coilrad = 0.03

	def __init__(self, ks, ms, zstarts, vstarts, centers, coilr, connectr, timestep):
		self.g = 9.8
		self.ks = np.array(ks, dtype='float64')
		self.ctrs = np.array(centers, dtype='float64')
		self.ms = np.array(ms, dtype='float64')
		self.zs = np.array(zstarts, dtype='float64')
		self.vs = np.array(vstarts, dtype='float64')
		self.coilr = coilr
		self.connectr = connectr
		self.step = timestep
		self.fs = np.zeros((2,))
		self.i = 0
		self.q = 1000 # magnetic charge at poles. No idea what this should be
		self.emfs = np.zeros((2,))
		self.log = False

	def calc_emfs(self):
		part1 = ((Osc.d + self.zs) ** 3 - (Osc.d + self.zs) ** 4)/(Osc.r ** 2 + (Osc.d + self.zs) ** 2) ** 1.5
		part2 = (self.zs ** 3 - self.zs ** 4) / (Osc.r ** 2 + self.zs ** 2) ** 1.5
		part3 = -1 * Osc.nturns * Osc.area * (Osc.br / 2) * (part1 - part2)
#		print "part3: ", part3
		self.emfs = part3 * self.vs
		self.i = -1 * (np.diff(self.emfs) / (self.coilr + self.connectr))
#		print "emfs: ", self.emfs
#		print "i: ", self.i

	def calc_forces(self):
		springforces = (self.ctrs - self.zs) * self.ks
		b = Osc.nturns * (Osc.muzero / (2)) * (Osc.coilrad ** 2 * self.i / (Osc.coilrad ** 2 + self.zs ** 2) ** 1.5)
		bfar = Osc.nturns * (Osc.muzero / (2)) * (Osc.coilrad ** 2 * self.i / (Osc.coilrad ** 2 + (self.zs + Osc.d) ** 2) ** 1.5)
		magforces = b * self.q + bfar * -1 * self.q
		magforces *= [1, -1]
#		print springforces, magforces
		if self.log:
			print "forces due to magnetism: ", magforces
		self.fs = springforces + magforces

	def propagate(self):
		self.calc_emfs()
		self.calc_forces()
		a = self.fs / self.ms
		deltav = a * self.step
		deltaz = self.vs * self.step
		self.vs += deltav
		self.zs += deltaz

def main():
	oscillator = Osc([20, 20], [0.084, 0.084], [0.0, 0.01], [0, 0.1], [0.0325, 0.0325], 2, 0.1, 0.0001)
	record_a = []
	record_b = []
	record_i = []
	for i in range(200000):
		oscillator.propagate()
		oscillator.log = False
		if i % 100 == 0:
			record_a.append(oscillator.zs[0])
			record_b.append(oscillator.zs[1])
			record_i.append(oscillator.i)
		if i % 10000 == 0:
			oscillator.log = True
			print "-----"
			print "positions: ", oscillator.zs
			print "velocities:", oscillator.vs
			print "forces:    ", oscillator.fs
	plt.plot(record_b)
	plt.plot(record_a)
	plt.show()
	plt.plot(record_i)
	plt.show()

if __name__ == "__main__":
	main()


