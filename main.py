import loadin
import lowestcolor
import shell

if __name__ == "__main__":
	colorSets = [["G", "Y"],["R", "B"]] 
	data = loadin.loadData("IndiaData.csv")
	countryColorList = [None] * len(data) 
	start = lowestcolor.getLongest(data)
	print start

	countryColorList = shell.ShellMain(start, data, countryColorList, colorSets)
	print countryColorList