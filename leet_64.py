'''
64. 最小路径和
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
'''


import numpy as np


class Solution:
    def minPathSum(self, grid):

        n = len(grid)
        m = len(grid[0])
        memory = np.zeros((n+1, m+1))

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):

                if i == n-1:
                    memory[i, j] = grid[i][j] + memory[i, j+1]
                elif j == m-1:
                    memory[i, j] = grid[i][j] + memory[i+1, j]
                elif i != (n-1) and j != (m-1):
                    memory[i, j] = min(grid[i][j] + memory[i+1, j], grid[i][j] + memory[i, j+1])

        return int(memory[0][0])


ss = Solution()
print(ss.minPathSum([
  [1, 3, 1],
  [1, 5, 1],
  [4, 2, 1]
]))



