
import random

# INITIAL SOLUTION:random genarate an (correct = with checker) solution, starting with highest amount of collors

# MOVE: change color of last used colored country's

# MEASURE OBJECTIVE: calculate the amount of different colors used and colors used per color

# MAXEVALUATIONS: give the maximum amount of valuations

def init_function(data, countryColorList):
	'''initiates countryColorList'''
	# select every country an give it a color
	for country in data:
		# number of colors used
		colorsUsed = len(data)

		# list of different colors used
		colorPalet = list(set(range(1,colorsUsed)))
		
		# pick random a color
		color = random.choice(colorPalet)
		colorPalet.remove(color)

		# select all neighbours
		neighbours = data[country[0]][1]

		# remember borders
		borderColorList = []

		# make list of colors of borders
		for border in neighbours:
			borderColorList.append(countryColorList[border])

		# compare border colors with color of country
		if color not in borderColorList:
			countryColorList[country] = color

	
	return countryColorList

def checkColors(countryColorList):
	'''Counts the numbers of colors used'''
	colors = 0

	for a in countryColorList:
		if a > colors:
			colors = a

	# make 1 based
	colors = colors + 1

	return colors
		

def move_operator(countryColorList):
	''' uses 1 color less and only colors country with removed color '''
	colorsUsed = checkColors(countryColorList)

	# use 1 less color
	colorsUsed -= 1

	# select every country an give it a color
	for country in data:
		# number of colors used
		colorsUsed = len(data)

		# list of different colors used
		colorPalet = list(set(range(1,colorsUsed)))
		
		# pick random a color
		color = random.choice(colorPalet)
		colorPalet.remove(color)

		# select all neighbours
		neighbours = data[country[0]][1]

		# remember borders
		borderColorList = []

		# make list of colors of borders
		for border in neighbours:
			borderColorList.append(countryColorList[border])

		# compare border colors with color of country
		if color not in borderColorList:
			countryColorList[country] = color


	return countryColorList
	


def objective_function(countryColorList):
	''' determines how many colors are used '''
	# check number of colors used
	return checkColors(countryColorList)



def hillclimber(init_function,move_operator,objective_function,max_evaluations):
	''' Evaluates until max evaluations runs out or local minimum is reached  '''

	best = init_function(data,countryColorList)
	best_score = objective_function(best)

	num_evaluations=1

	print ('hillclimb started: score=%f',best_score)
    
	while num_evaluations < max_evaluations:
	    # examine moves around our current position
	    move_made = False
	    for next in move_operator(best):
	        if num_evaluations >= max_evaluations:
	            break	
	        
	        # current score comparing to best score
	        next_score=objective_function(next)
	        num_evaluations +=1
	        if next_score < best_score:
	            best=next
	            best_score=next_score
	            move_made = True
	            break
	    # random-restart when at local maximum or maximum is reached 
	    if not move_made:
	        best = init_function(data,countryColorList)
	        best_score = objective_function(best)

	print ('hillclimber finished: num_evaluations=%d, best_score=%f',num_evaluations,best_score)
	return (num_evaluations,best_score,best)


