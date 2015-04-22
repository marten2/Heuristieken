import main1
#import makeplot
import csv

# make sure the make graph and prints in main1 are turned off before you run this
def run():
	''' Runs the lowestcolor algorithm 1000 times and saves the output in a csv file '''

	# open file to write experimental data to
	c = csv.writer(open("experimentaldata.csv", "w"))

	# run main 1000 times
	for i in range(0, 1000):
		output = main1.main()
		output[0] = str(output[0])
		output[1] = str(output[1])
		c.writerow(output)
run()