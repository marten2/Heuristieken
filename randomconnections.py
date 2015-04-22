import sys 
import random 

def randomConnections():
	'''Outputs a csv file with random connections between nodes 0 to 100'''
	
	# total number of connections is random as well
	totalConnections = random.randint(1000, 100000)
	connectionList = []
	output = open('connections.txt', 'w')

	for i in range(0, totalConnections):
		
		# select two random members to connect
		number1 = random.randint(0, 1000)
		number2 = random.randint(0, 1000)

		# avoid self connection
		while(number1 == number2):
			number2 = (number1 + random.randint(1, 999)) % 1000 

		# write to file
		output.write(str(number1) + "," + str(number2) + "\n")
	# close file
	output.close()
	return totalConnections

randomConnections()
