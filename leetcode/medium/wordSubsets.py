# 916. Word Subsets

# Create a counter of all the chars of words in words2
# and the counter of each character represents the max count
# of the character in all the words
# for 'foo': c2 = {'o': 2, 'f': 1}
# for 'off': c2 = {'o': 1, 'f': 2}
# so: d = {'o': 2, 'f': 2}

class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        ans= []
        counter =  defaultdict(int)

        for i in range(0,len(words2)):
            tempCounter = Counter(words2[i])
            
            for char in tempCounter:
                counter[char] = max(counter[char],tempCounter[char])

        for word in words1:
            tempCounter = Counter(word)
            for char in counter:
                if tempCounter[char] < counter[char]:
                    break
            else:
                ans.append(word)
                
        
        return ans
            
            

            
        