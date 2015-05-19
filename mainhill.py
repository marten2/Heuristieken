import hillclimber
import loadin

def main():

	# load data
	data = loadin.loadData("USAdata.csv")

	# start for colors used
	colorsUsed = len(data)

	# Number of different colors used
	colorPalet = list(set(range(1,colorsUsed)))

	# make empty array for storing colors
	countryColorList = [[None]] * len(data)
	

	for i, a in enumerate(countryColorList):
		if a == None:
	 		countryColorList = i
	 		
	print countryColorList

 	# max evaluations
 	max_evaluations = 500

 	

 	# run hillclimber
 	hillclimber.hillclimber(hillclimber.init_function,hillclimber.move_operator,hillclimber.objective_function,max_evaluations)

if __name__ == "__main__":
	main()