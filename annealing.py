import random
import check
import figuresearch
import socialload

def randomColor(colorList, colorNumber):
	'''Changes the color of a random node''' 

	country = random.randint(0, len(colorList) - 1)
	colorList[country] = random.randint(0, colorNumber)

	return colorList

def start(data, colorNumber):
	'''Colors the graph randomly with the minimum amount of colors'''

	# make color list 
	colorList = [0] * len(data)
	
	# color nodes in list
	for i in range (0, len(colorList) - 1):
		colorList[i] = random.randint(0, colorNumber)

	return colorList

def iterate(iterationNumber, colorNumber, colorList, data):
	'''Performs iteration on the color list'''

	for i in range(0, iterationNumber):
		# change a color
		newColorList = randomColor(colorList, colorNumber)

		# check if improved
		verdict = evaluate(colorList, newColorList, data)

		# accept change if improved
		if verdict == True:
			colorList = newColorList

		if verdict == False:

	return colorList

def evaluate(colorList, newColorList, data):
	'''Compares two color lists and determines which gives the least clashes'''

	# check errors for both new and old versions
	output1 = check.Checklist(colorList, data)
	output2 = check.Checklist(colorList, data)

	if len(output2) < len(output1):
		return True
	else:
		return False

def annealingMain(iterationNumber):
	'''Calls different functions to perform annealing''' 

	data = socialload.loadData('network1.txt')
	
	# set clique number as initial color number
 	figurelist = figuresearch.buildFigures(data)
	colorNumber = figuresearch.findBiggestClique(figurelist)

	# color graph randomly 
	colorList = start(data, colorNumber)

	output = check.Checklist(colorList, data)

	# keep iterating as long as there are still errors
	while(True): 

		# try to eliminate errors with iteration
		colorList = iterate(iterationNumber, colorNumber, colorList, data)

		# check if there are still errors
		output = check.Checklist(colorList, data)

		# stop if correct 
		if output == "No errors found":
			break 

		print colorNumber

		# if errors increase color number
		colorNumber = colorNumber + 1

	return colorList 

if __name__ == "__main__":
	annealingMain(1000)