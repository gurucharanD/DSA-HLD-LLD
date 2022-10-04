# 59. Spiral Matrix II

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        result = [[0]*n for _ in range(n)]
        
        startRow = startCol = 0
        endRow = endCol = n-1
        i = 1
        
        while startRow <= endRow and startCol <= endCol:
            
            # fill the first row
            for col in range(startCol,endCol+1):
                result[startRow][col] = i
                i+=1
            
            # fill the last col
            for row in range(startRow+1,endRow+1):
                result[row][endCol] = i
                i+=1
                
            # fill the last row in reverse order
            for col in range(endCol-1,startCol-1,-1):
                if startRow == endRow:
                    break
                    
                result[endRow][col] = i
                i+=1
                
            # fill the first col in reverse order            
            for row in range(endRow-1,startRow,-1):
                if startCol == endCol:
                    break
                    
                result[row][startCol] = i
                i+=1
            
            startRow += 1
            endRow -= 1
            startCol += 1
            endCol -= 1
            
        return result