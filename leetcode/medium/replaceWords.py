class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        
        wordsInSentence = sentence.split(" ")
        outPut = ""
        for i in range(0,len(wordsInSentence)):
            
            word = wordsInSentence[i]
            
            for j in range(0,len(word)):
                if word[0:j] in dictionary:
                    wordsInSentence[i] = word[0:j]
                    break
                    
        for word in wordsInSentence:
            outPut += word+" "
                
        return outPut.strip()

        