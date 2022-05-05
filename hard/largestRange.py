# create a hash map of all the elements in the array
# start looping over the input array and check 
# if the left and right elements of the current element are present in the hashmap
# if they are present decrement the left pointer and increment the right pointer
# else calculate the range and update the best range if current range is 
# greater than already known better range

# O(n) time and Space

def largestRange(array):
    # Write your code here.
	bestRange = []
	longestLength = 0
	nums = {}
	for num in array:
		nums[num] = True
		
	for num in array:
		
		if not nums[num]:
			continue
			
		nums[num] = False
		currentLength = 1
		left = num-1
		right = num+1
		
		while left in nums:
			nums[left] = False
			currentLength+=1
			left -=1
		
		while right is nums:
			nums[right] = False
			currentLength+=1
			right+=1
		
		if currentLength > longestLength:
			longestLength = currentLength
			bestRange = [left+1,right-1]
		
	return bestRange
