import loadin
import lowestcolor
import check 
import socialload
# import graph
import randomconnections
#import figuresearch
import random
#import annealing
import degreecolor

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

  	totalConnections, tuplesList = randomconnections.randomConnections(10, 10, 100)
 	# load random social data
 	data = socialload.loadData(tuplesList)

 	# ---------- End Research part -----------

 	# make empty array for storing colors
 	countryColorList = [None] * len(data) 

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
	# check if correct
	output = check.Checklist(countryColorList, data)
	
	colors = check.checkColors(countryColorList)
	# print colors
	# print results 	
	# print "Colors:"
 	print countryColorList
	print "Number of colors used:" + str(colors)	 
 	#figurelist = figuresearch.buildFigures(data)
	#biggest = figuresearch.findBiggestClique(figurelist)
  	# print output

 	#figurelist = figuresearch.buildFigures(data)
	#biggest = figuresearch.findBiggestClique(figurelist)
	#print biggest

 	#graph.makeGraph(countryColorList, data)

 	return [totalConnections, colors]
	# figurelist = figuresearch.buildFigures(data)
	# biggest = figuresearch.findBiggestClique(figurelist)
	# print biggest
 	#graph.makeGraph(countryColorList, data)

if __name__ == "__main__":
	main()