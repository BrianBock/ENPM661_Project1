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
from plot_path import print_matrix

print("All packages imported properly")

#Record the start time to calculate the run time at the end
start = datetime.now()


# Set up board and goal
height=3
width=height #board must be square
#board=np.zeros((width,height)) #board will be populated later
goal=np.array([[1,2,3],[8,0,4],[7,6,5]])


initialboard=np.array([[2,8,1],[0,4,3],[7,6,5]])

print("Start is: "+str(square2flat(initialboard)))
print("Goal is:  "+str(square2flat(goal)))

#total_permutations=int(math.factorial(height*width))

print("Starting now.")
print("If the puzzle is very difficult or unsolvable, this may take a minute or two.")
print("Please be patient.")
printboard(square2flat(initialboard)) #nodePath should start with the initial configuration


#queue - boards we want to try. Will exhaust itself when we run out of possible moves
#nodes_list - a list of lists. Each 2 element sublist contains the new board and it's parent index
#parent_node = index of the parent board config as stored in nodes_list (index of nodes_list)
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
found_goal=False

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
			#print("Board is: "+str(myboard[b]))
			queue.append(myboard[b])
			board_tracker.add(board) #add it to the board_tracker
			nodes_list.append([board,parent_node])

			#Is it the goal?
			if(myboard[b] == square2flat(goal)):
				print("Goal found!")
				goal_node=len(nodes_list)#-1 #-1 to compensate for 0 index
				
				#Clear everything else so the program stops here
				queue.clear()
				found_goal=True
				break

	parent_node+=1

if found_goal==False:
	print("No solution found :(")

else:
	print("Printing solution to file now...")

	parent_index=nodes_list[goal_node-1][1]
	# print(parent_index)
	# print(nodes_list[parent_index])

	victorypath=[]
	while (parent_index>0):
		k=nodes_list[parent_index][1]
		victorypath.append(nodes_list[k][0])
		parent_index=nodes_list[k][1]

	# Reverse the path so its from start to goal
	victorypath.reverse()
	
	print("Done in "+str(len(victorypath))+" moves! Here's how I got to the goal:")
	print("Start Node:")
	for count, move in enumerate(victorypath):
		#print(move)
		printboard(move)
		if count >0:
			print("Step #"+str(count))
		print_matrix(move)
		print("\n\n")





end = datetime.now()
runtime=end-start
#runtime=runtime.strftime("%H:%M:%S")
print("Finished in "+str(runtime)+" (hours:min:sec)")


