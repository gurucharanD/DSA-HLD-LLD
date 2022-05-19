# O(1) time and space as the size of the board is always 9/9
# at every step place a number and check if it is valid
# if the number is not valid place a 0 at its place
# and backtrack to the last value that you placed a value
# and try to change its value


def solveSudoku(board):
	solvePartialSudoku(0,0,board)
    return board

def solvePartialSudoku(row,col,board):
	currentRow = row
	currentCol = col
	
	if currentCol == len(board[row]):
		currentRow+=1
		currentCol=0
		
		if currentRow == len(board):
			return True
	
	if board[currentRow][currentCol] == 0:
		return tryDigitsAtPosition(currentRow,currentCol,board)
	
	return solvePartialSudoku(currentRow,currentCol+1,board)

def tryDigitsAtPosition(row,col,board):
	for digit in range(1,10):
		if isValidAtPosition(digit,row,col,board):
			board[row][col] = digit
			if solvePartialSudoku(row,col+1,board):
				return True
			
	board[row][col] = 0
	return False

def isValidAtPosition(value,row,col,board):
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