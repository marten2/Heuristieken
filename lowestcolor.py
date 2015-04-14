def getLongest(edgeData):
	''' Returns country with most connections '''
<<<<<<< HEAD
	longest = []
	for element in edgeData:
		if element[1].length > longest:
			longest = element[1].length
	return longest

def makeColor(countryColorList, country, color):
	''' Colors a country '''
	countryColorList[country] == color
	return countryColorList

# colors = [blue, red, yellow, green]
def determineColor(colors, edgeData, country, countryColorList):
	''' Returns appropriate color for country '''
	temp = edgeData[country]
	i = 0
	for border in temp[1]:
		if countryColorList[border] == colors[i]:
			i++
	print colors[i]
	return colors[i]

def selectCountry(edgeData, longest, countryColorList):
''' Returns right country to be colored, using a breadth-first algorithm '''
	
	'''countryColorList[longest] == colors[0]
	country = edgeData[longest] 

	for i in range (0, len(edgeData)):
		for neighbours in country[1]:
			return country'''
=======
	longest = 0
	output = 0
	for element in edgeData:
		if len(element[1]) > longest:
			longest = len(element[1])
			output = element[0]
	print longest
	print output
	return output

# def makeColor(countryColorList, country, color):
# 	''' Colors a country '''
# 	countryColorList[country] = color
# 	return countryColorList

# # colors = [blue, red, yellow, green]
# def determineColor(colors, edgeData, country, countryColorList):
# 	''' Returns appropriate color for country '''
# 	temp = edgeData[country]
# 	i = 0
# 	for border in temp[1]:
# 		if countryColorList[border] == colors[i]:
# 			i++
# 	print colors[i]
# 	return colors[i]


def ShellSelect(shell, edgeData, countryColorList):
	totalConnections = []
	newShell = []

	# sellect all possible connection for next shell
	for e in shell:
		# copy elements not lists
		for a in edgeData[e][1]:
			if not countryColorList[a]:
				totalConnections.append(a)

	# filter all connection to only get next shell
	for e in totalConnections:
		for a in edgeData[e][1]:
			if a not in totalConnections:
				newShell.append(e)

	# return the shell
	return newShell
