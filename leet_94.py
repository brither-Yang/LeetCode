'''
94. 二叉树的中序遍历
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.stack = []

    def inorderTraversal(self, root):
        if not root:
            return []
        self.inorderTraversal(root.left)
        self.stack.append(root.val)
        self.inorderTraversal(root.right)
        return self.stack

    # 非递归
    def ineorderTravelBinaryTree(self, root):
        if not root:
            return []

        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            res.append(node.val)
        return res[::-1]

