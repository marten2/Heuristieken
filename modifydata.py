def getLongest(edgeData):
	''' Returns country with most connections '''
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



