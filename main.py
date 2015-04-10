import loadin
import modifydata
import algorithm

if __name__ == "__main__":
	colorSets = [["G", "Y"],["R", "B"]] 
	data = loadin.loadData("IndiaData.csv")
	countryColorList = [None] * len(data) 
	start = modifydata.getLongest(data)
	print start

	#countryColorList = algorithm.ShellMain(start, data, countryColorList, colorSets)
	print countryColorList