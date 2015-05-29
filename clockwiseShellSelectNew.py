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