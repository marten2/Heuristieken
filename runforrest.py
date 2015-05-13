import main3
#import makeplot
import csv

# make sure the make graph and prints in main1 are turned off before you run this

def run(n):
	''' Runs the lowestcolor algorithm 1000 times and saves the output in a csv file '''

	# open file to write experimental data to
	c = csv.writer(open("experimentaldatasorted.csv", "w"))

	# run main n times
	for i in range(0, n):
		output = main3.main()
		output[0] = str(output[0])
		output[1] = str(output[1])
		c.writerow(output)
run(1000)