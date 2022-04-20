# to jump to the first index, we need 0 steps
# to jump to other indexes, we dont know how many steps we need
# so we initialise it to infinity

# dynamic programming using, O(n^2) time and O(n) space

# for i in range(0,n):
#     for j in range(0,i):
#         if array[j]+j >= i:
#             jumps[i] = min(jumps[i],jumps[j]+1)

def minNumberOfJumps(array):
	jumps = [float("inf") for _ in range(0,len(array))]	
	jumps[0] = 0
	
	for i in range(1,len(array)):
		for j in range(0,i):
			if array[j]+j >= i:
				jumps[i] = min(jumps[i],jumps[j]+1)
				
	
	return jumps[-1]


# solution 2:

def minNumberOfJumps(array):
    # Write your code here.
	if len(array) == 1:
		return 0
	
	jumps = 0
	maxReach = array[0]
	steps = array[0]
	
	for i in range(1,len(array)-1):
		maxReach = max(maxReach,i+array[i])
		
		steps-=1
		
		if steps==0:
			jumps+=1
			steps = maxReach - i
		
    return jumps+1





