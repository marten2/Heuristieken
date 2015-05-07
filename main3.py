import lowestcolor
import degreecolor
import socialload
import check
import graph
import loadin
import copy
import random
import randomconnections
import figuresearch

def main():

	n = random.randint(10, 100)

 	totalConnections = randomconnections.randomConnections(n, 1000, 1000)

	# load data
	data = socialload.loadData('connections.txt')

	# load map data
 	# data = loadin.loadData("IndiaData.csv")

 	sortedData = copy.deepcopy(data)

	# make empty array for storing colors
	countryColorList = [None] * len(data)

	# sort nodes on number of edges 
	sortedData = degreecolor.sortOnEdges(sortedData)

	# color all countries 
	for element in sortedData:
		countryNumber = element[0]
		countryColorList = lowestcolor.determineColor(data, countryNumber, countryColorList)

	# print colors
	# print countryColorList

	# check if correct
	output = check.Checklist(countryColorList, data)
	print output
	
	# count number of colors
	colors = check.checkColors(countryColorList)
	print colors

	# make graph of data
	#graph.makeGraph(countryColorList, data)

	# find biggest cluster
	figurelist = figuresearch.buildFigures(data)
	biggest = figuresearch.findBiggestClique(figurelist)
	print biggest

 	return [biggest, colors]

if __name__ == "__main__":
	main()