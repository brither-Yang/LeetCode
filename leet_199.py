'''
199. 二叉树的右视图
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
'''


class Solution:
    def rightSideView(self, root):

        if not root:
            return []

        res = []
        stack = [root]
        while stack:

            res.append(stack[-1].val)
            tem = []
            for node in stack:
                if node.left:
                    tem.append(node.left)
                if node.right:
                    tem.append(node.right)
            stack = tem
        return res


def rightSideView(root):

    res = []
    if not root:
        return res

    stack = [root]
    res = []
    while stack:
        tem = []
        res.append(stack[-1].val)
        for node in stack:
            if node.left:
                tem.append(node.left)
            if node.right:
                tem.append(node.right)
        stack = tem

    return res