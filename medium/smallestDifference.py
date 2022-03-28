from calendar import different_locale
from turtle import update
from xml.dom.minidom import Element
from numpy import array_split


def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
	arrayOne.sort()
	arrayTwo.sort()
	
	pointerOne = 0
	pointerTwo = 0
	smallestDiff = float('inf')
	combination = []
	
	while pointerOne < len(arrayOne) and pointerTwo < len(arrayTwo):
		
		if(arrayOne[pointerOne]==arrayTwo[pointerTwo]):
			return[arrayOne[pointerOne],arrayTwo[pointerTwo]];
		
		currentDiff = abs( arrayOne[pointerOne] - arrayTwo[pointerTwo] );
		
		if currentDiff < smallestDiff:
			smallestDiff = currentDiff;
			combination = [arrayOne[pointerOne],arrayTwo[pointerTwo]]
			
		if arrayOne[pointerOne] < arrayTwo[pointerTwo]:
			pointerOne+=1
		else:
			pointerTwo+=1
		
		
    return combination;




# sort the arrays and place a pointer at the beginning of two arrays
# and find the absolute difference between the values pointed by the pointers

# if the current difference is smaller than the global smallest difference, update
# your the global smallest difference with current difference

# increment the pointer that points to the smallest of both the pointers
# because since the arrays are sorted, the elemenent next to the smallest Element
# might be closer to the element pointed by second pointer.


