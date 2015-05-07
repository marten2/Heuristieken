import matplotlib.pyplot as plt
import numpy as np


def makePlot(filename):
	
	data = np.genfromtxt(filename, delimiter=",", names=['x', 'y'])

	plt.scatter(data['x'], data['y'])
	plt.xlabel("Biggest clique")
	plt.ylabel("Total amount of colors used")
	plt.show()

makePlot('clique_vs_colors_sorted_10_tot_100_nodes_1000_keer.csv')