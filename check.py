def Checklist(CCL, edgeData):
	output = []
	for a in edgeData:
		for b in edgeData[a[0]][1]:
			if CCL[b] == CCL[a[0]]:
				output.append([b, a[0]])

	if output:
		return "Some errors found:" + output
	else:
		return "Good job!"