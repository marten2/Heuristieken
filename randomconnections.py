import sys 
import random 

def randomConnections():
	'''Outputs a csv file with random connections between nodes 0 to 100'''
	
	# total number of connections is random as well
	totalConnections = random.randint(150, 300)
	connectionList = []
	output = open('connections.txt', 'w')

	for i in range(0, totalConnections):
		
		number1 = random.randint(0, 100)
		number2 = random.randint(0, 100)

		while(number1 == number2):
			number2 = (number1 + random.randint(1, 99)) % 100 

		output.write(str(number1) + "," + str(number2) + "\n")

	output.close()
randomConnections()
