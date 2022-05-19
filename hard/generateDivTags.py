def generateDivTags(numberOfTags):
    # Write your code here.
	solution = []
	helper("",numberOfTags,numberOfTags,solution)
    return solution

def helper(prefix,opening,closing,solution):
	head = "<div>"
	tail = "</div>"
	
	if opening > 0:
		helper(prefix+head,opening-1,closing,solution)
	
	if opening < closing:
		helper(prefix+tail,opening,closing-1,solution)
	
	if opening == 0 and closing == 0:
		solution.append(prefix)
		
	

# since this is a combination problem,
# the time complexity of this is going to be a catalina number

# O( (2n)! / n!((n+1)!))

# mostly analysing the time complexity of this kind of problems 
# is not needed in an interview, you can just say that it takes
# lot of time