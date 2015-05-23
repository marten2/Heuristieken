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

	#n = random.randint(10, 100)

 	#totalConnections = randomconnections.randomConnections(1000, 10000, 10000)

	# load data
	#data = socialload.loadData('connections.txt')
	totalConnections, tuplesList = randomconnections.randomConnections(10, 100, 100)
 	
 	# load random social data
 	data = socialload.loadData(tuplesList)

	# load map data
 	# data = loadin.loadData("USAdata.csv")

 	sortedData = copy.deepcopy(data)

	# make empty array for storing colors
	countryColorList = [None] * len(data)

	# sort nodes on number of edges 
	sortedData = degreecolor.sortOnEdges(sortedData)
	
	maximum = len(sortedData[0][1])
	#print maximum

	# color all countries 
	for element in sortedData:
		countryNumber = element[0]
		countryColorList = lowestcolor.determineColor(data, countryNumber, countryColorList)

	# print colors
	# print countryColorList

	# check if correct
	output = check.Checklist(countryColorList, data)
	print output

	#figurelist = figuresearch.buildFigures(data)
	#biggest = figuresearch.findBiggestClique(figurelist)
	
	# count number of colors
	colors = check.checkColors(countryColorList)
	print colors

	# make graph of data
	#graph.makeGraph(countryColorList, data)

	# find biggest cluster
	#figurelist = figuresearch.buildFigures(data)
	#biggest = figuresearch.findBiggestClique(figurelist)
	#print biggest

 	return [maximum, colors]

if __name__ == "__main__":
	main()