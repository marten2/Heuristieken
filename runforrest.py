import main1
import main3
import csv

# make sure the make graph and prints in main1 are turned off before you run this

def run(n):
	''' Runs the lowestcolor algorithm 1000 times and saves the output in a csv file '''

	# open file to write experimental data to
<<<<<<< HEAD
	c = csv.writer(open("Marten_Hybrid_degree.csv", "w"))

=======
	c = csv.writer(open("jenny_annealing_connections.csv", "w"))
>>>>>>> fecba0fa9e2037beef1591ce675cfb0ad10e044a

	# run main n times
	for i in range(0, n):
		print i
<<<<<<< HEAD

=======
>>>>>>> fecba0fa9e2037beef1591ce675cfb0ad10e044a
		output = main1.main()
		output[0] = str(output[0])
		output[1] = str(output[1])
		c.writerow(output)
if __name__ == "__main__": 
	run(1000)
