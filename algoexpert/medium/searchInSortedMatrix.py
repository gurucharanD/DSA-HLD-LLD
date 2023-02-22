
# start at the top right corner of the array
# if target is less than the current position move to left column
# eliminating all the elements in the current column
# if target is greater thatn the current position move to next row
# eliminating all the elements in the current row

# at any point, 
# the elements that are greater than
# the current element are towards the 
# right and down of the current element
# the elements that are smaller than
# the current element are towards the
# left and up of the current element


# space is O(1) - no extra space
# time is O(N+M) 
# N - no of rows
# M - no of columns

# the greatest number of iterations come from 
# finding the element at the left corner 
# which is equal to the sum of M+N 
# therefore that is the time complexity
# and it is the maximum


def searchInSortedMatrix(matrix, target):
    # Write your code here.
	row = 0
	col = len(matrix[0])-1
	
	while row < len(matrix) and col >= 0:
		
		if target == matrix[row][col]:
			return [row,col]
		
		if target > matrix[row][col]:
			row+=1
		elif target < matrix[row][col]:
			col-=1

			
		
	return [-1,-1]
