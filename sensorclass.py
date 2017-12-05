import numpy

def sensora(voltage):
	a = 1.83
	b = 0.073
	c = -0.128
	e = 2.48
	f = -5.86
	i = 1.014
	h = -2.4
	g = 0.4
	cm = a + g + c * voltage
	cm += b * e ** (-1 * (voltage + f))
	cm += 1 / (i * voltage + h)
	return cm

def sensorb(voltage):
	a = 1.83
	b = 0.07
	c = -0.152
	e = 2.48
	f = -5.9
	i = 1.01
	h = -2.4
	g = 0.4
	cm = a + g + c * voltage
	cm += b * e ** (-1 * (voltage + f))
	cm += 1 / (i * voltage + h)
	return cm
