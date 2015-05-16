import random
import check
import figuresearch
import socialload
import copy
import graph

def hillclimber(iterationNumber, colorNumber, colorList, data):
	'''Performs iteration on the color list'''

	for i in range(0, iterationNumber):

		# select random country 
		country = random.randint(0, len(colorList) - 1)

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

	if not output2 or not output1:
		return True
	elif len(output2) <= len(output1):
		return True
	else:
		return False

def annealingMain(iterationNumber):
	'''Calls different functions to perform annealing''' 

	data = socialload.loadData('network1.txt')
	
	# set clique number as initial color number
 	figurelist = figuresearch.buildFigures(data)
	colorNumber = figuresearch.findBiggestClique(figurelist)

	# prepare list
	colorList = [0] * len(data)

	# color graph randomly 
	for i in range (0, len(colorList) - 1):
		colorList[i] = random.randint(0, colorNumber)

	output = check.Checklist(colorList, data)


	# keep iterating as long as there are still errors
	while(True): 

		# try to eliminate errors with iteration
		colorList = hillclimber(iterationNumber, colorNumber, colorList, data)

		# check if there are still errors
		output = check.Checklist(colorList, data)

		# stop if correct 
		if not len(output):
			break 

		print colorNumber

		# if errors increase color number
		colorNumber = colorNumber + 1

	print colorNumber
	graph.makeGraph(colorList, data)

if __name__ == "__main__":
	annealingMain(10000)