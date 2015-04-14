import loadin
import lowestcolor
import shell

# main for lowestcolor algorithm
if __name__ == "__main__":
 	colors = ["G", "Y", "R", "B"]
 	data = loadin.loadData("IndiaData.csv")
 	countryColorList = [None] * len(data) 
 	start = lowestcolor.getLongest(data)

	countryColorList = lowestcolor.LowestColor(data, start, countryColorList, colors)
 	print countryColorList