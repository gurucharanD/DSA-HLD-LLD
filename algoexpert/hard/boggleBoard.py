# use trie
# when you need to string matching, tries come in handy

def boggleBoard(board, words):
    # Write your code here.
	trie = Trie()
	for word in words:
		trie.add(word)
		
	finalWords = {}
	visited = [[False for col in row] for row in board]
	for r in range(0,len(board)):
		for c in range(0,len(board[r])):
			explore(r,c,board,trie.root,visited,finalWords)
	
	return list(finalWords.keys())

def explore(r,c,board,trieNode,visited,finalWords):
	if visited[r][c]:
		return
	
	letter = board[r][c]
	if letter not in trieNode:
		return 
	visited[r][c] = True
	trieNode = trieNode[letter]
	if "*" in trieNode:
		finalWords[trieNode["*"]]=True
	
	neighbours = getNeighbours(r,c,board)
	for neighbour in neighbours:
		explore(neighbour[0],neighbour[1],board,trieNode,visited,finalWords)
	visited[r][c] = False
	
def getNeighbours(r,c,board):
	neighbours = []
	
	if r != 0:
		neighbours.append([r-1,c])
	if r != len(board)-1:
		neighbours.append([r+1,c])
	if c != len(board[0])-1:
		neighbours.append([r,c+1])
	if c!=0:
		neighbours.append([r,c-1])
		
	if r!=0 and c!=0:
		neighbours.append([r-1,c-1])
	if r!=0 and c != len(board[0])-1:
		neighbours.append([r-1,c+1])
	if c != len(board[0])-1 and  r != len(board)-1 :
		neighbours.append([r+1,c+1])
	if c != 0 and  r != len(board)-1 :
		neighbours.append([r+1,c-1])
	
	return neighbours


class Trie:
	def __init__(self):
		self.root = {}
		self.endSymbol = "*"
		
	def add(self,word):
		current = self.root
		for letter in word:
			if letter not in current:
				current[letter] = {}
			current = current[letter]
		current[self.endSymbol] = word
		