'''
63. 不同路径 II
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
'''

import numpy as np
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = np.zeros((m, n), np.int32)
        if obstacleGrid[0][0] == 1:
            return 0

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i, j] = 1

                elif i == 0 and j > 0:
                    if obstacleGrid[i][j] == 0:
                        dp[i, j] = dp[i, j-1]

                elif j == 0 and i > 0:
                    if obstacleGrid[i][j] == 0:
                        dp[i, j] = dp[i-1, j]

                else:
                    if obstacleGrid[i][j] == 0:
                        dp[i, j] = dp[i, j-1] + dp[i-1, j]

        return dp[-1, -1]

        # m = len(obstacleGrid)
        # n = len(obstacleGrid[0])
        # dp = [1] + [0] * n
        # for i in range(0, m):
        #     for j in range(0, n):
        #         dp[j] = 0 if obstacleGrid[i][j] else dp[j] + dp[j - 1]
        # return dp[-2]


ss = Solution()
print(ss.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))

