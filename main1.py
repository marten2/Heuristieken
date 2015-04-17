import loadin
import lowestcolor
import check 
import socialload
import graph

# main for lowestcolor algorithm
if __name__ == "__main__":
<<<<<<< HEAD
 	# load data
 	# data = socialload.loadData("network1.txt")
 	print data
=======

 	# load social data
 	# data = socialload.loadData("network1.txt")

 	# load map data
>>>>>>> 7baab70e69dfad0d25c7ac207b88ae92d909ff01
 	data = loadin.loadData("IndiaData.csv")

 	# make empty array for storing colors
 	countryColorList = [None] * len(data) 

 	# determine the starting country
 	start = lowestcolor.getLongest(data)

 	# print maximum of connections
 	print "Maximum connections:"
 	print len(data[start][1])

 	# color countries
	countryColorList = lowestcolor.lowestColor(data, start, countryColorList)

	for i, a in enumerate(countryColorList):
		if a == None:
			countryColorList[i] = 1
	# check if correct
	output = check.Checklist(countryColorList, data)
	
	# print results 	
	print "Colors:"
 	print countryColorList
 	
 	print output

 	graph.makeGraph(countryColorList, data)
