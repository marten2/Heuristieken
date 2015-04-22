def Checklist(CCL, edgeData):
	output = []
	for a in edgeData:
		for b in edgeData[a[0]][1]:
			if CCL[b] == CCL[a[0]]:
				output.append([b, a[0]])

	if output:
		return output
	else:
		return "No errors found"

def checkColors(CCL):
	# count number of colors used
	colors = 0

	for a in CCL:
		if a > colors:
			colors = a

	colors = colors + 1

	return colors