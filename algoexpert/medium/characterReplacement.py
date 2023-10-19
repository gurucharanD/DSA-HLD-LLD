# 424. Longest Repeating Character Replacement

# start a sliding window and keep expanding it 
# as long as you have a valid substring
# a substring is valid as long as the following condition is satisfied
# length of substring - count of character with max count in the substring <= k
# here the substring is represented by the sliding window
# find the length of valid substrings and the length of the max window is the answer
# when the sliding window is not valid then move the left pointer to shrink the window

# TC: O(N) since we are sliding through the string only once
# SC: O(26) since there will be only 26 Alphabets

from collections import defaultdict

class Solution:


    def characterReplacement(self, s: str, k: int) -> int:

        counter = defaultdict(int)
        l = 0
        ans = 0

        def isValid(l,r):
            count = 0
            for key in counter:
                count = max(count,counter[key])
            return ((r-l+1)-count) <= k
            
        n = len(s)
        for r in range(n):
            counter[s[r]]+=1
            if isValid(l,r):
                ans = max(ans, r-l+1)
            else:
                counter[s[l]]-=1
                l+=1
        return ans


            





         