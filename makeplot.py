import matplotlib.pyplot as plt
import numpy as np


def makePlot(filename):
	
	data = np.genfromtxt(filename, delimiter=",", names=['x', 'y'])

	plt.scatter(data['x'], data['y'])
	plt.xlabel("Total amount of connections")
	plt.ylabel("Total amount of colors used")
	plt.show()

makePlot('tot_con_vs_col_10000_cycles_1000_nodes_1000_10000_con.csv')