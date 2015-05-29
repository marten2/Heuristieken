import socialload
import check
import graph
import random
import copy


def hillClimber(colorList, data, max_col, max_error):
	''''Implements hillclimber algorithm on data
		optimizing on clashes in colorlist,
		returns optimized colorlist'''
	i = 0
	size = len(colorList)
	while(i < 10000):
		# make copy to save optimal situation
		temp = copy.deepcopy(colorList)

		# select random element to change
		element = random.randint(0, size - 1)
		color = temp[element]

		# change elements color to a random other color
		while(temp[element] == color):
			temp[element] = random.randint(0, max_col)
		
		# get new score 
		new_len = len(check.Checklist(temp, data))
		
		# compare if new situation is better
		if  new_len <= max_error:
			
			# save new sitiuation 
			max_error = new_len
			colorList = temp
			if new_len == 0:
				return colorList
		i += 1
	return colorList

def chaneBuild(shell, data, edgeData, chane, chaned):
	'''Build a chane of elements that are connected from 
	   the errors, data contains the errors'''
	
	new_shell = []
	# select all elements in the previous link to build a new link
	for e in shell:

		# check the connections of those elements and if they
		# are in data(list of errors) and if they are not chaned yet
		for connection in edgeData[e][1]:
			for d in data:
				if connection in d and connection not in chaned:
					new_shell.append(connection)

					# add the new element to the new link
					chaned.append(connection)
	
	# build next link recursively if last link wasn't zero
	if len(new_shell) != 0:
		# add link tot chane
		chane.append(new_shell)
		chane, chaned = chaneBuild(shell, data, edgeData, chane, chaned)
	return chane, chaned

def chaneColoring(colorList, data, max_col, edgeData):
	'''Aply chane algorithm to last clashes in data,
	   data contains the clashes returns colorlist'''
	chanes = []
	chaned = []

	# start building a new chane if element isn't in a chane yet
	for d in data:
		if d[0] not in chaned:
			# start building chane
			chane = [[d[0]]]
			chane, chaned = chaneBuild([d[0]], data, edgeData, chane, chaned)
		
		# add chane to list of chanes
		chanes.append(chane)
	
	# color list of chanes, chane by chane
	for c in chanes:
		for i, a in enumerate(c):
			# color all even links in chane
			if i % 2 == 0:
				for b in a:
					colorList[b] = max_col + 1

	return colorList

def algorithm(data):
	'''Run hybrid algorithm, return color list'''
	colorList = [0] * len(data) 
	for i in range(1, 100):
		colorList = hillClimber(colorList, data, i, len(check.Checklist(colorList, data)))
		if  len(check.Checklist(colorList, data)) == 0:
			break
		chaneColoring(colorList, check.Checklist(colorList, data), i, data)
	return colorList