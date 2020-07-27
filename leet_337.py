'''
337. 打家劫舍 III
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:

输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

输出: 7
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
示例 2:

输入: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):

        # if not root:
        #     return 0
        #
        #     # 抽象到最小结构 动态规划结合递归， [3,2,3,null,3,null,1]为例
        #     # 递归到第二层2时 （不抢收益是3， 抢收益是2）;递归到第二层3时（不抢收益是1，抢收益是3）
        #     # 此时如何倒推到根节点是关键
        #     # 一般会想max(左抢+右抢， 抢根节点+左不抢+右不抢)是根节点的最优值 按照这个思路写会有一个问题
        #     # 就是 4 3 2 1这中情况不对，这是个思维陷阱：
        #     # res4= (0, 4)  res3=(4, 3) 这里在算res2不抢的时候，如果只是从res3抢继承过来就会导致错过4这个最优解
        #     # 所以我们修改max(左抢+右抢， 抢根节点+左不抢+右不抢) 为
        #     # max(max(左不抢+右抢, 左抢+右不抢， 左不抢+右不抢， 左抢+右抢)， 抢根节点+左不抢+右不抢)
        #     # 等价为 max(max(左不抢,左抢)+max(右不抢，右抢)， 抢根节点+左不抢+右不抢)
        #
        # def func(root):
        #     # 终止条件
        #     if not root:
        #         return 0, 0
        #
        #     # 递归调用
        #     left_not_do, left_do = func(root.left)
        #     right_not_do, right_do = func(root.right)
        #
        #     # 本次函数返回什么
        #     return max(left_not_do, left_do) + max(right_not_do, right_do), left_not_do + right_not_do + root.val
        #
        # return max(func(root))

        return self.helper(root)[1]

    def helper(self, root):
        if not root:
            return [0, 0]

        left_amount = self.helper(root.left)
        right_amount = self.helper(root.right)

        without_root = left_amount[1] + right_amount[1]
        with_root = root.val + left_amount[0] + right_amount[0]

        return [without_root, max(without_root, with_root)]