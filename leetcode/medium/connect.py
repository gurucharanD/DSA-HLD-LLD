"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if root is None:
            return None
        
        sol = []
        q = [root]
        
        while len(q):
            level = []
            length = len(q)
            prev = None
            for _ in range(length):
                node = q.pop(0)
                if prev:
                    prev.next = node
                level.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                    
                prev = node
            
            sol.append(level[:])
            
        return root