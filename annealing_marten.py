import socialload
import check
import graph
import random
import copy
import math
import time

start_time = time.time()

def anealing(CCL, data, max_col, max_error):
	i = 0
	size = len(CCL)
	T = 10
	g = 0.99994
	while(i < 10000):
		# print i
		temp = copy.deepcopy(CCL)
		temp[random.randint(0, size - 1)] = random.randint(0, max_col)
		new_len = len(check.Checklist(temp, data))
		delta_score = new_len - max_error
		a = delta_score / T
		print a, delta_score, T
		chance = math.exp(-(a))
		# print chance
		T = T * math.pow(g, i)
		evaluate = random.uniform(0, 1)
		if  chance >= evaluate:
			max_error = new_len
			CCL = temp
		i += 1
	return CCL


def algorithm(data, CCL):
	CCL = [0] * len(CCL) 
	for i in range(1, 100):
		CCL = anealing(CCL, data, i, len(check.Checklist(CCL, data)))
		if  len(check.Checklist(CCL, data)) == 0:
			break
		# chaneColoring(CCL, check.Checklist(CCL, data), i, data)
	return CCL

if __name__ == "__main__":
	data = socialload.loadData('network1.txt')
	CCL = [None] * len(data)
	CCL = algorithm(data, CCL) 
	graph.makeGraph(countryColorList, data)
	print("--- %s seconds ---" % (time.time() - start_time))