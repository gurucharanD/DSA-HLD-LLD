# https://leetcode.com/problems/permutation-in-string/solutions/3873356/python-sliding-window-o-26-n/
# 567. Permutation in String

# Instead of creating m*n substring windows, as the window moves from 0 to n-m we decrement the count of character pointed by L and 
# add the new characters that are added to the window by the sliding R pointer.
# This makes our code run in a linear time 
# and the compare operation used to compare the 
# counts of characters in the window with s1 has to atmost 26 comparisons it could be considered as running in a constant time




from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        def compare(s1_counter,s2_counter):
            for c in s1_counter:
                if c in s2_counter:
                    if s1_counter[c] != s2_counter[c]:
                        return False
                else:
                    return False
            return True
        
        
        m = len(s1)
        n = len(s2)
        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:m])

        if compare(s1_counter,s2_counter):
            return True
        
        s2_counter[s2[0]]-=1
        for l in range(1,n-m+1):
            r = (l+m)-1
            s2_counter[s2[r]]+=1

            if compare(s1_counter,s2_counter):
                return True

            s2_counter[s2[l]]-=1

        return False






            



