import copy

def getLongest(edgeData):
	''' Returns country with most connections '''
	longest = 0
	output = 0
	for element in edgeData:
		if len(element[1]) > longest:
			longest = len(element[1])
			output = element[0]
	return output

def determineColor(edgeData, country, colorList):
	''' Returns appropriate color for country, aims for the lowest position possible in color list '''
	temp = edgeData[country]

	color = 0
	borderColorList = []

	# make list of colors of borders
	for border in temp[1]:
		borderColorList.append(colorList[border])

	# compare border colors with color of country
	# change to higher color if colors are the same
	for c in range(len(temp[1]) + 1):
		if c not in borderColorList:
			color = c
			break
	
	# add color of country to list of countries' colors
	colorList[country] = color

	return colorList

def shellSelect(shell, edgeData, colorList):
	''' Returns borders of former shell, for the shell algorithm ''' 
	totalConnections = []

	# sellect all possible connection for next shell
	for e in shell:
		# copy elements not lists
		for a in edgeData[e][1]:
			if a not in totalConnections:
				if not colorList[a]:
					totalConnections.append(a)
	# return the shell
	return totalConnections

def clockwiseShellSelect(shell, edgeData, countryColorList):
	''' Selects borders of former shell ''' 
	temp = []
	totalConnections = []
	sets = []

	# sellect all possible connection for next shell
	for country in shell:
		# copy elements not lists
		for newShellNeighbour in edgeData[country][1]:
			if newShellNeighbour not in temp:
				if not countryColorList[newShellNeighbour]:
					temp.append(newShellNeighbour)
	
	# put connections in clockwise order
	for newCountry in temp:
		sets = [set(edgeData[newCountry][1]), set(temp)]
		sameNeighbours = list(set.intersection(*sets))
		sameNeighboursLength = len(sameNeighbours)

		if sameNeighboursLength <= 0:
			if newCountry not in totalConnections:
					if not countryColorList[newCountry]:
						totalConnections.append(newCountry)
		else:
			for neighbour in sameNeighbours:
				if neighbour not in totalConnections:
					if not countryColorList[neighbour]:
						totalConnections.append(neighbour)
	# return the shell
	return totalConnections

def shell(data, start):
	''' Calls functions to color the map '''
	colorList = [None] * len(data)
	
	if not start:
		start = getLongest(data)
	shell = [start] 

	while(True):

		# determine countries to be colored
		shell = shellSelect(shell, data, colorList)
		
		# exit if done
		if len(shell) == 0:
			# that's all folks
			return colorList

		# color countries in shell
		for country in shell:
			colorList = determineColor(data, country, colorList)

def clockwise(data, start):
	''' Calls functions to color the map '''
	colorList = [None] * len(data)
	
	if not start:
		start = getLongest(data)
	shell = [start] 

	while(True):
		# Clockwise select
		shell = clockwiseShellSelect(shell, data, colorList)
		
		# exit if done
		if len(shell) == 0:
			# that's all folks
			return colorList

		# color countries in shell
		for country in shell:
			colorList = determineColor(data, country, colorList)

def sortOnEdges(edgeData):
	''' Sorts nodes on number of connections, for degree algorithm''' 

	for index in range (1, len(edgeData)):
		position = index
		currentValue = edgeData[index] 

		# use binary sort to sort list of nodes 
		while position > 0 and len(edgeData[position - 1][1]) < len(currentValue[1]):
			temp = edgeData[position]
			edgeData[position] = edgeData[position - 1]
			edgeData[position - 1] = temp
			position = position - 1

	return edgeData

def degree(data):
	sortedData = copy.deepcopy(data)

	# sort nodes on number of edges 
	sortedData = sortOnEdges(sortedData)
	colorList = [None] * len(data)

	for element in sortedData:
		countryNumber = element[0]
		colorList = determineColor(data, countryNumber, colorList)
	return colorList