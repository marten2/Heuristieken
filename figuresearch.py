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
	''''''
	for element in edgeData[element][1]:
		# initialize count
		i = 0

		# count if element is connected by all ellements 
		for check in checklist:
			if element in check:
				i += 1
			# save element if connected to all others in the clique
			if i == len(checklist):
				temp.append(element)
				
				# add connections of the new element to the checklis
				checklist.append(edgeData[element][1])
				
				# start looking from new element
				temp = recursivebuild(element, edgeData, checklist, temp)
	return temp


def findBiggestClique(figurelist):
	'''Gets a list of cliques and returns the size of the biggest one'''	
	size = 0
	for c in figurelist:
		if len(c) > size:
			size = len(c)
	return size
