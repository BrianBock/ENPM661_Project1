#Brian Bock
#ENPM661 - Perception for Autonomous Robots
#Spring 2020

#import required packages
import numpy as np
import math
from datetime import datetime
import collections

#import my packages
from printboard import printboard
from printboard import flatboard
#from printboard import flatboard_spaceless
import actions
from verbose import verbose
from board_switcher import flat2square
from board_switcher import square2flat

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


#branches=np.empty([total_permutations, total_permutations],dtype='object')
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


myboard=np.empty(4,dtype='object')

attempt=[[]*10]*10
attempt[0].append("000")
k=0

# for i in range(1,len(attempt)):
# 	attempt[i]=attempt[i-1].copy()
# 	attempt[i].append(str(i)+str(i)+str(i))

def BFS(board,attempt,attempt_num,parent,k):
	myboard[0]=actions.MoveLeft(board)
	myboard[1]=actions.MoveRight(board)
	myboard[2]=actions.MoveUp(board)
	myboard[3]=actions.MoveDown(board)

	for i in range(0,4):
		print(myboard[i])

	for i in range(0,4):
		if(square2flat(myboard[i]) in board_tracker): # board configuration is already saved. Move on
			verbose("Board configuration is already saved.")
			return
		else:
			verbose("Adding board to list")
			board_tracker[k]=square2flat(myboard[i])
			k=k+1
		#print(attempt_num)

			attempt[attempt_num]=attempt[parent].copy()
			attempt[attempt_num].append(square2flat(myboard[i]))
			parent=attempt_num
			attempt_num+=1
			# print(attempt[parent])
			BFS(myboard[i],attempt,attempt_num+i,parent,k)



BFS(initialboard,attempt,0,0,k)
print(attempt)

a=flat2square("123456780")
b=actions.MoveLeft(a)


#print(attempt)
#print(a)
#print(b)















end = datetime.now()
runtime=end-start
#runtime=runtime.strftime("%H:%M:%S")
print("Finished in "+str(runtime)+" (hours:min:sec)")
