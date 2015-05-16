def Checklist(CCL, edgeData):
	'''Checks if there are any collisions in colors''' 
	output = []

	# loop through all nodes and their edges
	for a in edgeData:
		for b in edgeData[a[0]][1]:
			if CCL[b] == CCL[a[0]]:
				if output.count(sorted([b, a[0]])) == 0:
					output.append(sorted([b, a[0]]))

	# return errors if there are any
	if output:
		return output

def checkColors(CCL):
	'''Counts the numbers of colors used'''
	colors = 0

	for a in CCL:
		if a > colors:
			colors = a

	# make 1 based
	colors = colors + 1

	return colors