"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

# diameter of a binary tree is the longest path between any two nodes in the tree
# at every node diameter is calculated by sum of left tree height and right tree height
# at any node height is calculated by 1+max(left tree height,right tree height) 

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        ans = 0
        def traversal(node):
            
            nonlocal ans
            if node.children:
                tallest = 0
                second_tallest = 0
                
                for child in node.children:
                    curr_height = traversal(child)
                    
                    if not tallest:
                        tallest = curr_height
                    else:
                        if curr_height > tallest:
                            second_tallest = tallest
                            tallest = curr_height
                        elif curr_height > second_tallest:
                            second_tallest = curr_height
                                
                if tallest and second_tallest:
                    ans = max(ans,tallest+second_tallest)
                else:
                    ans = max(ans,tallest)
                return 1+tallest
            
            return 1
        
        traversal(root)
        return ans
            