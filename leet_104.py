# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):

        if not root:
            return 0

        leftMaxDeep = self.maxDepth(root.left)
        rightMaxDeep = self.maxDepth(root.right)

        return max(leftMaxDeep, rightMaxDeep)