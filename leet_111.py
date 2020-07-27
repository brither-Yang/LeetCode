# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        if not root:
            return 0

        queue = [(1, root)]
        while queue:
            depth, node = queue.pop(0)

            if node.left is None and node.right is None:
                return depth
            if node.left:
                queue.append((depth+1, node.left))
            if node.right:
                queue.append((depth+1, node.right))