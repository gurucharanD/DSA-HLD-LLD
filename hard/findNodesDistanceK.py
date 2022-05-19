# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) time and space

def findNodesDistanceK(tree, target, k):
    # Write your code here.
	nodesToParents = {}
	populatNodeToParents(tree,nodesToParents)
	targetNode = getNodeFromValue(target,tree,nodesToParents)
    return bfs(targetNode,nodesToParents,k)

def getNodeFromValue(value,tree,nodeToParents):
	if tree.value == value:
		return tree
	
	nodeParent = nodeToParents[value]
	if nodeParent.left and nodeParent.left.value == value:
		return nodeParent.left
	
	return nodeParent.right
	
def populatNodeToParents(node,nodeToParents,parent=None):
	if node:
		nodeToParents[node.value] = parent
		populatNodeToParents(node.left,nodeToParents,node)
		populatNodeToParents(node.right,nodeToParents,node)
		
def bfs(targetNode,nodesToParents,k):
	queue = [(targetNode,0)]
	seen = {targetNode.value}
	while len(queue)>0:
		currentNode,distance = queue.pop(0)
		
		if distance == k:
			nodesDistanceK = [node.value for node,_ in queue]
			nodesDistanceK.append(currentNode.value)
			return nodesDistanceK
		
		connectedNodes = [currentNode.left,currentNode.right,nodesToParents[currentNode.value]]
		for node in connectedNodes:
			if node is None:
				continue
			if node.value in seen:
				continue
				
			seen.add(node.value)
			queue.append((node,distance+1))
		
	return []

	
	
	
	
	
	
	