# 128. Longest Consecutive Sequence

# create a hashmap of the elements in the array as keys and each key has value as False
# this hashmap is used to avoid double counting the elements
# for every element compute the left and right numbers of it in the numeric order
# left is 1 smaller the current element and right is 1 greater than the current element
# keep going to the left as long as you keep finding the smaller numbers having difference 1, mark the elements that you have used as TRUE
# keep going to the right as long as you keep finding the greater numbers having difference 1, mark the elements that you have used as TRUE
# at every step compute the range i.e difference between left and right, and keep track of the longest range
# O(N) time and O(N) space.

class Solution(object):
    def longestConsecutive(self, array):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(array) == 0:
            return 0
        
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

            while right in nums:
                nums[right] = False
                currentLength+=1
                right+=1

            if currentLength > longestLength:
                longestLength = currentLength
                bestRange = [left+1,right-1]

        return bestRange[1]-bestRange[0]+1