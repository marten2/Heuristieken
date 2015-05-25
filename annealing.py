import random
import check
import figuresearch
import socialload
import copy
import loadin
import graph
import math 
 
def hillclimber(iterationNumber, colorNumber, colorList, data):
	'''Performs iteration on the color list'''
	size = len(colorList)
	frac = 0.9994
	minTemp = 0.1
	temperature = 10

	for i in range(0, iterationNumber):

		# select random country 
		country = random.randint(0, size - 1)

		# make candidate color list
		newColorList = copy.deepcopy(colorList)

		# determine color
		color = random.randint(0, colorNumber)

		# make sure a different color is chosen
		while color == colorList[country]:
			color = random.randint(0, colorNumber)

		# color country 
		newColorList[country] = color

		# update temperature while bigger than 1
		if temperature > minTemp:
			temperature = temperature * frac

		# check if improved
		verdict = evaluate(colorList, newColorList, data, temperature)

		# accept change if improved, stop hillclimbing if no errors 
		if verdict == 2:
			break
		elif verdict == 1:
			colorList = copy.deepcopy(newColorList)

	return colorList

def evaluate(colorList, newColorList, data, temperature):
	'''Compares two color lists and determines which gives the least clashes'''

	# check errors for both new and old versions
	beginEnergy = len(check.Checklist(colorList, data))
	neighborEnergy = len(check.Checklist(newColorList, data))

	# stop hillclimber if there are no errors
	if beginEnergy == 0:
		return 2
	
	if neighborEnergy <= beginEnergy:
		return 1
	else:
		return 0

	# calculate chance 
	#chance = math.exp(-(neighborEnergy - beginEnergy) / temperature)

	# generate number to compare with
	#compare = random.uniform(0.0, 1.0)

	# decide if change is accepted
	#if compare <= chance:
	#	return 1
	#else:
	#	return 0

def annealingMain(data, iterationNumber):
	'''Calls different functions to perform annealing''' 

	# set clique number as initial color number
 	#figurelist = figuresearch.buildFigures(data)
 	#biggest = figuresearch.findBiggestClique(figurelist)

	colorNumber = 2 

	# prepare list
	colorList = [0] * len(data)

	# set temperature
	temperature = 10

	# color graph randomly 
	for i in range (0, len(colorList) - 1):
		colorList[i] = random.randint(0, colorNumber)

	output = check.Checklist(colorList, data)

	# keep iterating as long as there are still errors
	while(len(output) != 0): 
		# try to eliminate errors with iteration
		#colorList, temperature 
		colorList = hillclimber(iterationNumber, colorNumber, colorList, data)

		# check if there are still errors
		output = check.Checklist(colorList, data)

		# if errors increase color number
		colorNumber = colorNumber + 1

	print colorNumber
	#graph.makeGraph(colorList, data)

	return colorList 

if __name__ == "__main__":
	data = socialload.loadData('network1.txt')
	annealingMain(data, 10000)
