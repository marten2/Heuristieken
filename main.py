import loadin
import lowestcolor
import shell
import check
import figuresearch
import socialload

if __name__ == "__main__":
	# data = loadin.loadData("IndiaData.csv")
	data = socialload.loadData('connections.txt')
	countryColorList = [None] * len(data) 
	figurelist = figuresearch.buildFigures(data)
	biggest = figuresearch.findBiggestClique(figurelist)

	print biggest