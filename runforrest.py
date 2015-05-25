import main1
#import main3
import csv

# make sure the make graph and prints in main1 are turned off before you run this

def run(n):
	''' Runs the lowestcolor algorithm 1000 times and saves the output in a csv file '''

	# open file to write experimental data to

<<<<<<< HEAD
	c = csv.writer(open("Marten_hybrid_degree.csv", "w"))
=======
	c = csv.writer(open("jeroen_clockwise_connections.csv", "w"))
>>>>>>> aeac09c6091eb0b2bfc82519efff57be71e15a90

	# run main n times
	for i in range(0, n):
		print i
		output = main1.main()
		output[0] = str(output[0])
		output[1] = str(output[1])
		c.writerow(output)
if __name__ == "__main__": 
	run(1000)
