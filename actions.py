import numpy as np

verbose=True #change to True for more print statements (may be slower)

def ActionMoveLeft(CurrentNode):
	board=CurrentNode

	num_rows=len(board) #one side of the puzzle
	num_cols=len(board)

	blankspot=np.where(board==0) #Find the location of the blank space
	blank_row=blankspot[0] #new variables to make it easy to keep track of
	blank_col=blankspot[1]

	print(blankspot)

	if(blankspot[1]==0): #Blank spot is on the left edge; cannot be moved left
		if verbose==True:
			print("Blank space is at the left edge of the board and cannot be moved left.")
		return

	else:
		if verbose==True:
			print("Moving 1 square to the left")
		newBoard=board
		newBoard[blank_row,blank_col]=board[blank_row,blank_col-1]
		newBoard[blank_row,blank_col-1]=0#board[blank_row,blank_col]
		return newBoard