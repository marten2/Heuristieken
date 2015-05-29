import loadin
import lowestcolor
import check 
import socialload
import graph
import randomconnections
import figuresearch
import random
import annealing
import hybrid
import annealing
import degreecolor
import time
import hillclimber

def main(algorithm, network, isMapType):
	'''Calls different functions to color a network'''

	# ----------------------------- Select data type -----------------------------

	# load in data 
	if network is 'random':
	  	totalConnections, tuplesList = randomconnections.randomConnections(20, 0, 190)
	  	data = socialload.loadData(tuplesList)
	elif isMapType is True:
		loadin.loadData(network)
	else:
		socialload.loadData(network)


	# ----------------------------- Select algorithm -----------------------------

 	# color network
 	if algorithm is 'shell':
 		colorList = lowestcolor.shell(data, None)

 		# color islands too
 		for i, a in enumerate(colorList):
			if a == None:
				colorList = lowestcolor.shell(data, i)

 	elif algorithm is 'annealing':
		colorList = annealing.annealingMain(data, 10000)

	elif algorithm is 'hillclimber':
		colorList = hillclimber.hillclimberMain(data, 10000)

	elif algorithm is 'degree':
		colorList = lowestcolor.degree(data)

	elif algorithm is 'hybrid':
		colorList = hybrid.algorithm(data)

	elif algorithm is 'clockwise':
		colorList = lowestcolor.clockwise(data, None)
		# color islands too
 		for i, a in enumerate(colorList):
			if a == None:
				colorList = lowestcolor.clockwise(data, i)


	# check if no errors
	output = check.Checklist(colorList, data)
	print output


	# ----------------------------- Obtain testdata -----------------------------
	
	# Test degree 
 	maximum = len(data[lowestcolor.getLongest(data)][1])
	
	# find biggest clique
 	figurelist = figuresearch.buildFigures(data)
	biggest = figuresearch.findBiggestClique(figurelist)
	colors = check.checkColors(colorList)

	# make graph of colored network
 	graph.makeGraph(colorList, data)

if __name__ == "__main__":
	# measure time
	start_time = time.time()
	
	# run main for specific algorithm
	# provide name of text file or choose random

	main('hybrid', 'random', False)

	print("--- %s seconds ---" % (time.time() - start_time))
