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

#Record the start time to calculate the run time at the end
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


branches=np.empty([total_permutations, total_permutations],dtype='object')
#want an array of lists. Each list contains all of the entries/moves for each branch. 
#the first branch that makes it to the goal is the winner. That branch becomes the victory path
#path is the same in all until fork
#			1) 147208365
#2) Left 		3) Right 		4) Up 			5) Down
# 107248365		147268305		147028365		147280365
# etc
# say left most branch wins
# Victory path=
# 147208365
# 107248365
# ...
# goal

# at each decision, copy previous path and append new board
# board_tracker[i]=board_tracker[i-1].copy() where board_tracker is an array of lists. 
# board_tracker[i].append(board)

# attempt1=[board1, board2, board3, board4....]
# attempt2=[attempt1, boardi]
# attempt3=[attempt2, boardj]

attempt=[]

myboard=np.empty(4,dtype='object')

global k
k=0
attempt=0

def findAllPerms(board,k,attempt):
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
			print(flatboard_spaceless(myboard[i]))
			board_tracker[k]=flatboard_spaceless(myboard[i])
			k=k+1
			return
		else:
			verbose("Adding board to list")
			board_tracker[k]=flatboard_spaceless(myboard[i]) # board configuration is not saved yet. Save it
			k=k+1
			findAllPerms(myboard[i],k)



findAllPerms(initialboard,k)

print(board_tracker)
print("There are "+str(np.count_nonzero(board_tracker))+" board configurations saved.")

goal_pos=np.where(board_tracker==flatboard_spaceless(goal))
print("The goal configuration is the "+str(goal_pos[0])+"th entry. ")

# newBoard=actions.MoveDown(initialboard)

# printboard(newBoard)












end = datetime.now()
runtime=end-start
#runtime=runtime.strftime("%H:%M:%S")
print("Finished in "+str(runtime)+" (hours:min:sec)")




