import loadin
import lowestcolor
import check 
import socialload
# import graph
import randomconnections
#import figuresearch
import random
<<<<<<< HEAD
import annealing
import Marten_hillclimber
=======
#import annealing
import degreecolor
>>>>>>> aeac09c6091eb0b2bfc82519efff57be71e15a90

def main():
	'''Calls different functions for the lowestcolor algorithm'''

 	# load map data
 	# data = loadin.loadData("USAdata.csv")

 	# load social data
 	#data = socialload.loadData('network1.txt')

 	# ---------- Research part -----------

 	# Determine amount of nodes
 	# n = random.randint(1000, 1000)
 	# print n

 	# Determine amount of connections
 	# totalConnections = randomconnections.randomConnections(n, 1000, 10000)

  	totalConnections, tuplesList = randomconnections.randomConnections(10, 100, 100)
 	# load random social data
 	data = socialload.loadData(tuplesList)

 	# ---------- End Research part -----------

 	# make empty array for storing colors
 	countryColorList = [None] * len(data) 

<<<<<<< HEAD
 	maximum = len(data[lowestcolor.getLongest(data)][1])
 	print maximum
 	# print "Maximum connections:" + str(maximum)

 	countryColorList = Marten_hillclimber.algorithm(data, countryColorList)
 	# color countries
	# countryColorList = annealing.annealingMain(data, 10000)

	# for i, a in enumerate(countryColorList):
	# 	if a == None:
	# 		countryColorList = lowestcolor.lowestColor(data, i, countryColorList)
=======
 	maximum = lowestcolor.getLongest(data)
 	# print maximum of connections
 	# print "Maximum connections:" + str(maximum)

 	# sortedData = degreecolor.sortOnEdges(data)

 	#for element in sortedData:
 		#countryColorList = lowestcolor.determineColor(data, element, countryColorList)
 	# color countries
	# countryColorList = annealing.annealingMain(data, 10000)

	for i, a in enumerate(countryColorList):
		if a == None:
			countryColorList = lowestcolor.lowestColor(data)
		#, i, countryColorList	
>>>>>>> aeac09c6091eb0b2bfc82519efff57be71e15a90
	# check if correct
	output = check.Checklist(countryColorList, data)
	
	colors = check.checkColors(countryColorList)
	# print colors
	# print results 	
	# print "Colors:"
<<<<<<< HEAD
 	# print countryColorList
	# print "Number of colors used:" + str(colors)	 
 	# figurelist = figuresearch.buildFigures(data)
	# biggest = figuresearch.findBiggestClique(figurelist)
=======
 	print countryColorList
	print "Number of colors used:" + str(colors)	 
 	#figurelist = figuresearch.buildFigures(data)
	#biggest = figuresearch.findBiggestClique(figurelist)
>>>>>>> aeac09c6091eb0b2bfc82519efff57be71e15a90
  	# print output

 	#figurelist = figuresearch.buildFigures(data)
	#biggest = figuresearch.findBiggestClique(figurelist)
	#print biggest

 	#graph.makeGraph(countryColorList, data)

<<<<<<< HEAD
 	return [maximum, colors]
=======
 	return [totalConnections, colors]
>>>>>>> aeac09c6091eb0b2bfc82519efff57be71e15a90
	# figurelist = figuresearch.buildFigures(data)
	# biggest = figuresearch.findBiggestClique(figurelist)
	# print biggest
 	#graph.makeGraph(countryColorList, data)

if __name__ == "__main__":
	main()