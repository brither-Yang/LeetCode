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

    def maxDepth1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        stack = [root]
        depth = 0
        while stack:
            tem = []
            for node in stack:
                if node.left:
                    tem.append(node.left)
                if node.right:
                    tem.append(node.right)
            stack = tem
            depth += 1
        return depth