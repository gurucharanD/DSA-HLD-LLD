# 2326. Spiral Matrix IV

class Solution(object):
    def spiralMatrix(self, m, n, head):

        result = [[-1] * n for _ in range(m)]
        startRow = 0
        endRow = len(result)-1
        startCol = 0
        endCol = len(result[0])-1

        while startRow <= endRow and startCol <= endCol:

            # fill the first row
            for col in range(startCol,endCol+1):
                if head:
                    result[startRow][col] = head.val
                    head = head.next
            
            # fill the last col
            for row in range(startRow+1,endRow+1):
                if head:    
                    result[row][endCol] = head.val
                    head = head.next

            # fill the last row
            for col in reversed(range(startCol,endCol)):
                if startRow == endRow:
                    break
                
                if head:
                    result[endRow][col] = head.val
                    head = head.next

            # fill the first col
            for row in reversed(range(startRow+1,endRow)):
                if startCol == endCol:
                    break
                
                if head:
                    result[row][startCol] = head.val
                    head = head.next


            startRow+=1
            startCol+=1
            endRow-=1
            endCol-=1

        return result
