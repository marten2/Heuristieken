def loadData(filename):
	with open(filename, "r") as fin:
		data = []
		for l in fin.readlines():
			temp = l.split(",")
			temp[0] = int(temp[0])
			temp[1] = int(temp[1])
			data.append(temp)

		length = getLength(data)
		output = []
		for i in range(length -1):
			output.append([i,[]])

		for d in data:
			output[d[0]][1].append(d[1])
			output[d[1]][1].append(d[0])

		print output 

def getLength(data):
	high = 0 
	for l in lines:
		for a in l:
			if a > high:
				high = a

	return high