# when you are at row 0 and moving upwards, then you change direction to right
# when you are at last column, we cant go right then we go down 
# when you are at col 0 move down

def zigzagTraverse(array):
    # Write your code here.
	height = len(array)-1
	width = len(array[0])-1
	result = []
	row,col = 0,0 
	goingDown = True
	
	while not isOutOfBounds(row,col,height,width):
		result.append(array[row][col])
		if goingDown:
			if col == 0 or row == height:
				goingDown = False
				if row == height:
					col+=1
				else:
					row+=1
			else:
				row+=1
				col-=1
		else:
			if row == 0 or col == width:
				goingDown = True
				if col == width:
					row+=1
				else:
					col+=1
			else:
				col+=1
				row-=1
					
	return result
						
		
	
def isOutOfBounds(row,col,height,width):
	return row < 0 or row > height or col < 0 or col > width
