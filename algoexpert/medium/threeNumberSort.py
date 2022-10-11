# BRUTEFORCE : O( len(ORDER) * len(array) * len(array) )
# for every element in the order 
# find the corresponding elements in the array 
# and swap them with the elements
# since len(ORDER) is always 3
# we can conisder it to be O(n^2)

def threeNumberSort(array, order):
    # Write your code here.
	start = 0
	for i in range(0,len(order)):
		for j in range(start,len(array)):
			if order[i] != array[j]:
				index = findIndexToSwap(order[i],j+1,array)
				if index == -1:
					break
				else:
					array[j],array[index] = array[index],array[j]
					start = j+1				
    return array

def findIndexToSwap(order,index,array):
	for k in range(index,len(array)):
		if array[k] == order:
			return k
		
	return -1

# second approach is to 
# break the array into three parts
# first part of the array contains first element in the order array
# loop the array in forward direction
# last part of the array contains last element in the order array
# loop the array in backward direction
# the middle part contains the middle element in the order array
# this gets automatically sorted as we the first and last parts
# are sorted. the middle elements get pushed to middle by default
# this approach invlolves multiple individual lopps over the input array

# optimised approach it to use three pointers
# first pointer points to the first element in the array
# second pointer points to the second element in the array
# third pointer points to the last element in the array

# always compare the elements of the array that are pointed by the second pointer

# if the value pointed by secondPointer is euqal to firstValue in order array
# swap pointer1 and pointer2
# increment the pointer1 and pointer2

# elif it is equal to the second value in the order array
# dont swap just increment the pointer

# elif it is equal to the third value in the order array
# swap and decrement the third pointer



def threeNumberSort(array, order):
    # Write your code here.
	firstIndex = 0
	secondIndex = 0
	thirdIndex = len(array)-1
	
	firstValue = order[0]
	secondValue = order[1]
	thirdValue = order[2]
	
	while secondIndex <= thirdIndex:
		
		value = array[secondIndex]
		
		if value == firstValue:
			array[secondIndex],array[firstIndex] = array[firstIndex],array[secondIndex]
			secondIndex+=1
			firstIndex+=1
		elif value == secondValue:
			secondIndex+=1
		else:
			array[secondIndex],array[thirdIndex] = array[thirdIndex],array[secondIndex]
			thirdIndex-=1

    return array




