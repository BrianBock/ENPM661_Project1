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

	stringBoard=list(spacelessflatboard) #Convert it to a list
	# print("OG string board:")
	# print(stringBoard)

	i=0
	squareBoard=np.empty([num_cols,num_rows])
	squareBoard = squareBoard.astype('int') 
	for col in range (0,num_cols):
		for row in range(0,num_rows):
			squareBoard[row,col]=int(stringBoard[i])
			i+=1
	# print("Square board is:")
	# #print(squareBoard)
	return squareBoard
	



def square2flat(squareBoard):
	"""This function takes an 8 puzzle board and converts it to a linear string
	"""
	# Orignal board:
	# 1 2 3
	# 4 5 6
	# 7 8 0
	# becomes: 
	# "147258360"

	num_rows=len(squareBoard) #one side of the puzzle
	num_cols=len(squareBoard)
	i=0
	flatboard=""#Create an empty string which will be the single line print out
	for col in range (0,num_cols):
		for row in range(0,num_rows):
			flatboard=flatboard+str(squareBoard[row,col])
			i+=1
	#print("Flatboard is: "+str(flatboard))
	return flatboard




#flat2square("147258360")

