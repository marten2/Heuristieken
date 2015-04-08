def getLongest(list):
	''' Returns country with most connections '''
	longest = []
	for element in list:
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
	
	''''countryColorList[longest] == colors[0]
	country = edgeData[longest]

	for i in range (0, len(edgeData)):
		for neighbours in country[1]:
			return country'''




