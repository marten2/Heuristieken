import random
import check
import figuresearch
import socialload
import copy
import loadin
import graph

def hillclimber(iterationNumber, colorNumber, colorList, data):
	'''Performs iteration on the color list'''
	size = len(colorList)

	for i in range(0, iterationNumber):

		# select random country 
		country = random.randint(0, size - 1)

		# make candidate color list
		newColorList = copy.deepcopy(colorList)

		# color country randomly
		newColorList[country] = random.randint(0, colorNumber)

		# check if improved
		verdict = evaluate(colorList, newColorList, data)

		# accept change if improved
		if verdict == True:
			colorList = copy.deepcopy(newColorList)
		
	return colorList

def evaluate(colorList, newColorList, data):
	'''Compares two color lists and determines which gives the least clashes'''

	# check errors for both new and old versions
	output1 = check.Checklist(colorList, data)
	output2 = check.Checklist(newColorList, data)

	if len(output2) <= len(output1):
		return True
	else:
		return False

def annealingMain(data, iterationNumber):
	'''Calls different functions to perform annealing''' 

	print "start"
	#data = socialload.loadData('network1.txt')
	#data = loadin.loadData("USAdata.csv")

	# set clique number as initial color number
 	#figurelist = figuresearch.buildFigures(data)
	colorNumber = 2 #figuresearch.findBiggestClique(figurelist)

	# prepare list
	colorList = [0] * len(data)

	# color graph randomly 
	for i in range (0, len(colorList) - 1):
		colorList[i] = random.randint(0, colorNumber)

	output = check.Checklist(colorList, data)


	# keep iterating as long as there are still errors
	while(len(output) != 0): 

		# try to eliminate errors with iteration
		colorList = hillclimber(iterationNumber, colorNumber, colorList, data)

		# check if there are still errors
		output = check.Checklist(colorList, data)

		# if errors increase color number
		colorNumber = colorNumber + 1

	return colorList 
	#graph.makeGraph(colorList, data)

if __name__ == "__main__":
	annealingMain(10000)