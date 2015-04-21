def buildFigures(edgeData):
	output = []
	checklist = []
	for e in edgeData:
		for a in e[1]:
			checklist.append(e[1])
			temp = [e[0],[a]]
			recursivebuild(temp, a, edgeData, checklist)
			output.append(temp)

	return output
def recursivebuild(temp, a, edgeData, checklist):
	for b in edgeData[a][1]:
		for c in checklist:
			if b not in c:
				break
			temp[1].append(b)
			checklist.append(edgeData[a][1])
			temp = recursivebuild(temp, b, edgeData, checklist)

	return temp