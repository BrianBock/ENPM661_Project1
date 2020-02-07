#Brian Bock
#ENPM661 - Perception for Autonomous Robots
#Spring 2020

#import required packages
import numpy as np
from printboard import printboard
from printboard import flatboard
from printboard import flatboard_spaceless
import actions
import math


#verbose=True #set this to True for more print statements (may be slower)


# Set up board and goal
height=3
width=height #board must be square
#board=np.zeros((width,height)) #board will be populated later
goal=np.array([[1,2,3],[4,5,6],[7,8,0]])

initialboard=np.array([[1,2,3],[4,5,6],[7,0,8]])
total_permutations=int(math.factorial(height*width))
# print(total_permutations)

# print(board)
# print(goal)



printboard(initialboard) #nodePath should start with the initial configuration

#create a 2D array where the first dimension is a position and the second is a string flatboard like "1 4 7 2 5 8 3 6 0"
board_tracker=np.empty([total_permutations],dtype='object')


#for i in range(0,total_permutations,4):
myboard=np.empty(4)


def findAllPerms(board):
	global k
	k=0
	#4 ways to move
	myboard1=actions.MoveLeft(board)
	print("Flatboard is: "+flatboard_spaceless(myboard1))
	# myboard2=actions.MoveRight(board)
	# myboard3=actions.MoveUp(board)
	# myboard4=actions.MoveDown(board)
	if(flatboard_spaceless(myboard1) in board_tracker): # board configuration is already saved. Move on
		return
	elif(myboard1 is flatboard_spaceless(goal)): #goal found
		print("Goal found!")
	else:
		print("Adding board to list")
		board_tracker[k]=flatboard_spaceless(myboard1) # board configuration is not saved yet. Save it
		k=k+1




findAllPerms(initialboard)

print(board_tracker)

# newBoard=actions.MoveDown(initialboard)

# printboard(newBoard)







