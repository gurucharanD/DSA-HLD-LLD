# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 987. Vertical Order Traversal of a Binary Tree

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        node_list = []

        def BFS(root):
            queue = [(root, 0, 0)]
            while queue:
                node, row, column = queue.pop(0)
                if node is not None:
                    node_list.append([column, row, node.val])
                    queue.append((node.left, row + 1, column - 1))
                    queue.append((node.right, row + 1, column + 1))

        BFS(root)

        node_list.sort()
        print(node_list)

        ret = OrderedDict()
        for column, row, value in node_list:
            if column in ret:
                ret[column].append(value)
            else:
                ret[column] = [value]

        return ret.values()