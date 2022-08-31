# 496. Next Greater Element I

# initialise the stack with index 0
# and start iterating over the array

# keep adding the indexes into the stack 
# as long as you dont find the elements at current index
# greater than the element at the index of the top of the stack

# once you find a greater element at a index, keep popping the 
# elements from the stack as long as the element at the index
# is greater than the element at the top of the stack


class Solution:
    def nextGreaterElement(self, nums1: List[int], array: List[int]) -> List[int]:
        outputArray = [-1 for _ in array]
        stack = [0]
	
        for index in range(len(array)):

            while len(stack) > 0 and array[index] > array[stack[-1]]:
                poppedIndex = stack.pop()
                outputArray[poppedIndex] = array[index]
            stack.append(index)
            
        print(outputArray)
        ans = []
        for num in nums1:
            ans.append(outputArray[array.index(num)])
        return ans