
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rows = numRows
        cols = len(s)
        # print(rows,cols)
        matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        # print(matrix)
        
        row = -1
        col = 0
        index = 0
        
        while index < len(s):
            row+=1
            while row < rows and col<cols and index<len(s):
                print("1",row,col,index,s[index])
                matrix[row][col] = str(s[index])
                index+=1
                row+=1
                
            row-=1
            row-=1
            col+=1
            
            while row >= 0 and col<cols and index<len(s):
                print("2",row,col,index,s[index])
                matrix[row][col] = str(s[index])
                index+=1
                row-=1
                col+=1
                
            row+=1
            col-=1
            
            
        output = ''
        for r in range(0,len(matrix)):
            for c in range(0,len(matrix[r])):
                if matrix[r][c] != 0:
                    output+=matrix[r][c]

        return output
            
        