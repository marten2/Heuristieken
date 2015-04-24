# program that gets all connections figures, for maps these are tuples, triangles, sqaures
def buildFigures(edgeData):
	# ready an output
	output = []
	for element in edgeData:
		
		# ready cliques per element
		temp = [element[0], []]
		for e in element[1]:
			# built a checklist to check if an element is connected to all elements
			checklist= [element[1], edgeData[e][1]]
			
			# ready clique list
			temp2 = [e]

			# build a clique list
			temp2 = recursivebuild(e, edgeData, checklist, temp2)
			
			# add clique for an element to output
			temp[1].append(temp2)
		
		output.append(temp)	
	return output

def recursivebuild(element, edgeData, checklist, temp):
	# loop over all connections of an element checking 
	# if one is connected with the other elements in the clique
	for e in edgeData[element][1]:
		# initialize count
		i = 0

		# count if element is connected by all ellements 
		for check in checklist:
			if e in check:
				i += 1
			# save element if connected to all others in the clique
			if i == len(checklist):
				temp.append(e)
				
				# add connections of the new element to the checklis
				checklist.append(edgeData[e][1])
				
				# start looking from new element
				temp = recursivebuild(e, edgeData, checklist, temp)
	return temp


def findBiggestClique(figurelist):
	'''Gets a list of cliques and returns the size of the biggest one'''	
	size = 0
	for element in figurelist:
		for figure in element[1]:
			if len(figure) > size:
				size = len(figure)
	return size + 1
	



if __name__ == "__main__":
	data =  buildFigures([[0,[1,2,3]],[1,[0,2,4]],[2,[0,1,4]],[3,[0,4]],[4,[1,2,3]]])
