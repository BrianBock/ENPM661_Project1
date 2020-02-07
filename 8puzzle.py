#Brian Bock
#ENPM661 - Perception for Autonomous Robots
#Spring 2020

#import required packages
import numpy as np
import matplotlib

# Set up board and goal
height=3
width=height #board must be square
board=np.zeros((width,height))
goal=np.array([[1,2,3],[4,5,6],[7,8,0]])


print(board)
print(goal)

# Create nodePath.txt file, which will house all of the moves we make
nodePathfile=open("nodePath.txt","w+")

def printboard(board):
	# Board gets written to file 
	# 1 2 3
	# 4 5 6
	# 7 8 0
	# becomes: 
	# 1 4 7 2 5 8 3 6 0

