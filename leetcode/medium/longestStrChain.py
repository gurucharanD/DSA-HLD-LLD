# 1048. Longest String Chain
# sort the list of words in the list in ascending order of length
# because the successor of word[i] is greater in length 
# than word[i],for each word start removing a character 
# one by one and check if the word formed by removing the 
# character is already in the dictionary, 
# no of successors[i] is 1 + no of successors of the newly formed word

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        dic = {}
        
        words.sort(key=len)
        
        for i in words:
            
            dic[i] = 1

            for j in range(0,len(i)):
                succ = i[:j] + i[j+1:]
                if succ in dic:
                    dic[i] = max(dic[i],1+dic[succ])
                    
        return max(dic.values())
                    
        