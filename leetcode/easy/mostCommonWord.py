class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        paragraph = paragraph.lower()
        
        symbols = "!?',;."
        
        words = []
        word = ''
        
        for char in paragraph:
            if char in symbols or char == ' ':
                if word not in banned and word != '':
                    words.append(word)
                word = ''
            else:
                word+=char
                
        words.append(word)
        
        counter = Counter(words)
        maxCount = 0
        ans = None
        
        for word in counter:
            if counter[word] > maxCount:
                ans = word
                maxCount = counter[word]
        
        return ans
        
        