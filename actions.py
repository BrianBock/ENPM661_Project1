import numpy as np
from verbose import verbose
from board_switcher import flat2square
from board_switcher import square2flat

def MoveLeft(board):
	#Moves blank tile left, if possible
	#Convert to a square array
	board=flat2square(board)

	num_rows=len(board) #one side of the puzzle
	num_cols=len(board)

	[blank_row,blank_col]=np.where(board==0) #Find the location of the blank space
	
	if(blank_col==0): #Blank spot is on the left edge; cannot be moved left
		verbose("Blank space is at the left edge of the board and cannot be moved left.")
		return #board

	else:
		verbose("Moving 1 square to the left")
		newBoard=np.copy(board)
		newBoard[blank_row,blank_col]=board[blank_row,blank_col-1]
		newBoard[blank_row,blank_col-1]=0#board[blank_row,blank_col]
		newBoard=square2flat(newBoard)
		return newBoard






def MoveRight(board):
	#Moves blank tile right, if possible
	#Convert to a square array
	board=flat2square(board)

	num_rows=len(board) #one side of the puzzle
	num_cols=len(board)

	[blank_row,blank_col]=np.where(board==0) #Find the location of the blank space

	if(blank_col==num_cols-1): #Blank spot is on the right edge; cannot be moved right
		if verbose==True:
			print("Blank space is at the right edge of the board and cannot be moved right.")
		return #board

	else:
		verbose("Moving 1 square to the right")
		newBoard=np.copy(board)
		newBoard[blank_row,blank_col]=board[blank_row,blank_col+1]
		newBoard[blank_row,blank_col+1]=0#board[blank_row,blank_col]
		newBoard=square2flat(newBoard)
		return newBoard









def MoveUp(board):
	#Moves blank tile up, if possible
	#Convert to a square array
	board=flat2square(board)

	num_rows=len(board) #one side of the puzzle
	num_cols=len(board)

	[blank_row,blank_col]=np.where(board==0) #Find the location of the blank space


	if(blank_row==0): #Blank spot is on the top edge; cannot be moved up
		verbose("Blank space is at the top edge of the board and cannot be moved up.")
		return #board

	else:
		verbose("Moving 1 square up")
		newBoard=np.copy(board)
		newBoard[blank_row,blank_col]=board[blank_row-1,blank_col]
		newBoard[blank_row-1,blank_col]=0
		newBoard=square2flat(newBoard)
		return newBoard








def MoveDown(board):
	#Moves blank tile down, if possible
	#Convert to a square array
	board=flat2square(board)

	num_rows=len(board) #one side of the puzzle
	num_cols=len(board)

	[blank_row,blank_col]=np.where(board==0) #Find the location of the blank space

	#print(num_rows)
	if(blank_row==num_rows-1): #Blank spot is on the bottom edge; cannot be moved down
		verbose("Blank space is at the bottom edge of the board and cannot be moved down.")
		return #board

	else:
		verbose("Moving 1 square down")
		newBoard=np.copy(board)
		newBoard[blank_row,blank_col]=board[blank_row+1,blank_col]
		newBoard[blank_row+1,blank_col]=0
		newBoard=square2flat(newBoard)
		return newBoard



