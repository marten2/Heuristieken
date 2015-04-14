def getLongest(edgeData):
	''' Returns country with most connections '''
	longest = 0
	output = 0
	for element in edgeData:
		if len(element[1]) > longest:
			longest = len(element[1])
			output = element[0]
	print output
	return output

# colors = [blue, red, yellow, green]
def determineColor(colors, edgeData, country, countryColorList):
	''' Returns appropriate color for country '''
	temp = edgeData[country]
	i = 0
	for border in temp[1]:
		if countryColorList[border] == colors[i]:
			i = i+1
	
	countryColorList[country] == colors[i]
	return countryColorList

def ShellSelect(shell, edgeData, countryColorList):
	totalConnections = []

	# sellect all possible connection for next shell
	for e in shell:
		# copy elements not lists
		for a in edgeData[e][1]:
			if not countryColorList[a]:
				totalConnections.append(a)

	# return the shell
	return totalConnections

def LowestColor(data, start, countryColorList, colors):

	shell = [start] 

	while(True):
		
		# determine countries to be colored
		totalConnections = ShellSelect(shell, data, countryColorList)
		
		# exit if done
		if len(shell) == 0:
			break

		for country in totalConnections:
			countryColorList = determineColor(colors, data, country, countryColorList)

		return countryColorList
