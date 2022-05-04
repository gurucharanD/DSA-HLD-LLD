# find all the ones on the border as these are invalid islands
# loop through the border, and save all invalid islands in a data struture

# then loop through the internal border and see 
# if there are any islands that touch the invalid islands that we already know
# if they touch then make these islands invalid


  [1, 0, 0, 0, 0, 0],
  [0, 1, 0, 1, 1, 1],
  [0, 0, 1, 0, 1, 0],
  [1, 1, 0, 0, 1, 0],
  [1, 0, 1, 1, 0, 0],
  [1, 0, 0, 0, 0, 1]





def removeIslands(matrix):
    # Write your code here.
	onceConnectedToBorder = [[False for _ in matrix[0]] for _ in matrix]
	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			rowIsBorder = row == 0 or row == len(matrix)-1
			colIsBorder = col == 0 or col == len(matrix[row])-1
			isBorder = rowIsBorder or colIsBorder
			
			if not isBorder:
				continue
			
			if matrix[row][col]!=1:
				continue
				
			findOnesConnectedToBorder(matrix,row,col,onceConnectedToBorder)
			
	for row in range(1,len(matrix)-1):
		for col in range(1,len(matrix[row])-1):
			if onceConnectedToBorder[row][col]:
				continue
			matrix[row][col] = 0
	return matrix


def findOnesConnectedToBorder(matrix,startRow,startCol,onceConnectedToBorder):
	stack = [(startRow,startCol)]
	while len(stack) > 0:
		currentPosition = stack.pop()
		currentRow,currentCol = currentPosition
		
		alreadyVisited = onceConnectedToBorder[currentRow][currentCol]
		if alreadyVisited:
			continue
			
		onceConnectedToBorder[currentRow][currentCol] = True
	
		neighbours = getNeighbours(currentRow,currentCol,matrix)
		print(currentRow,currentCol)
		for neighbour in neighbours:
			print(neighbour)
			row,col = neighbour
			if matrix[row][col] != 1:
				continue
			stack.append(neighbour)
						
def getNeighbours(row,col,matrix):
	neighbours = []
	numRows = len(matrix)
	numCols = len(matrix[row])
	
	print('-',numRows,numCols)
	
	#top
	if row-1 >= 0:
		neighbours.append((row-1,col))
	#bottom
	if row+1 < numRows:
		neighbours.append((row+1,col))
	#left
	if col-1>=0:
		neighbours.append((row,col-1))
	#right
	if col+1 < numCols:
		neighbours.append((row,col+1))

	return neighbours