import loadin
import lowestcolor
import check 
import socialload
import graph
import randomconnections
import figuresearch
import random
import Marten_hillclimber
import annealing


def main():
	'''Calls different functions for the lowestcolor algorithm'''

 	# load map data

 	# data = loadin.loadData("USAData.csv")

 	# load social data
 	# data = socialload.loadData('network1.txt')

  	totalConnections, tuplesList = randomconnections.randomConnections(10, 10, 100)
 	
 	# load random social data
 	data = socialload.loadData(tuplesList)

 	# make empty array for storing colors
 	#countryColorList = [None] * len(data) 

 	# determine the starting country
 	#start = lowestcolor.getLongest(data)

 	#maximum = len(data[start][1])

 	# print maximum of connections
 	# print "Maximum connections:" + str(maximum)

 	# color countries
	countryColorList = annealing.annealingMain(data, 10000)

	#for i, a in enumerate(countryColorList):
	#	if a == None:
	#		countryColorList = lowestcolor.lowestColor(data, i, countryColorList)
	# check if correct
	
	output = check.Checklist(countryColorList, data)
	
	colors = check.checkColors(countryColorList)

	# print results 	
	# print "Colors:"
 	# print countryColorList
	print "Number of colors used:" + str(colors)	 
  	print output

 	figurelist = figuresearch.buildFigures(data)
	biggest = figuresearch.findBiggestClique(figurelist)
	#print biggest

 	#graph.makeGraph(countryColorList, data)

 	return [biggest, colors]


if __name__ == "__main__":
	main()