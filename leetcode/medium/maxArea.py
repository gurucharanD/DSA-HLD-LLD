# Sort the arrays, then compute the maximum difference 
# between two consecutive elements for horizontal cuts and vertical cuts.
# The answer is the product of these maximum values in horizontal cuts and vertical cuts.

# append 0,h and 0,w since the max area can also be formed
# with the edges as well


class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        horizontalCuts.append(0)
        verticalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(w)
        
        horizontalCuts.sort()
        verticalCuts.sort()
        
        currHMaxDiff = 0
        currVMaxDiff = 0

        for i in range(1,len(horizontalCuts)):
            currHMaxDiff = max(currHMaxDiff,horizontalCuts[i]-horizontalCuts[i-1])
            
        for i in range(1,len(verticalCuts)):
            currVMaxDiff = max(currVMaxDiff,verticalCuts[i]-verticalCuts[i-1])
        
        return (currHMaxDiff*currVMaxDiff)%(10**9+7)