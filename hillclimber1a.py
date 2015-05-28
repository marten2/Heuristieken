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
	
	# remember size of color list
	size = len(colorList)

	# starting amount of errors
	beginEnergy = len(check.Checklist(colorList, data))

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

		# check errors of new version
		neighborEnergy = len(check.Checklist(newColorList, data))

		# accept change if improved, stop hillclimbing if no errors 
		if neighborEnergy == 0:
			colorList = copy.deepcopy(newColorList)
			break
		elif neighborEnergy <= beginEnergy:
			colorList = copy.deepcopy(newColorList)	
			beginEnergy = neighborEnergy

	return colorList

def hillclimberMain(data, iterationNumber):
	'''Calls different functions to perform hillclimber''' 

	colorNumber = 2 

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


	graph.makeGraph(colorList, data)

	return colorList 

if __name__ == "__main__":
	data = socialload.loadData('network1.txt')
	print hillclimberMain(data, 10000)
