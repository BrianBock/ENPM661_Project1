# Conditional print function to toggle verbose output

verbose=True #set this to True for more print statements (may be slower)
def verbose(mystring):
	if(verbose==True):
		print(mystring)
	else:
		return