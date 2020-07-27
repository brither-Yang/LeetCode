# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.stack = []

    def postorderTraversal(self, root):
        if not root:
            return []
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.stack.append(root.val)

        return self.stack