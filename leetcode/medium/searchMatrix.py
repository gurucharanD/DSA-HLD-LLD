# if you consider the matrix 
# as a sorted array then the
# left will be at 0
# right will be at (n*m-1)
# if pivot_index = (left+right)//2
# then the pivot element will be at
# matrix[pivot_index//cols][pivot_index%cols]

# consider the 2D matrix as a 1D matrix

#     0   1   2
# 0   1   2   3

# 1   4   5   6

# 2   7   8   9

# this can be converted into a 1D matrix like this

# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# when you are considering the low and high from the 1D array to find the mid
# to find the row in which the element falls: divide the mid by no.of columns => mid//cols
# to find the col in whihc the element falls: mod the mid by the no.of columns => mid%cols

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        n = len(matrix)
        m = len(matrix[0])
        l = 0
        r = (n*m)-1
        
        while l<=r:
            
            pivot_index = (l+r)//2
            pivot_element = matrix[pivot_index//m][pivot_index%m]
            
            if pivot_element == target:
                return True
            
            if pivot_element < target:
                l = pivot_index+1
            else:
                r = pivot_index-1
        
        return False

# identify the row in which the target element may fall under using binary search 
# then do another binary search on the row that we identified 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)-1
        cols = len(matrix[0])-1

        low = 0
        top = rows

        while low <= top:
            row = (low+top)//2
            if matrix[row][0] <= target <= matrix[row][-1]:
                break
            elif target < matrix[row][0]:
                top = row-1
            elif target > matrix[row][-1]:
                low = row+1
        
        if top < low:
            return False
        
        row = (low+top)//2
        
        left = 0
        right = cols
        while left <= right:
            mid = (left+right)//2
            if matrix[row][mid] == target:
                return True
            
            if target > matrix[row][mid]:
                left = mid+1
            else:
                right = mid-1
        
        return False
        