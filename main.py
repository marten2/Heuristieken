import loadin
import lowestcolor
import shell
import check
import figuresearch

if __name__ == "__main__":
	data = loadin.loadData("IndiaData.csv")
	countryColorList = [None] * len(data) 
	print figuresearch.buildFigures(data)