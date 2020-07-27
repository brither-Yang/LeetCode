# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def creatTree(self, array):
        tem = root = TreeNode(array[0])

        stack = [root]
        while array:
            tem = array.pop(0)
            if tem is None:
                pass
            else:

            node = TreeNode(tem)
            if tem.left == None:
                tem.left = node
            else:
                tem.right = node
            tem =

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        leftMaxDeep = self.maxDepth(root.left)
        rightMaxDeep = self.maxDepth(root.right)

        return max(leftMaxDeep, rightMaxDeep) + 1