import loadin
import lowestcolor
import check 
import socialload
import graph

# main for lowestcolor algorithm
if __name__ == "__main__":
<<<<<<< HEAD
	# make sure color list has enough colors
 	colors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

=======
>>>>>>> 3914295016f6f13bc374c06bbbcec27cc67f5e97
 	# load data
 	data = socialload.loadData("network1.txt")
 	# data = loadin.loadData("IndiaData.csv")

 	# make empty array for storing colors
 	countryColorList = [None] * len(data) 

 	# determine the starting country
 	start = lowestcolor.getLongest(data)

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
