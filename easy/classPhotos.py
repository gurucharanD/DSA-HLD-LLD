def classPhotos(redShirtHeights, blueShirtHeights):
	
    # Write your code here.
	redShirtHeights.sort();
	blueShirtHeights.sort();
	
	firstRow = redShirtHeights;
	secondRow = blueShirtHeights;
	
	if firstRow[0]>secondRow[0]:
		secondRow = redShirtHeights
		firstRow = blueShirtHeights
		
	print(firstRow,secondRow)
	for i in range(len(firstRow)):
		if firstRow[i]>=secondRow[i]:
			return False
	
    return True


# O(nlogn) -> due to sort
