def minimumPassesOfMatrix(matrix):
	passes = convertNegative(matrix)
	return passes-1 if not containsNegative(matrix) else -1

def convertNegative(matrix):
	nextQ = getAllPositivePositions(matrix)
	passes = 0
	while len(nextQ)>0:
		currentQ = nextQ
		nextQ = []
		while len(currentQ) > 0:
			currentRow,currentCol = currentQ.pop(0)
			adjacentPositions = getAdjacentPositions(currentRow,currentCol,matrix)
			for position in adjacentPositions:
				row,col = position
				value = matrix[row][col]
				if value<0:
					matrix[row][col] *= -1
					nextQ.append([row,col])
		passes+=1
	return passes	
	
def getAllPositivePositions(matrix):
	positivePositions = []
	
	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			value = matrix[row][col]
			if value>0:
				positivePositions.append([row,col])
				
	return positivePositions

def getAdjacentPositions(row,col,matrix):
	
	adjacentPositions = []
	
	if row>0 :
		adjacentPositions.append([row-1,col])
		
	if row < len(matrix)-1 :
		adjacentPositions.append([row+1,col])
		
	if col > 0 :
		adjacentPositions.append([row,col-1])
		
	if	col < len(matrix[0]) -1 :
		adjacentPositions.append([row,col+1])
	
	return adjacentPositions

def containsNegative(matrix):
	for row in matrix:
		for value in row:
			if value < 0:
				return True
	return False
			




