
# place 2 pointers at the begining of the array,
# keep incrementing the right pointer and add elements into hashSet
# when ever you find an element that is already in hashset that is pointed by right pointer
# it means that you have arrived at a place that is duplicate of the left pointer
# remove the element that is pointed by left pointer from hashset and increment the left pointer
# at every iteration keep track of the maxLength, which is the differene between
# left and right pointer + 1 





class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashSet = set()
        
        left = 0
        right = 0
        maxLength = 0
        
        for right in range(0,len(s)):
            
            while s[right] in hashSet:
                hashSet.remove(s[left])
                left+=1
                
            maxLength = max(maxLength,right-left+1)
            hashSet.add(s[right])
            
        return maxLength