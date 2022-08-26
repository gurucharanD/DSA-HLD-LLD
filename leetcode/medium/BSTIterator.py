# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# insert the left most nodes of the tree into Stack
# as these are the first ones to be returned when next is called

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        node = root
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        ans = node.val
        if not node.right:
            return ans
        
        node = node.right
        while node:
            self.stack.append(node)
            node = node.left
        
        return ans
        
    def hasNext(self) -> bool:
        return not len(self.stack) == 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()