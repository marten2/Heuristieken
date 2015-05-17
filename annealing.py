import random
import check
import figuresearch
import socialload
import copy
import loadin
import graph
import math 

 
def hillclimber(iterationNumber, colorNumber, colorList, data, temperature):
	'''Performs iteration on the color list'''
	size = len(colorList)
	frac = 0.5

	for i in range(0, iterationNumber):

		# select random country 
		country = random.randint(0, size - 1)

		# make candidate color list
		newColorList = copy.deepcopy(colorList)

		# color country randomly
		newColorList[country] = random.randint(0, colorNumber)

		# update temperature
		temperature = temperature * frac

		# check if improved
		verdict = evaluate(colorList, newColorList, data, temperature)

		# accept change if improved
		if verdict == True:
			colorList = copy.deepcopy(newColorList)
		
	return colorList

def evaluate(colorList, newColorList, data, temperature):
	'''Compares two color lists and determines which gives the least clashes'''

	boltzmann = 1.3806488 * 10^-23

	# check errors for both new and old versions
	beginEnergy = len(check.Checklist(colorList, data))
	neighborEnergy = len(check.Checklist(newColorList, data))
	
	# calculate energy 
	energy = math.exp(-(beginEnergy - neighborEnergy) / (temperature * boltzmann))
	print energy

	compare = random.randint(0, 1)

	# decide if change is accepted
	if compare < energy:
		return True
	else:
		return False

def annealingMain(data, iterationNumber):
	'''Calls different functions to perform annealing''' 

	#data = loadin.loadData("USAdata.csv")

	# set clique number as initial color number
 	#figurelist = figuresearch.buildFigures(data)
	colorNumber = 2 #figuresearch.findBiggestClique(figurelist)

	# prepare list
	colorList = [0] * len(data)

	# set temperature
	temperature = 1000

	# color graph randomly 
	for i in range (0, len(colorList) - 1):
		colorList[i] = random.randint(0, colorNumber)

	output = check.Checklist(colorList, data)


	# keep iterating as long as there are still errors
	while(len(output) != 0): 

		# try to eliminate errors with iteration
		colorList, temperature = hillclimber(iterationNumber, colorNumber, colorList, data, temperature)

		# check if there are still errors
		output = check.Checklist(colorList, data)

		# if errors increase color number
		colorNumber = colorNumber + 1

	return colorList 
	#graph.makeGraph(colorList, data)

if __name__ == "__main__":
	data = socialload.loadData('network1.txt')
	annealingMain(data, 10000)