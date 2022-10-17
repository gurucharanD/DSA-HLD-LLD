# 449. Serialize and Deserialize BST

# The preorder traversal of the  tree can be saved in a deque
# and using the same technique as checking if the binary tree 
# is a valid BST where each node has to fall between a min and max
# value we can construct the tree back

class Codec:
# serialize_deserialize
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        
        preOrder = deque([])
        
        def dfs(node):
            if not node:
                return
            
            preOrder.append(node.val)
            dfs(node.left)
            dfs(node.right)
            
            return
        
        dfs(root)
        # print(inOrder)
        return "#".join(map(str,preOrder))
            

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        
        data = list(data.split("#"))
        data = list(map(int,data))
        data = deque(data)
                
        def buildBST(low,high):
            
            if data and ( low < data[0] < high ):

                val = data.popleft()
                newNode = TreeNode(val)

                newNode.left = buildBST(low,val)
                newNode.right = buildBST(val,high)

                return newNode
        
        return buildBST(float("-inf"),float("inf"))
        
        
        
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans