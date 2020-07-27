'''
62. 不同路径
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？
'''


import numpy as np
class Solution:
    def uniquePaths(self, m, n):
        dp = np.ones((m, n), np.int32)

        for i in range(1, m):
            for j in range(1, n):
                dp[i, j] = dp[i, j-1] + dp[i-1, j]

        return int(dp[m-1, n-1])


ss = Solution()
print(ss.uniquePaths(7, 3))