from tkinter.tix import DECREASING


def isMonotonic(array):
	
	if len(array)==0:
		return True
	
	order = 'asc'
	if array[0]>array[len(array)-1]:
		order='desc'
		
    for i in range(len(array)-1):
		if(array[i] != array[i+1]):
			if(array[i] < array[i+1] and order == 'asc'):
				continue
			elif(array[i] > array[i+1] and order == 'desc'):			
				continue
			else:
				return False;
			
	return True;
			


# find the order which you need to verify, either it is increasing or DECREASING

# skip if the elements are same
# for each element identify if the order is being satisfied
# at any point if the order is not satisfied return false

# at the end of theloop return true