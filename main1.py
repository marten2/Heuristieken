import loadin
import lowestcolor
import check 
import socialload
import graph
import randomconnections
import figuresearch
import random
import annealing
import Marten_hillclimber
import annealing
import degreecolor
import time




def main():
	'''Calls different functions for the lowestcolor algorithm'''

 	# load map data
 	# data = loadin.loadData("IndiaData.csv")

 	# load social data
 	# data = socialload.loadData('network1.txt')

	



 	# ---------- Research part -----------

 	# Determine amount of nodes
 	# n = random.randint(1000, 1000)
 	# print n

 	# Determine amount of connections
 	# totalConnections = randomconnections.randomConnections(n, 1000, 10000)

  	totalConnections, tuplesList = randomconnections.randomConnections(20, 0, 190)
 	# load random social data
 	data = socialload.loadData(tuplesList)
<<<<<<< HEAD

	# Test degree 
 	# maximum = len(data[lowestcolor.getLongest(data)][1])
 	# print "Maximum connections:" + str(maximum)

	# Research biggest clique
 	figurelist = figuresearch.buildFigures(data)
	biggest = figuresearch.findBiggestClique(figurelist)

=======
>>>>>>> origin/master

 	# ---------- End Research part -----------

 	# make empty array for storing colors
 	countryColorList = [None] * len(data) 

 	countryColorList = Marten_hillclimber.algorithm(data, countryColorList)
 	# color countries
	# countryColorList = annealing.annealingMain(data, 10000)

	# for i, a in enumerate(countryColorList):
	# 	if a == None:
	# 		countryColorList = lowestcolor.lowestColor(data, i, countryColorList)


 	# maximum = lowestcolor.getLongest(data)
 	# print maximum of connections
 	# print "Maximum connections:" + str(maximum)

 	# sortedData = degreecolor.sortOnEdges(data)

 	# for element in sortedData:
 	# 	countryColorList = lowestcolor.determineColor(data, element[0], countryColorList)

	# for i, a in enumerate(countryColorList):
	# 	if a == None:
	# 		countryColorList = lowestcolor.lowestColor(data)
		#, i, countryColorList	

	# check if correct
	# output = check.Checklist(countryColorList, data)
	
<<<<<<< HEAD
	
	
	# print results 	
	# print "Colors:"
=======
	colors = check.checkColors(countryColorList)	 
 	figurelist = figuresearch.buildFigures(data)
	biggest = figuresearch.findBiggestClique(figurelist)
>>>>>>> origin/master

 	# print output
 	# figurelist = figuresearch.buildFigures(data)
	# biggest = figuresearch.findBiggestClique(figurelist)

<<<<<<< HEAD
 	# print output

 	# Get amount of colors used
	colors = check.checkColors(countryColorList)
	#print colors
=======
>>>>>>> origin/master
 	#graph.makeGraph(countryColorList, data)

 	return [biggest, colors]
	# figurelist = figuresearch.buildFigures(data)
	# biggest = figuresearch.findBiggestClique(figurelist)
	# print biggest
 	# graph.makeGraph(countryColorList, data)


if __name__ == "__main__":
	start_time = time.time()
	main()
	print("--- %s seconds ---" % (time.time() - start_time))
