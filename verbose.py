# Conditional print function to toggle verbose output

def verbose(mystring):
	verbose=False #set this to True for more print statements (may be slower)
	if(verbose==True):
		print(mystring)
	else:
		return