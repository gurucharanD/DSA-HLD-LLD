class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        
        @lru_cache(maxsize=None)
        def helper(row,currSum):
            
            if row == rows:
                return abs(currSum-target)
            
            ans = float("inf")
            for num in mat[row]:
                ans = min(ans,helper(row+1,currSum+num))
                if currSum+num >= target:
                    break
                
            return ans
        
        rows = len(mat)
        for i in range(rows):
            # the reason we create a set is to avoid duplicates 
            # in each row as the duplciates would result in the 
            # same state 
            # the reason we sort the elements is because
            # once we reach a point where the sum of the 
            # elements choosen is greater than the target
            # if we keep going on adding new elements to the 
            # sum it would only increase the difference
            # between the target sum and sum hence
            # we could avoid such calculations and it saves
            # us a lot of time
            mat[i] = sorted(set(mat[i]))

        return helper(0,0)        
        