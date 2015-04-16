import loadin
import lowestcolor
import check 
import socialload

# main for lowestcolor algorithm
if __name__ == "__main__":
	
 	# load data
 	data = socialload.loadData("network1.txt")
 	print data
 	# data = loadin.loadData("IndiaData.csv")

 	# make empty array for storing colors
 	countryColorList = [None] * len(data) 

 	# determine the starting country
 	start = lowestcolor.getLongest(data)
 	print start

 	# color countries
	countryColorList = lowestcolor.lowestColor(data, start, countryColorList)

	for i, a in enumerate(countryColorList):
		if a == None:
			countryColorList[i] = 1
	# check if correct
	output = check.Checklist(countryColorList, data)
	
	# print results 	
 	print countryColorList
 	print output

 	graph.makeGraph(countryColorList, data)
