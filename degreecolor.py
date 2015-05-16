def sortOnEdges(edgeData):
	''' Sorts nodes on number of connections ''' 

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
