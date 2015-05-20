import loadin
import check
import random

# INITIAL SOLUTION:random genarate an (correct = with checker) solution, starting with highest amount of collors

# MOVE: change color of last used colored country's

# MEASURE OBJECTIVE: calculate the amount of different colors used and colors used per color

# MAXEVALUATIONS: give the maximum amount of valuations

# load data
data = loadin.loadData("USAdata.csv")
print data

# start for colors used
colorsUsed = len(data)

# Number of different colors used
colorPalet = list(set(range(1,colorsUsed)))


def init_function(data,colorsUsed,colorPalet):

	# make empty array for storing colors
	countryColorList = [None] * len(data) 

	# select every country an give it a color
	for country in data:
		# pick random a color
		color = random.choice(colorPalet)
		colorPalet.remove(color)

		# select all neighbours
		neighbours = data[country[0]][1]
		print neighbours

		# remember borders
		borderColorList = []

		# make list of colors of borders
		for border in neighbours:
			borderColorList.append(countryColorList[border])

		# compare border colors with color of country
		if color not in borderColorList:
			countryColorlist[country] = color
			break
	
	return countryColorList

		

def move_operator(colorPalet):
	# use 1 less color
	colorsUsed -= 1
	


def objective_function():
	# check number of colors used
	return check.checkColors(countryColorList)
	#len(Colorpalet)



def hillclimber(init_function,move_operator,objective_function,max_evaluations):
	''' Evaluates until max evaluations runs out or local minimum is reached  '''

	best = init_function(data,colorsUsed,colorPalet)
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
	    # # break when at local maximum or maximum is reached 
	    # if not move_made:
	    #     break 
	print ('hillclimber finished: num_evaluations=%d, best_score=%f',num_evaluations,best_score)
	return (num_evaluations,best_score,best)

def main():


 	# max evaluations
 	max_evaluations = 500

 	# make empty array for storing colors
	countryColorList = [None] * len(data) 

 	# run hillclimber
 	hillclimber(init_function,move_operator,objective_function,max_evaluations)

if __name__ == "__main__":
	main()
