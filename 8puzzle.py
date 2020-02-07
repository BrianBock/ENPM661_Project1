#Brian Bock
#ENPM661 - Perception for Autonomous Robots
#Spring 2020

#import required packages
import numpy as np
from printboard import printboard
import actions


verbose=True #set this to True for more print statements (may be slower)



#Create necessary functions


# Set up board and goal
height=3
width=height #board must be square
board=np.zeros((width,height)) #board will be populated later
goal=np.array([[1,2,3],[4,5,6],[7,8,0]])

initialboard=np.array([[1,2,3],[4,5,6],[7,0,8]])


print(board)
print(goal)



printboard(initialboard)
newBoard=actions.MoveDown(initialboard)

printboard(newBoard)







