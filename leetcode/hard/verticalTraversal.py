# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# vertical order traversal
# with top view and bottom view

from sortedcontainers import SortedDict
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        node_list = []
        topView = SortedDict()
        bottomView = SortedDict()

        def BFS(root):
            queue = [(root, 0, 0)]
            while queue:
                node, row, column = queue.pop(0)
                if node :
                    node_list.append([column, row, node.val])
                    if column not in topView:
                        topView[column] = node.val
                        
                    bottomView[column] = node.val
                    queue.append((node.left, row + 1, column - 1))
                    queue.append((node.right, row + 1, column + 1))

        BFS(root)
        print(topView.values())
        print(bottomView.values())
        node_list.sort()

        ret = OrderedDict()
        for column, row, value in node_list:
            if column in ret:
                ret[column].append(value)
            else:
                ret[column] = [value]
        
        return ret.values()