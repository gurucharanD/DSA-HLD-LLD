# bruteforce solution : 
# find sum of all submatirces of size k and return the maximum sum of all
# there are lot of overlaping sums, time would be O(w * h * size^2) 
# size^2 comes from the additional 
# operations that come from performing the addition of all elements in the submatrix
# example: if you have a submatrix of 3 X 3 size, you have 9 elements and 
# you will need 9 addition operations to find the sum which 3 ^ 2
# space is constant O(1)

def maximumSumSubmatrix(matrix, size):
	
	maxSum = float("-inf")
    for i in range(len(matrix) - size + 1):
        for j in range(len(matrix[0]) - size + 1):
            tempsum = 0
			
            for p in range(i, size + i):
                for q in range(j, size + j):
                    tempsum+= matrix[p][q]
			
			if tempsum > maxSum:
				maxSum =tempsum
			
    return maxSum


# using dynamic programming, the complexity could be improved by avoiding the
# repeated addition of the overlaping sub-matrices
# create a 2D matrix called sums of size w*h
# at every index (i,j) , calculate the sum of the submatrix from (0,0) to that (i,j)

# at any point

#  sum[i,j] = sum[i-1,j] + sum[i,j-1] - sum[i-1,j-1] + matrix[i,j]
#  (as the diagonal element will be included twice, we substract it once)
#  the first row and first column of the sums matrix needs to caluculated seperately

# if i = 0
#     sum[i,j] = sum[i,j-1]+matrix[i,j]
# if j = 0
#     sum[i,j] = sum[i-1,j]+matrix[i,j]
# else
#     sum[i,j] = sum[i-1,j] + sum[i,j-1] - sum[i-1,j-1] + matrix[i,j]

# loop through the sums matrix and find the submatrix sums of given size 

# in the sums array 
# if you are finding the sum of the subarray touches left border and top border do nothing`
# if it doesnt touch left border, remove sum from top elements 
# if it doesnt touch top border, remvove sum from left elements
# if it doesnt touch both add diagonal element

def maximumSumSubmatrix(matrix, size):
    # Write your code here.
	sums = [[0 for i in range(len(matrix[0]))] for _ in range(len(matrix))]
	sums[0][0] = matrix[0][0]
	
	for i in range(1,len(matrix[0])):
		sums[0][i] = sums[0][i-1] + matrix[0][i]

	for i in range(1,len(matrix)):
		sums[i][0] = sums[i-1][0] + matrix[i][0]
	
	for i in range(1,len(matrix)):
		for j in range(1,len(matrix[0])):			
			sums[i][j] = sums[i-1][j] + sums[i][j-1] - sums[i-1][j-1] + matrix[i][j]
			
	maxSum = float("-inf")
			
	for row in range(size-1,len(matrix)):
		for col in range(size-1,len(matrix[row])):
			
			total = sums[row][col]
			
			touchesTopBorder = row - size < 0
			
			if not touchesTopBorder:
				total -= sums[row-size][col]
				
			touchesLeftBorder = col - size < 0

			if not touchesLeftBorder:
				total -= sums[row][col-size]
				
			
			touchesTopOrLeftBorder = touchesTopBorder or touchesLeftBorder
			
			if not touchesTopOrLeftBorder:
				total += sums[row-size][col-size]
				
			maxSum = max(total,maxSum)

				
	return maxSum
	
	
				
			
	
	

		
	
	print(sums)
    return -1


