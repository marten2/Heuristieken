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

if __name__ == "__main__":
	data = socialload.loadData('network1.txt')
	CCL = [0] * len(data)
	for i in range(1, 5):
		CCL = hillClimber(CCL, data, i, len(check.Checklist(CCL, data)))
		if  len(check.Checklist(CCL, data)) == 0:
			break
		print i
	print CCL
	graph.makeGraph(CCL, data)