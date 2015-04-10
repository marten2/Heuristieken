def ShellSelect(shell, edgeData, countryColorList):
	totalConnections = []
	newShell = []

	# sellect all possible connection for next shell
	for e in shell:
		# copy ellements not lists
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


# kleur van laatste shell niet mee dus nog niet bepaald welke kleur oneven dinges krijgt
# oneven element van vorig shell moet geinsert worden zodat het het eerste van de nieuwe shell is
def ShellColoring(shell, colorSet, countryColorList, edgeData, formercolor):
	'''Colour shell, start is either first element or uneven added element'''
	
	# initialise color switch
	a = 0

	# select color for odd things
	if formercolor == colorSet[0]:
		a = 1

	# start with first element
	temp = shell[0]

	# loop over all elements selecting neighbour elements
	for i in range(len(shell) - 1):
		
		# switch colors
		a = (a + 1) % 2
		countryColorList[temp] = colorSet[a]
		
		# select neighbouring element
		for e in edgeData[temp][1]:
			if e in shell:
				if not countryColorList[e]:
					temp = e
					break
	return countryColorList

# complete algorith to be ran in main
def ShellMain(start, edgeData, countryColorList, colorSets):
	# first shell is ellement with most connections
	shell = [start]
	
	# initialise some values
	odd = 0
	a = 0
	while(True):
		# switch colorsets
		a = (a + 1) % 2

		# sellect new shell
		shell = ShellSelect(shell, edgeData, countryColorList)
		
		# exit if done
		if len(shell) == 0:
			break

		# do shit for odd shells
		if odd != 0:
			shell.insert(0, odd)
		if len(shell) % 2 == 0:
			odd = shell[1]
		else:
			odd = 0

		# color the country
		countryColorList = ShellColoring(shell, colorSets[a], countryColorList, edgeData, "niks")



	# Thats all folks!! 
	return countryColorList