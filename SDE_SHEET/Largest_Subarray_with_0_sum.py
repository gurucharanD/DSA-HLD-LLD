N = 8
A = [15,-2,2,-8,1,7,10,23]

class Solution:
    def maxLen(self, n, arr):
        #Code here
        seen = {0:-1}
        ans = 0
        add = 0
        
        for i in range(len(arr)):
            add += arr[i]
            if add in seen:
                ans = max(ans,i-seen[add])
            else:
                seen[add]=i
        
        return ans