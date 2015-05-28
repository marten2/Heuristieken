def clockwiseShellSelect(shell, edgeData, countryColorList):
	''' Selects borders of former shell ''' 
	totalConnections = []
	sets = []
	neighbour = []

	# sellect all possible connection for next shell
	for country in shell:
		i = 0
		temp = []
		# copy elements not lists
		for neighbour in edgeData[country][1]:
			sets = [set(edgeData[country][1]), set(edgeData[neighbour][1])]
			sameNeighbours = list(set.intersection(*sets))
			sameNeighboursLength = len(sameNeighbours)
			
			# for first neighbour to choose direction
			if i == 0 and sameNeighboursLength != 0:
				if sameNeighbours[0] not in totalConnections:
					if not countryColorList[sameNeighbours[0]]:
						totalConnections.append(sameNeighbours[0])
			# continue with clockwise coloring
			elif i != 0:
				for oneNeighbour in sameNeighbours:
					if oneNeighbour not in totalConnections:
						if not countryColorList[oneNeighbour]:
							totalConnections.append(oneNeighbour)
			# if i = 0 and sameNeighbours[0] is empty
			# else:
			# 	if not countryColorList[neighbour]:
			# 			print i
			# 			totalConnections.append(neighbour)
			i += 1

	# return the shell
	return totalConnections