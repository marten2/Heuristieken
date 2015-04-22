import matplotlib.pyplot as plt
import numpy as np


def makePlot(filename):
	
	data = np.genfromtxt(filename, delimiter=",", names=['x', 'y'])

	plt.scatter(data['x'], data['y'])
	plt.xlabel("Total amount of connections")
	plt.ylabel("Total amount of colors used")
	plt.show()

makePlot('experimentaldata.csv')