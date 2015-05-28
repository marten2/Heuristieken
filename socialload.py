
def loadData(data):
	'''converts given data set into usable lists of lists with every connection
	   for every country. It takes either a list of tuples or string with a filename'''
	if str(type(data)) == "<type 'str'>":
		data = importData(data) 

	length = getLength(data)
	output = []
	for i in range(length + 1):
		output.append([i,[]])

	for d in data:
		if d[0] != d[1]:
			output[d[0]][1].append(d[1])
			output[d[1]][1].append(d[0])

	return output

def importData(filename):
	'''import data from file, returns a list of tuples'''
	with open(filename, "r") as fin:
			data = []
			for l in fin.readlines():
				temp = l.split(",")
				temp[0] = int(temp[0])
				temp[1] = int(temp[1])
				data.append(temp)
			return data