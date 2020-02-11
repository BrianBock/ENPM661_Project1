import numpy as np
from verbose import verbose

def MoveLeft(board):
	#Moves blank tile left, if possible
	#board=CurrentNode

	num_rows=len(board) #one side of the puzzle
	num_cols=len(board)

	[blank_row,blank_col]=np.where(board==0) #Find the location of the blank space
	
	if(blank_col==0): #Blank spot is on the left edge; cannot be moved left
		verbose("Blank space is at the left edge of the board and cannot be moved left.")
		return board

	else:
		verbose("Moving 1 square to the left")
		newBoard=np.copy(board)
		newBoard[blank_row,blank_col]=board[blank_row,blank_col-1]
		newBoard[blank_row,blank_col-1]=0#board[blank_row,blank_col]
		return newBoard