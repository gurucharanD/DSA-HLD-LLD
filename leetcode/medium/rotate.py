# 48. Rotate Image
# we transpose the matrix i.e swap matrix[i][j] with matrix[j][i]
# and reverse all the arrays inside the transposed matrix
# and return the reversed array

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        m = len(matrix[0])
        
        for i in range(0,n):
            # we loop only from 0 to i, to avoid double swapping
            for j in range(0,i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
                
        
        for i in range(n):
            matrix[i] = matrix[i][::-1]
            
        return matrix
        
        