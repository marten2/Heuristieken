import csv

def loadData(filename):
	'''Loads map data'''

	output = []
	with open(filename, "r") as fin:
		data = fin.readlines()[1:]
		for i, d in enumerate(data):
			# data separation on semicolon
			land = d.split(";")[1:]
			temp = []
			for j, a  in enumerate(land):
				if int(a) == 1:
					temp.append(j)

			output.append([i, temp])
	return output

if __name__ == "__main__":
	loadData("IndiaData.csv")