# {'a': {'p': {'p': {'l': {'e': {'*': True}}}}}}
# {'a': {'p': {'p': {'l': {'e': {'*': True}}, '*': True}}}}
# Python Trie representation ^

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
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)