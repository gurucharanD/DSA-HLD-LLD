# if you consider the matrix 
# as a sorted array then the
# left will be at 0
# right will be at (n*m-1)
# if pivot_index = (left+right)//2
# then the pivot element will be at
# matrix[pivot_index//cols][pivot_index%cols]



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