# 1858. Longest Word With All Prefixes
# insert all the words into Trie
# for each word in the array, check if the prefixes exist in the trie
# return the longest string with the max prefix matches

class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        current = self.root
        for l in word:
            if l not in current:
                current[l] = {}
            current = current[l]
        current['*'] = True
        
    def search(self, word: str) -> bool:
        current = self.root
        for l in word:
            if l in current:
                current = current[l]
            else:
                return False
            
        return '*' in current

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for l in prefix:
            if l in current:
                current = current[l]
            else:
                return False
            
        return True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        words.sort()
        print(words)
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        # print(trie.root)
        ans = ''
        
        for word in words:
            flag = False
            if len(word) > len(ans):
                current = trie.root
                for l in word:
                    if l in current:
                        current = current[l]
                        if '*' not in current:
                            flag = True
                            break
                        
                if flag:
                    continue
                else:
                    ans = word
                
        return ans
            
            