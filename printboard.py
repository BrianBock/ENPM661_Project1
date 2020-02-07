import numpy as np

verbose=True #change to True for more print statements (may be slower)

# Create nodePath.txt file, which will house all of the moves we make
nodePathfile=open("nodePath.txt","a+") #a+ for append. Be sure to delete the file from previous runs before starting


def printboard(board):
	"""This function takes an 8 puzzle board and writes it to a file
	"""
	# Board gets written to file 
	# 1 2 3
	# 4 5 6
	# 7 8 0
	# becomes: 
	# 1 4 7 2 5 8 3 6 0

	num_rows=len(board) #one side of the puzzle
	num_cols=len(board)
	i=0
	flatboard=np.empty([num_cols*num_rows],int)#Create an empty array which will be the single line print out
	for col in range (0,num_cols):
		for row in range(0,num_rows):
			flatboard[i]=int(board[row,col])
			i+=1

	flatboard_clean=str(flatboard)[1:-1]+"\n" #Clean up the list style brackets and add a line break
	if verbose is True:
		print(flatboard_clean)
	nodePathfile.write(flatboard_clean)
