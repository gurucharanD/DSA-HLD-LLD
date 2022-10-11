# recursive solution => O(2^(w+h)) => as at every position
# we need to make 2 decisions either to go left or up
# and we need atleast (m=n) steps to reach the base case
# and it also takes O(m+n) space, on the stack
# we start at the end of the end [w,d] and move all the way to the up [1,1]
# we are also not saving the intermediate results anywhere, 
# so we end up making same recursive call multiple times

def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
	if width == 1 or height == 1:
		return 1
	
    return numberOfWaysToTraverseGraph(width-1, height) + numberOfWaysToTraverseGraph(width, height-1)


# we can use dynamic porgramming to solve this by saving intermediate results
# runs in O(w*h) time and O(w+h) space``

def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
	matrix = [[0 for _ in range(width+1)] for _ in range(height+1)]
	
	for i in range(1,width+1):
		for j in range(1,height+1):
			if i == 1 or j == 1:
				matrix[j][i] = 1
			else:
				matrix[j][i] = matrix[j-1][i] + matrix[j][i-1]
	
	return matrix[height][width]


# final solution is using a math trick

# using the idea that , to reach the end of the 3 by 4 graph, we need to 
# make, 5 moves.  ( RRRDD ) so if we find the no of permutations for this 
# combination, we find the no of ways the graph can be traversed

# formula = fact(width + height) // ( fact(width)*fact(height) )


def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
	width -= 1
	height -= 1
		
    return fact(width + height) // ( fact(width)*fact(height) )


def fact(n):
	
	result = 1;
	for i in range(2,n+1):
		result *= i
		
	return result;
