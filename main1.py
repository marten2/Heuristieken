import loadin
import lowestcolor
import check 
import socialload
import graph
import randomconnections
import figuresearch
import random

def main():
	'''Calls different functions for the lowestcolor algorithm'''

 	# load map data
 	#data = loadin.loadData("IndiaData.csv")

 	# load social data
 	#data = socialload.loadData('socialconnections.txt')

 	n = random.randint(10, 100)
 	print n

 	totalConnections = randomconnections.randomConnections(n, 1000, 1000)

 	# load random social data
 	data = socialload.loadData('connections.txt')

 	# make empty array for storing colors
 	countryColorList = [None] * len(data) 

 	# determine the starting country
 	start = lowestcolor.getLongest(data)

 	maximum = len(data[start][1])

 	# print maximum of connections
 	# print "Maximum connections:" + str(maximum)

 	# # color countries
	countryColorList = lowestcolor.lowestColor(data, start, countryColorList)

	for i, a in enumerate(countryColorList):
		if a == None:
			countryColorList[i] = 1
	# check if correct
	output = check.Checklist(countryColorList, data)
	
	colors = check.checkColors(countryColorList)

	# print results 	
	# print "Colors:"
 # 	print countryColorList
	print "Number of colors used:" + str(colors)	 
  	print output

 	figurelist = figuresearch.buildFigures(data)
	biggest = figuresearch.findBiggestClique(figurelist)
	print biggest

 	# graph.makeGraph(countryColorList, data)

 	return [biggest, colors]


if __name__ == "__main__":
	main()