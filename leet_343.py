'''
343. 整数拆分
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设 n 不小于 2 且不大于 58。
'''


class Solution:
    def integerBreak(self, n):

        # method 1
        memory = [1] * (n+1)
        for i in range(3, n+1):
            for j in range(1, i):
                memory[i] = max(j*memory[i-j], j*(i-j), memory[i])
        return memory[n]

        # method 2
        # memory = [-1] * (n+1)
        # #
        # def helper(n):
        #     if n == 1:
        #         return 1
        #     if memory[n] != -1:
        #         return memory[n]
        #
        #     res = -1
        #     for i in range(1, n):
        #         res = max(res, i*(n-i), i*helper(n-i))
        #     memory[n] = res
        #     return res
        #
        # return helper(n)



ss = Solution()
print(ss.integerBreak(5))

