# program that gets all connections figures, for maps these are tuples, triangles, sqaures
def buildFigures(edgeData):
	output = []
	#print edgeData
	# loop over all data trying to find connection figuures
	for e in edgeData:
		checklist= [e[1]]
		temp = [e[0], []]

		# checklist invelops all the figures of the triangle 

		# look per connection country 		
	return output

def recursivebuild(element, edgeData, temp, checklist):
	for e in element[1]:
		for l in edgeData[e][1]:
			if l not in checklist:
				break
			else:
				checklist.append(edgeData[e][1])

				temp = recursivebuild(edgeData[l])



if __name__ == "__main__":
	print buildFigures([[0,[1,2,3]],[1,[0,2,4]],[2,[0,1,4]],[3,[0,4]],[4,[1,2,3]]])