import matplotlib.pyplot as plt
import numpy as np
from pylab import *

def makePlot(filename):
	
	data = np.genfromtxt(filename, delimiter=",", names=['x', 'y'])
	#data2 = np.genfromtxt('tot_con_vs_col_10000_cycles_1000_nodes_1000_10000_con.csv', delimiter=",", names=['a', 'b'])

	#plt.scatter(data2['a'], data2['b'], c='r', alpha=0.3)
	plt.scatter(data['x'], data['y'], c='b', alpha=0.1)
	m,b = polyfit(data['x'], data['y'], 1)
	plt.xlabel("Biggest clique")
	plt.ylabel("Total amount of colors used")
	plt.show()

makePlot('jenny_hillclimber_clique1.csv')