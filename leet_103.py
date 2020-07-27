'''
103. 二叉树的锯齿形层次遍历
给定一个二叉树，返回其节点值的锯齿形层次遍历。
（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]
'''


class Solution:
    def zigzagLevelOrder(self, root):

        res = []
        if not root:
            return res

        stack = [root]
        level = 0
        while stack:
            tem1 = []
            tem2 = []
            for node in stack:
                tem1.append(node.val)
                if node.left:
                    tem2.append(node.left)
                if node.right:
                    tem2.append(node.right)
            if level % 2 == 0:
                res.append(tem1)
            else:
                res.append(tem1[::-1])
            stack = tem2
            level += 1
        return res


def zigzagLevelOrder(root):
    res = []
    if not root:
        return res

    stack = [root]
    level = 1
    while stack:
        tem = []
        p = []
        for node in stack:
            if level % 2:
                p.append(node.val)
            else:
                p.insert(0, node.val)
            if node.left:
                tem.append(node.left)
            if node.right:
                tem.append(node.right)
        res.append(p)
        stack = tem
        level += 1
    return res