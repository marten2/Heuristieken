
# takes either list of data or filename and converts in usefll dataset
def loadData(data):
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
	with open(filename, "r") as fin:
			data = []
			for l in fin.readlines():
				temp = l.split(",")
				temp[0] = int(temp[0])
				temp[1] = int(temp[1])
				data.append(temp)
			return data

def getLength(data):
	high = 0 
	for l in data:
		for a in l:
			if a > high:
				high = a
	return high
	
if __name__ == "__main__":
	loadData("network1.txt")