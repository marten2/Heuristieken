import loadin
import lowestcolor
import shell
import check
import figuresearch
import socialload

if __name__ == "__main__":
<<<<<<< Updated upstream
	# data = loadin.loadData("IndiaData.csv")
	data = socialload.loadData('connections.txt')
=======
	colorSets = [["G", "Y"],["R", "B"]] 
	data = loadin.loadData("USAdata.csv")
>>>>>>> Stashed changes
	countryColorList = [None] * len(data) 
	figurelist = figuresearch.buildFigures(data)
	biggest = figuresearch.findBiggestClique(figurelist)

	print biggest