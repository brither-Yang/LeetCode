'''
102. 二叉树的层序遍历
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
'''


class Solution:
    def levelOrder(self, root):

        res = []
        if not root:
            return res

        stack = [root]

        while stack:
            tem1 = []
            tem2 = []
            for node in stack:
                tem1.append(node.val)
                if node.left:
                    tem2.append(node.left)
                if node.right:
                    tem2.append(node.right)
            res.append(tem1)
            stack = tem2

        return res


def levelOrder(root):

    if not root:
        return []

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
        stack = tem
        res.append(p)
    return res