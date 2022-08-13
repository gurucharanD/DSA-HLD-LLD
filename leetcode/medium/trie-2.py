# 1804. Implement Trie II (Prefix Tree)
# intialise the root node with cp (count prefix) and ew (ends with) properties
# everytime you insert a new word into the trie, for each character node increment the cp
# when you reach the end of the string, increment the value of ew
# erasing the string is totally opposite to insert
# decrement the value of cp for each character and at the end
# decrement the value of ew

class Trie:

    def __init__(self):
        self.root = {"ew":0,"cp":0}
        

    def insert(self, word: str) -> None:
        current = self.root
        for l in word:
            if l not in current:
                current[l] = {"ew":0,"cp":0}
            
            current = current[l]
            current["cp"]+=1
        
        current["ew"]+=1
        
        
    def countWordsEqualTo(self, word: str) -> int:
        current = self.root
        for l in word:
            if l in current:
                current = current[l]
            else:
                return 0
        
        return current['ew']
        

    def countWordsStartingWith(self, prefix: str) -> int:
        current = self.root
        for l in prefix:
            if l in current:
                current = current[l]
            else:
                return 0
        
        return current['cp']
    
    def erase(self, word: str) -> None:
        current = self.root
        for l in word:
            if l in current:
                current = current[l]
                current['cp']-=1
            else:
                return

        current['ew']-=1
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
