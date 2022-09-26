# 289. Game of Life
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def getNeighbours(r,c,board):
            neighbours = []

            # up
            if r-1 >= 0:
                neighbours.append(board[r-1][c])
            # down
            if r+1<n:
                neighbours.append(board[r+1][c])
            # left
            if c-1 >= 0:
                neighbours.append(board[r][c-1])
            # right                    
            if c+1 < m:
                neighbours.append(board[r][c+1])
            # neg diag                     
            if r+1 < n and c+1 < m:
                neighbours.append(board[r+1][c+1])
            if r-1 >= 0 and c-1 >= 0:
                neighbours.append(board[r-1][c-1])
            # pso diag
            if r-1>=0 and c+1 < m:
                neighbours.append(board[r-1][c+1])
            if r+1<n and c-1 >= 0:
                neighbours.append(board[r+1][c-1])
                
            return neighbours
                
        n = len(board)
        m = len(board[0])
        
        copy = [ [board[r][c] for c in range(m)] for r in range(n)]

        for r in range(n):
            for c in range(m):
                
                currentCell = board[r][c]
                neighbours = getNeighbours(r,c,copy)
                counter = Counter(neighbours)
                
                if currentCell == 1:
                    if counter[1] < 2 or counter[1] > 3:
                        board[r][c] = -1
                else:
                    if counter[1] == 3:
                        board[r][c] = 2
                        
        for r in range(n):
            for c in range(m):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                     board[r][c] = 0
                
        return board



                



                