import networkx as nx
import matplotlib.pyplot as plt

# problem with this is that it draws all borders twice 
# and that matplotlib is not downloaded yet
def makeGraph(countryColorList, edgeData):
	''' Draws a graph of the countries and their borders, 
	gives each country the color determined with the functions
	in modifydata'''
	
	G=nx.Graph()
	i = 0 

	for element in edgeData:
		G.add_node(element[0])
		node_color = countryColorList[i]
		i++

	for element in edgeData:
		for edge in element[1]:
			G.add_edge(element[0], edge)

	print("Nodes of graph: ")
	print(G.nodes())
	print("Edges of graph: ")
	print(G.edges())
	
	nx.draw(G)