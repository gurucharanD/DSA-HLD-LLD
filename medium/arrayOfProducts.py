from numpy import product
from pandas import array


def arrayOfProducts(array):
    # Write your code here.
	if len(array)<=1:
		return array;
	
	products = [1 for _ in range(len(array))]
	leftProducts = [1 for _ in range(len(array))]
	rightProducts = [1 for _ in range(len(array))]
	
	leftProducts[0] = 1
	rightProducts[len(array)-1] = 1
	
	for i in range(1,len(array)):
		leftProducts[i] = leftProducts[i-1]*array[i-1]

	for i in reversed(range(len(array)-1)):
		rightProducts[i] = rightProducts[i+1]*array[i+1]
		
	for i in range(len(array)):
		products[i]=leftProducts[i]*rightProducts[i]
		
		
    return products



# create 2 arrays that hold the left product and right product of elements in the array
# left product of first element will be 1
# right product of last element will be 1

# leftProduct[i] = array[i]*leftProduct[i-1]
# rightProduct[i] = array[i]*righProduct[i+1]

# product[i] = leftProduct[i]*rightProduct[i]
