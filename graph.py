import networkx as nx
import matplotlib.pyplot as plt

# problem with this is that it draws all borders twice 
# and that numpy is not downloaded yet
def makeGraph(countryColorList, edgeData):
	''' Draws a graph of the countries and their borders, 
	gives each country the color determined with the functions
	in modifydata'''
	
	G=nx.Graph()
	i = 0 
	colors = ['r', 'g', 'y', 'b', 'o', 'c']

	for element in edgeData:
		G.add_node(element[0])
		G.node_color = colors[countryColorList[i]]
		
		i = i + 1

	for element in edgeData:
		for edge in element[1]:
			G.add_edge(element[0], edge)


	nx.draw(G)
	plt.draw()
	plt.show()