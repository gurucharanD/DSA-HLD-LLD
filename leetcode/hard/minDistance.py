# 72. Edit Distance


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def helper(i,j):
            if i < 0:
                return j+1
            if j < 0:
                return i+1
            
            if word1[i] == word2[j]:
                return helper(i-1,j-1)
            else:
                return 1 + min(
                    helper(i-1,j-1),
                    helper(i-1,j),
                    helper(i,j-1)
                )
            
        return helper(len(word1)-1,len(word2)-1)
            