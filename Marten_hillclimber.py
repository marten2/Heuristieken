import socialload
import check
import graph
import random
import copy


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

def chaneBuild(shell, data, edgeData, chane, chaned):
	new_shell = []
	for e in shell:
		for a in edgeData[e][1]:
			for d in data:
				if a in d and a not in chaned:
					new_shell.append(a)
					chaned.append(a)
	if len(new_shell) != 0:
		chane.append(new_shell)
		chane, chaned = chaneBuild(shell, data, edgeData, chane, chaned)
	return chane, chaned

def chaneColoring(CCL, data, max_col, edgeData):
	'''Gives remaining clashes an extra color'''
	chanes = []
	chaned = []
	for d in data:
		if d[0] not in chaned:
			chane = [[d[0]]]
			chane, chaned = chaneBuild([d[0]], data, edgeData, chane, chaned)
		
		chanes.append(chane)
	
	for c in chanes:
		for i, a in enumerate(c):
			if i % 2 == 0:
				for b in a:
					CCL[b] = max_col + 1

	return CCL

def allgorithm(data, CCL) 
	for i in range(1, 5):
		CCL = hillClimber(CCL, data, i, len(check.Checklist(CCL, data)))
		if  len(check.Checklist(CCL, data)) == 0:
			break

		chaneColoring(CCL, check.Checklist(CCL, data), i, data)
		print i
	print CCL
	graph.makeGraph(CCL, data)