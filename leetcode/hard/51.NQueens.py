# place each Queen in each row and keep going forward
# add the visited columns, positive and negative diagonals into`
# the sets, the positive diagional is identified by ROW + COL 
# the negative diagonal is identifed by ROW - COL

# if these values are in any of the sets do nothing
# else insert the values of col, positiveDiagonal and negativeDiagonal
# into the corresponding sets and place the Queen in the Cell
# continue to next row by invoking the 
# same function recursively on ROW + 1
# if solution is not found , we back track and change the columns
# by removing the values from the corresponding sets and removing the 
# queen from the cell

# n! complexity and n^2 space

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        col = set()
        posDiag = set() # R + C
        negDiag = set() # R - C
        
        res = []
        board =[["."]*n for i in range(n)]
        
        def backTrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"
                
                backTrack(r+1) 
                
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
                
        backTrack(0)
        return res
                
                