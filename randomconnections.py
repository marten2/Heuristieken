import sys 
import random 

def randomConnections(nodes, minConnection, maxConnection):
	'''Outputs a csv file with random connections between nodes 0 to n'''
	
	# total number of connections is random as well
	if maxConnection:
		totalConnections = random.randint(minConnection, maxConnection)
	else:
		totalConnections = minConnection

	connectionList = []
	output = []

	for i in range(0, totalConnections):
		
		# select two random nodes to connect
		number1 = random.randint(0, nodes)
		number2 = random.randint(0, nodes)
		# avoid self connection
		while(number1 == number2):
				number2 = (number1 + random.randint(1, nodes - 1)) % nodes 

		# avoid double connections
		while sorted([number1, number2]) in output:
			
			# select two new random nodes to connect			
			number1 = random.randint(0, nodes)
			number2 = random.randint(0, nodes)
			
			# again avoid self connection
			while(number1 == number2):
				number2 = (number1 + random.randint(1, nodes - 1)) % nodes 
			
		# write to file
		output.append(sorted([number1, number2]))
	
	return totalConnections, output

