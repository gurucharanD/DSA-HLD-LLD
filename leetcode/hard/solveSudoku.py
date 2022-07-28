# O(1) time and space as the size of the board is always 9/9
# at every step place a number and check if it is valid
# if the number is not valid place a 0 at its place
# and backtrack to the last value that you placed a value
# and try to change its value
# 37. Sudoku Solver

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        def isValid(r,c,val):
            for i in range(0,9):
                if board[i][c] == val:
                    return False
                if board[r][i] == val:
                    return False
                if board[3*(r//3)+i//3][3*(c//3)+i%3] == val:
                    return False
            
            return True
                
                
        def helper(board):
            
            for r in range(0,len(board)):
                for c in range(0,len(board[0])):
                    
                    if board[r][c] == ".":
                                             
                        for val in range(1,10):
                            if isValid(r,c,str(val)):
                                board[r][c] = str(val)
                                if helper(board):
                                    return True
                                else:
                                    board[r][c] = "."
                        
                        return False
                                    
            return True

        return helper(board)
        
	rowIsValid = value not in board[row]
	colIsValid = value not in map(lambda r: r[col],board)
	
	if not rowIsValid or not colIsValid:
		return False
	
	subgridRowStart = row//3
	subgridColStart = col//3
	
	for rowIdx in range(3):
		for colIdx in range(3):
			rowToCheck = subgridRowStart*3 + rowIdx
			colToCheck = subgridColStart*3 + colIdx
			existingValue = board[rowToCheck][colToCheck]
			
			if existingValue == value:
				return False
			
	return True