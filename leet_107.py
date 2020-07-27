'''
107. 二叉树的层次遍历 II
给定一个二叉树，返回其节点值自底向上的层次遍历。
（即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]
'''


class Solution:
    def levelOrderBottom(self, root):

        if not root:
            return []

        stack = [root]
        result = []
        while stack:
            num = len(stack)
            r_temp = []
            for i in range(num):
                node = stack.pop(0)
                r_temp.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            result.insert(0, r_temp)
        return result

def levelOrderBottom(root):
    res = []
    if not root:
        return res

    stack = [root]
    res = []
    while stack:
        tem = []
        p = []
        for node in stack:
            p.append(node.val)
            if node.left:
                tem.append(node.left)
            if node.right:
                tem.append(node.right)
        res.append(p)
        stack = tem
    return res[::-1]