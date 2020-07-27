'''
144. 二叉树的前序遍历
给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]
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

    def preorderTraversal(self, root):
        if not root:
            return []
        self.stack.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.stack

    # 非递归
    def preorderTravelBinaryTree(self, root):
        if not root:
            return []

        stack = [root]
        res = []

        while stack:

            node = stack.pop()
            res.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res



