import sys 
import random 

def randomConnections(nodes, minConnection, maxConnection):
	'''Outputs a csv file with random connections between nodes 0 to 100'''
	
	# total number of connections is random as well
	if maxConnection:
		totalConnections = random.randint(minConnection, maxConnection)
	else:
		totalConnections = minConnection

	connectionList = []
	output = open('connections.txt', 'w')

	for i in range(0, totalConnections):
		
		# select two random members to connect
		number1 = random.randint(0, nodes)
		number2 = random.randint(0, nodes)

		# avoid self connection
		while(number1 == number2):
			number2 = (number1 + random.randint(1, nodes - 1)) % nodes 

		# write to file
		output.write(str(number1) + "," + str(number2) + "\n")
	# close file
	output.close()
	return totalConnections

