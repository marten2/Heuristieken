def getLongest(edgeData):
	''' Returns country with most connections '''
	longest = 0
	output = 0
	for element in edgeData:
		if len(element[1]) > longest:
			longest = len(element[1])
			output = element[0]
	return output

def determineColor(colors, edgeData, country, countryColorList):
	''' Returns appropriate color for country, aims for the lowest position possible in color list '''
	temp = edgeData[country]

	i = 0
	borderColorList = []

	# make list of colors of borders
	for border in temp[1]:
		borderColorList.append(countryColorList[border])

	# compare border colors with color of country
	# change to higher color if colors are the same
	for border in temp[1]:
		if colors[i] in borderColorList:
			i = i+1
	
	# add color of country to list of countries' colors
	countryColorList[country] = colors[i]

	return countryColorList

def shellSelect(shell, edgeData, countryColorList):
	''' Selects borders of former shell ''' 
	totalConnections = []

	# sellect all possible connection for next shell
	for e in shell:
		# copy elements not lists
		for a in edgeData[e][1]:
			if a not in totalConnections:
				if not countryColorList[a]:
					totalConnections.append(a)

	# return the shell
	return totalConnections

def lowestColor(data, start, countryColorList, colors):
	''' Calls functions to color the map '''
	shell = [start] 

	while(True):

		# determine countries to be colored
		shell = shellSelect(shell, data, countryColorList)
		
		# exit if done
		if len(shell) == 0:
			break

		# color countries in shell
		for country in shell:
			countryColorList = determineColor(colors, data, country, countryColorList)

	# that's all folks
	return countryColorList
