import matplotlib.pyplot as plt
import numpy as np
from pylab import *

def makePlot(filename):
	
	data = np.genfromtxt(filename, delimiter=",", names=['x', 'y'])
	#data2 = np.genfromtxt('tot_con_vs_col_10000_cycles_1000_nodes_1000_10000_con.csv', delimiter=",", names=['a', 'b'])

	#plt.scatter(data2['a'], data2['b'], c='r', alpha=0.3)
	#m, b = np.polyfit(data['x'], data['y'], 1)
	#x = np.array([0, 20])
	#y = (m*x + b)
	#plt.plot(x, y, "r-")
	plt.scatter(data['x'], data['y'], c='b', alpha=0.1)
	#plt.axis([0, 10, 0, 10])
	plt.text(90, 1.5, "nodes:  10\nedges:  10-100\ngraphs: 1000", bbox={"pad":10, "facecolor": "white", "alpha":0.8})
	plt.xlabel("Total connections")
	plt.ylabel("Total amount of colors used")
	plt.show()

if __name__ == "__main__":

	makePlot('Jenny_hillclimer_degree_corrected.csv')
