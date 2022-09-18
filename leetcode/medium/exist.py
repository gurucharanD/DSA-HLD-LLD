# 79. Word Search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        
        def helper(row,col,index):
            
            if row < 0 or row >= len(board): return False
            if col < 0 or col >= len(board[0]): return False
            if visited[row][col]: return False
            if board[row][col] != word[index]: return False
            if index == len(word)-1: return True
            
            visited[row][col] = True
            
            # if path is found -> return True
            if helper(row+1,col,index+1) or helper(row-1,col,index+1) or helper(row,col-1,index+1) or helper(row,col+1,index+1):
                return True
            
            # else - unmark the path by marking row and col as False
            # and return False
            visited[row][col] = False
            
            return False

        
        ans = False
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if board[i][j] == word[0]:
                    ans = ans or helper(i,j,0)
                    
        return ans