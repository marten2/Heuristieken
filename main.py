import loadin
import lowestcolor
import shell
import check

if __name__ == "__main__":
	colorSets = [["G", "Y"],["R", "B"]] 
	data = loadin.loadData("IndiaData.csv")
	countryColorList = [None] * len(data) 
	start = lowestcolor.getLongest(data)
	countryColorList = shell.ShellMain(start, data, countryColorList, colorSets)

		# check if correct
	output = check.Checklist(countryColorList, data)
	# print results 	
 	print countryColorList
 	print output