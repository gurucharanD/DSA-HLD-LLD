class Trie:

    def __init__(self):
        self.root = {"count":0}
        
    def insert(self, word: str) -> None:
        current = self.root
        for l in word:
            if l not in current:
                current[l] = {"count":0}
            
            current = current[l]
            current["count"]+=1
        
    def search(self, word: str):
        current = self.root
        count = 0
        for l in word:
            if l in current:
                current = current[l]
                count += current['count']
            else:
                return 0
        return count

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        trie = Trie()        
        ans = []
        
        # insert each word into a trie
        # during the insertion, update the count
        # which represents the no of times the 
        # each character occurs as a prefix in other strings
        
        for word in words:
            trie.insert(word)
        
        # during search- return the sum of all the count
        # of all the prefixes that occur in the word
        for word in words:
            ans.append(trie.search(word))
        
        return ans
                
        