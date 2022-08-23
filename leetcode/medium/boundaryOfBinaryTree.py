# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# get the left boundary
# get the leaves
# get the right boundary
# boundary = [root.val] + left + leaves + list(reversed(right))
# return boundary

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def getleftBoundary(curr = root.left, leftBoundary = []):
            if not curr:
                return leftBoundary
            #if leaf node
            if not curr.left and not curr.right:
                return leftBoundary
            leftBoundary.append(curr.val)
            if curr.left:
                return getleftBoundary(curr.left, leftBoundary)
            else:
                return getleftBoundary(curr.right, leftBoundary)                
                
        def getrightBoundary(curr = root.right, rightBoundary = []):
            if not curr:
                return rightBoundary
            #if leaf node
            if not curr.left and not curr.right:
                return rightBoundary
            rightBoundary.append(curr.val)
            if curr.right:
                return getrightBoundary(curr.right, rightBoundary)
            else:
                return getrightBoundary(curr.left, rightBoundary)
            
        def getLeaves(curr = root, leaves = []):
            if not curr:
                return
            if not curr.left and not curr.right:
                leaves.append(curr.val)
                return
            getLeaves(curr.left, leaves)
            getLeaves(curr.right, leaves)
            return leaves
            
        if not root.left and not root.right:
            return [root.val]

        leaves = getLeaves()
        left = getleftBoundary()
        right = getrightBoundary()

        boundary = [root.val] + left + leaves + list(reversed(right))
        return boundary

                
        