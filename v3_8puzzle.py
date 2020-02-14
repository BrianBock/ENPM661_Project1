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
total_permutations=int(math.factorial(height*width))
# print(total_permutations)

# print(board)
# print(goal)



printboard(initialboard) #nodePath should start with the initial configuration

#create a 2D array where the first dimension is a position and the second is a string flatboard like "147258360"

# [board,parent]

# Initial board. 
# while board is not goal:
	# Attempt to move left, up, down, right. 
	# Check if each move is valid (fits on board and hasn't been tried already). Discard if not.
	# Check if new board is goal
	# Add valid new board and parent index to a list


#queue - boards we want to try. Will exhaust itself when we run out of possible moves
#nodes_list - a list of lists. Each 2 element sublist contains the new board and it's parent index
#parent_node = index of the parent board config as stored in nodes_list (index of node_list)
#board_tracker - a set (for speed) of all of the tried boards

board_tracker={}
parent_node=0
#nodes_list=[147258360],[3]
board=square2flat(initialboard.copy())

queue=set()
queue.add(board)


while queue:
	# Add new moves to the queue. The Moves return empty if the move is invalid
	queue.add(actions.MoveLeft(board))
	queue.add(actions.MoveRight(board))
	queue.add(actions.MoveUp(board))
	queue.add(actions.MoveDown(board))

	for newboard in queue:
		#Has it been tried already?
		if(square2flat(newboard) not in board_tracker):
			print("New board")
			board_tracker.add(square2flat(newboard)) #add it to the board_tracker
			node_list.append(board,parent_node)

			#Is it the goal?
			if(square2flat(newboard) is square2flat(goal)):
				print("Goal found!")

		

		# Remove completed moves from the queue
		queue.remove(newboard)
		parent_node+=1







end = datetime.now()
runtime=end-start
#runtime=runtime.strftime("%H:%M:%S")
print("Finished in "+str(runtime)+" (hours:min:sec)")


