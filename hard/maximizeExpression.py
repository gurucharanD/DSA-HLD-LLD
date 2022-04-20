# brute force: O(n^4)

def maximizeExpression(array):
    # Write your code here.
	
	if len(array) < 4:
		return 0
	
	maximum = float("-inf")
	
	for i in range(0,len(array)):
		for j in range(i+1,len(array)):
			for k in range(j+1,len(array)):
				for l in range(k+1,len(array)):
						maximum = max(maximum,array[i]-array[j]+array[k]-array[l])
	
    return maximum


def maximizeExpression(array):
	if len(array) < 4:
		return 0
	
	op1 = [float("-inf") for _ in array]
	op1[0] = array[0]
	for i in range(1,len(array)):
		op1[i] = max(array[i],op1[i-1])
		
	op2 = [float("-inf") for _ in array]
	for i in range(1,len(array)):
		op2[i] = max(op1[i-1] - array[i],op2[i-1])
		
	op3 = [float("-inf") for _ in array]
	for i in range(2,len(array)):
		op3[i] = max(op2[i-1] + array[i],op3[i-1])
		
	
	op4 = [float("-inf") for _ in array]
	for i in range(3,len(array)):
		op4[i] = max(op3[i-1] - array[i],op4[i-1])
		

	return op4[len(array)-1]