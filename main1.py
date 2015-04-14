import loadin
import lowestcolor
import check 

# main for lowestcolor algorithm
if __name__ == "__main__":
	# make sure color list has enough colors
 	colors = ["R", "O", "Y", "G", "B", "P", "V"]

 	# load data
 	data = loadin.loadData("IndiaData.csv")

 	# make empty array for storing colors
 	countryColorList = [None] * len(data) 

 	# determine the starting country
 	start = lowestcolor.getLongest(data)

 	# color countries
	countryColorList = lowestcolor.lowestColor(data, start, countryColorList, colors)

	# check if correct
	output = check.Checklist(countryColorList, data)
	
	# print results 	
 	print countryColorList
 	print output