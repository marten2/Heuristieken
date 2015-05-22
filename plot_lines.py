import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as pt
import string

def makePlot(filename):
	
	#data2 = np.genfromtxt('tot_con_vs_col_10000_cycles_1000_nodes_1000_10000_con.csv', delimiter=",", names=['a', 'b'])

	#plt.scatter(data2['a'], data2['b'], c='r', alpha=0.3)
	colors = ["r", "g", "m", "k", "c"]
	patch = [None] * len(colors)
	for i, name in enumerate(filename):
		data = np.genfromtxt(name, delimiter=",", names=['x', 'y'])
		name_graph = name.split("_")[1]
		m, b = np.polyfit(data['x'], data['y'], 1)
		x = np.array([0, 110])
		y = (m*x + b)
		plt.plot(x, y, colors[i] + "-")
		patch[i] = pt.Patch(color = colors[i], label = name_graph)
		
	plt.legend(handles=patch, loc=4)
	plt.axis([0, 10, 0, 11])
	plt.xlabel("Biggest clique")
	plt.ylabel("Total amount of colors used")
	plt.show()


if __name__ == "__main__":

	makePlot(['Marten_hybrid_biggestClique.csv', 'jenny_hillclimber_clique1.csv', 'jenny_annealing_clique.csv', 'jenny_degree_clique1.csv', "jenny_lowestcolor_clique.csv"])