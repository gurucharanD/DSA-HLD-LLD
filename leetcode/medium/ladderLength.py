# 127. Word Ladder
# "hit"
# "cog"
# ["hot","dot","dog","lot","log","cog"]

from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        # build adjacency list for all patterns
        # that are possible with the given words
        #  {
        #       '*ot': ['hot', 'dot', 'lot'],
        #       'h*t': ['hot', 'hit'], 
        #       'ho*': ['hot'],
        #       'd*t': ['dot'],
        #       'do*': ['dot', 'dog'],
        #       '*og': ['dog', 'log', 'cog'],
        #       'd*g': ['dog'],
        #       'l*t': ['lot'], 
        #       'lo*': ['lot', 'log'],
        #       'l*g': ['log'], 
        #       'c*g': ['cog'], 
        #       'co*': ['cog'],
        #       '*it': ['hit'], 
        #       'hi*': ['hit']
        #  }

        adjList = defaultdict(list)
        wordList.append(beginWord)
        
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] +"*"+ word[j+1:]
                adjList[pattern].append(word)
        
        # perform BFS on the adjacent list
        # since we are finding the shortest distance
        # start at start word and keep incrementing the levels
        # until the end word is found
        # the neighbours of a word are the words that are 
        # present in the adjacency list of patterns of
        # the current word

        visited = set([beginWord])
        q = [beginWord]
        res = 1
        
        while q:
            
            length = len(q)
            
            for _ in range(length):
                
                word = q.pop(0)
                if word == endWord:
                    return res
                
                for j in range(len(word)):
                    pattern = word[:j] +"*"+ word[j+1:]
                    
                    for nei in adjList[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)

            res+=1
        
        return 0