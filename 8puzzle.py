#Brian Bock
#ENPM661 - Perception for Autonomous Robots
#Spring 2020

#import required packages
import numpy as np
import math
from datetime import datetime

#import my packages
from printboard import printboard
from printboard import flatboard
from printboard import flatboard_spaceless
import actions
from verbose import verbose

start = datetime.now()


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
board_tracker=np.empty([total_permutations],dtype='object') #must be type object so we can use python style strings


#for i in range(0,total_permutations,4):
myboard=np.empty(4,dtype='object')

global k
k=0

def findAllPerms(board,k):
	#4 ways to move
	myboard[0]=actions.MoveLeft(board)
	myboard[1]=actions.MoveRight(board)
	myboard[2]=actions.MoveUp(board)
	myboard[3]=actions.MoveDown(board)
	for i in range(0,4):
		verbose("Flatboard is: "+flatboard_spaceless(myboard[i]))
		if(flatboard_spaceless(myboard[i]) in board_tracker): # board configuration is already saved. Move on
			verbose("Board configuration is already saved.")
			#return
		elif(flatboard_spaceless(myboard[i]) == flatboard_spaceless(goal)): #goal found
			print("Goal found!")
			return
		else:
			verbose("Adding board to list")
			board_tracker[k]=flatboard_spaceless(myboard[i]) # board configuration is not saved yet. Save it
			k=k+1
			findAllPerms(myboard[i],k)



findAllPerms(initialboard,k)

print(board_tracker)
print("There are "+str(np.count_nonzero(board_tracker))+" board configurations saved.")

# newBoard=actions.MoveDown(initialboard)

# printboard(newBoard)












end = datetime.now()
runtime=end-start
#runtime=runtime.strftime("%H:%M:%S")
print("Finished in "+str(runtime)+" (hours:min:sec)")




