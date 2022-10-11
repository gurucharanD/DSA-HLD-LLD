# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array):
    # Write your code here.
	return ProductSumHelper(array,1)
    pass

def ProductSumHelper(array,depth):
	productSum = 0;

	for i in array:
		if isinstance(i,list):
			productSum = productSum + depth*ProductSumHelper(i,depth+1)
		else:
			productSum = productSum + (i*depth);
	
	print(array,depth,productSum)

		
	return productSum
