import clockwiseShellSelectNew

def getLongest(edgeData):
	''' Returns country with most connections '''
	longest = 0
	output = 0
	for element in edgeData:
		if len(element[1]) > longest:
			longest = len(element[1])
			output = element[0]
	return output

def determineColor(edgeData, country, countryColorList):
	''' Returns appropriate color for country, aims for the lowest position possible in color list '''
	temp = edgeData[country]

	color = 0
	borderColorList = []

	# make list of colors of borders
	for border in temp[1]:
		borderColorList.append(countryColorList[border])

	# compare border colors with color of country
	# change to higher color if colors are the same
	for c in range(len(temp[1]) + 1):
		if c not in borderColorList:
			color = c
			break
	
	# add color of country to list of countries' colors
	countryColorList[country] = color

	return countryColorList

def shellSelect(shell, edgeData, countryColorList):
	''' Returns borders of former shell ''' 
	totalConnections = []

	# sellect all possible connection for next shell
	for e in shell:
		# copy elements not lists
		for a in edgeData[e][1]:
			if a not in totalConnections:
				if not countryColorList[a]:
					totalConnections.append(a)
	print totalConnections
	# return the shell
	return totalConnections

def lowestColor(data, countryColorList):
	''' Calls functions to color the map '''
	start = getLongest(data)
	# countryColorList = [None] * len(data)
	shell = [start] 

	while(True):

		# determine countries to be colored
		# shell = shellSelect(shell, data, countryColorList)

		# Clockwise select
		shell = clockwiseShellSelectNew.clockwiseShellSelect(shell, data, countryColorList)
		

		# exit if done
		if len(shell) == 0:
			# that's all folks
			return countryColorList

		# color countries in shell
		for country in shell:
			countryColorList = determineColor(data, country, countryColorList)
