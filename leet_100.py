# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isSameTree(self, p, q):
        # 都是空的，情况相同，返回 是
        if p is None and q is None:
            return True

            # 其中一个是空的，另一个不空，返回 否
        if p is None and q is not None:
            return False
        if p is not None and q is None:
            return False

        # 值不相同，返回 否
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
