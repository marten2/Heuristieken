# gets longest list

def getLongest(list):
	''' Returns country with most connections '''
	longest = []
	for element in list:
		if element[1].length > longest:
			longest = element[1].length
	return longest

def makeColor(colorlist, country, color):
	''' Colors a country '''
	colorlist[country] == color
	return countrylist



