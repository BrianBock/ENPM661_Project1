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

print("All packages imported properly")

#Record the start time to calculate the run time at the end
start = datetime.now()


# Set up board and goal
height=3
width=height #board must be square
#board=np.zeros((width,height)) #board will be populated later
goal=np.array([[1,2,3],[4,5,6],[7,8,0]])


initialboard=np.array([[1,2,3],[4,5,6],[7,0,8]])

print("Start is: "+str(square2flat(initialboard)))
print("Goal is:  "+str(square2flat(goal)))

#total_permutations=int(math.factorial(height*width))


printboard(initialboard) #nodePath should start with the initial configuration


#queue - boards we want to try. Will exhaust itself when we run out of possible moves
#nodes_list - a list of lists. Each 2 element sublist contains the new board and it's parent index
#parent_node = index of the parent board config as stored in nodes_list (index of node_list)
#board_tracker - a set (for speed) of all of the tried boards

board_tracker=set()
parent_node=0
#nodes_list=[147258360],[3]
nodes_list=[]
board=square2flat(initialboard.copy())

queue=collections.deque([])
queue.append(board)
i=0
myboard=np.empty(4,dtype='object')

while queue:
	# Add new moves to the queue. The Moves return empty if the move is invalid
	board=queue.popleft()
	myboard[0]=actions.MoveLeft(board)
	myboard[1]=actions.MoveRight(board)
	myboard[2]=actions.MoveUp(board)
	myboard[3]=actions.MoveDown(board)

	for b in range(0,4):
		# Don't want empty entries and don't want any repeat entries
		if (myboard[b] is not None) and (myboard[b] not in board_tracker):
			#print("b is: "+str(b))
			print("Board is: "+str(myboard[b]))
			queue.append(myboard[b])
			board_tracker.add(board) #add it to the board_tracker
			nodes_list.append([board,parent_node])

			#Is it the goal?
			if(myboard[b] == square2flat(goal)):
				print("Goal found!")

				#Clear everything else so the program stops here
				queue.clear()
				done=True
				break

		parent_node+=1





end = datetime.now()
runtime=end-start
#runtime=runtime.strftime("%H:%M:%S")
print("Finished in "+str(runtime)+" (hours:min:sec)")


