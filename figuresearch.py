# program that gets all connections figures, for maps these are tuples, triangles, sqaures
def buildFigures(edgeData):
	output = []
	# loop over all data trying to find connection figuures
	for e in edgeData:

		# checklist invelops all the figures of the triangle 
		checklist = []
		temp = [e[0], []]
		# look per connection country 
		for a in e[1]:
			checklist.append(e[0])
			print checklist
			temp[1].append(a)
			recursivebuild(temp, a, edgeData, checklist)
			output.append(temp)

	return output

# go through data seeing if a data point is connected to all other data points
def recursivebuild(temp, a, edgeData, checklist):
	
	# loop through connected data points checking if data is connected to other data point in figure. 
	for b in edgeData[a][1]:
		for c in checklist:
			if b not in c:
				break
			else: 
				# add item if connected and check if there are more items in the connection
				temp[1].append(b)
				checklist.append(edgeData[a][1])
				temp = recursivebuild(temp, b, edgeData, checklist)

	return temp