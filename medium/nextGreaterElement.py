
# loop through the array 2 times as this is a circular array 
# initialise the output array with all -1
# initialise a stack ( using array ) and loop thorugh the array

# compare the current element to the element on top of the stack

# if the element on top of stack is smaller than current element
# then current element is the next greater element to the element on top of the stack
# add index of current element on to the top of the stack

# when you find an element greater than the element 
# at the top of the stack, we keep poping the stack until the elements in the stack 
# are smaller than current element.
# and push the current element on to the stack


def nextGreaterElement(array):
    # Write your code here.
	outputArray = [-1 for _ in array]
	stack = []
	
	for index in range(2*len(array)):
		currentIndex = index % len(array)

		while len(stack) > 0 and array[currentIndex] > array[stack[len(stack)-1]]:
			poppedIndex = stack.pop()
			outputArray[poppedIndex] = array[currentIndex]
			
		stack.append(currentIndex)
    return outputArray





