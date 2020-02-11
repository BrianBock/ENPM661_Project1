import numpy as np
import math

def flat2square(spacelessflatboard):
	#It's easier to work with spaceless strings (spaceless_flatboards) in the main program, 
	#but easier to action (Left, Right, Up, Down) in the array space. This function switches between the two
	# "147258360" becomes
	# 1 2 3
	# 4 5 6
	# 7 8 0

	num_cols=int(math.sqrt(len(spacelessflatboard)))
	num_rows=num_cols #must be square

	stringBoard=list(spacelessflatboard)
	# for q in range(0, len(stringBoard)): 
	# 	stringBoard[q] = int(stringBoard[q]) 
	print(stringBoard)

	i=0
	squareBoard=np.empty([num_cols,num_rows])
	for col in range (0,num_cols):
		for row in range(0,num_rows):
			squareBoard[row,col]=int(stringBoard[i])
			i+=1

	print(squareBoard)

flat2square("147258360")