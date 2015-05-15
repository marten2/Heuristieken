import socialload
import check
import graph
import random
import copy

def buildFigures(edgeData):
	'''Gets all connection figures of the graph'''
	
	# ready an output
	output = []
	
	for element in edgeData:
		# ready cliques per element
		for e in element[1]:
			# build a checklist to check if an element is connected to all elements
			checklist= [element[1], edgeData[e][1]]
			
			# ready clique list
			temp = [element[0], e]

			# build a clique list
			temp = recursivebuild(e, edgeData, checklist, temp)
			
			temp = sorted(temp)
			if temp not in output: 
				# add clique for an element to output
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
	for c in figurelist:
		if len(c) > size:
			size = len(c)
	return size

def colorCLique(clique, CCL):
	for e in clique:
		if CCL[e] == None:
			
			colors = []
			for a in clique: 
				if CCL[a] != None:
					colors.append(CCL[a])
			
			for c in range(len(clique) + 1):
				if c not in colors:
					CCL[e] = c
					break
	return CCL

def cliqueColoring(data, CCL):
	for d in data:
		CCL = colorCLique(d, CCL)

	return CCL

def hillClimber(CCL, data, max_col, max_error):
	i = 0
	size = len(CCL)
	while(i < 10000):
		temp = copy.deepcopy(CCL)
		temp[random.randint(0, size - 1)] = random.randint(0, max_col)
		new_len = len(check.Checklist(temp, data))
		if  new_len <= max_error:
			max_error = new_len
			CCL = temp
		i += 1
	return CCL

def clashColoring(CCL, data, max_col, edgeData):
	changed = []
	for d in data:
		if d[0] not in changed:
			CCL[d[0]] = max_col + 1
			for a in edgeData[d[0]][1]:
				if a not in changed:
					changed.append(a)
		elif d[1] not in changed:
			CCL[d[1]] = max_col + 1
			for a in edgeData[d[1]][1]:
				if a not in changed:
					changed.append(a)
		return CCL


if __name__ == "__main__":
	# data =  buildFigures([[0,[1,2,3]],[1,[0,2,4]],[2,[0,1,4]],[3,[0,4]],[4,[1,2,3]]])
	data = socialload.loadData('network1.txt')
	print data[0][1]
	CCL = [None] * len(data)
	data2 = buildFigures(data)
	data2 = sorted(data2, key=len, reverse=True)
	CCL = cliqueColoring(data2, CCL)
	for i in range(len(CCL)):
		if CCL[i] == None:
			CCL[i] = 0
	CCL = hillClimber(CCL, data, 2, len(check.Checklist(CCL, data)))
	print check.Checklist(CCL, data)
	CCL = clashColoring(CCL, check.Checklist(CCL, data), 2, data)
	print check.Checklist(CCL, data)
	# graph.makeGraph(CCL, data)

