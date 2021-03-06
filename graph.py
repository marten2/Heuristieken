import networkx as nx
import matplotlib.pyplot as plt
import networkx.algorithms.approximation.clique as cq

def makeGraph(countryColorList, edgeData):
	''' Draws a graph of the countries and their borders, 
	gives each country the color determined by algorithm'''
	
	G=nx.Graph()

	# draw node for each data element and give it the corresponding color
	for element in edgeData:
		G.add_node(element[0])

	# draw connections between data elements
	for element in edgeData:
		for edge in element[1]:
			G.add_edge(element[0], edge)

	# draw and show graph	
	nx.draw(G, pos=nx.spring_layout(G), node_color=countryColorList)
	plt.show()

