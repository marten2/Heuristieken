import loadin
import lowestcolor
import check 
import socialload
# import graph
import randomconnections
import figuresearch
import random
import annealing
import Marten_hillclimber

def main():
	'''Calls different functions for the lowestcolor algorithm'''

 	# load map data
 	# data = loadin.loadData("USAdata.csv")

 	# load social data
 	#data = socialload.loadData('network1.txt')

 	# n = random.randint(10, 100)
 	# print n

 	# totalConnections = randomconnections.randomConnections(n, 1000, 1000)

  	totalConnections, tuplesList = randomconnections.randomConnections(10, 100, 100)
 	# load random social data
 	data = socialload.loadData(tuplesList)

 	# make empty array for storing colors
 	countryColorList = [None] * len(data) 

 	maximum = len(data[lowestcolor.getLongest(data)][1])
 	print maximum
 	# print "Maximum connections:" + str(maximum)

 	countryColorList = Marten_hillclimber.algorithm(data, countryColorList)
 	# color countries
	# countryColorList = annealing.annealingMain(data, 10000)

	# for i, a in enumerate(countryColorList):
	# 	if a == None:
	# 		countryColorList = lowestcolor.lowestColor(data, i, countryColorList)
	# check if correct
	# output = check.Checklist(countryColorList, data)
	
	colors = check.checkColors(countryColorList)
	# print colors
	# print results 	
	# print "Colors:"
 	# print countryColorList
	# print "Number of colors used:" + str(colors)	 
 	# figurelist = figuresearch.buildFigures(data)
	# biggest = figuresearch.findBiggestClique(figurelist)
  	# print output

 	#figurelist = figuresearch.buildFigures(data)
	#biggest = figuresearch.findBiggestClique(figurelist)
	#print biggest

 	#graph.makeGraph(countryColorList, data)

 	return [maximum, colors]
	# figurelist = figuresearch.buildFigures(data)
	# biggest = figuresearch.findBiggestClique(figurelist)
	# print biggest
 	#graph.makeGraph(countryColorList, data)

if __name__ == "__main__":
	main()