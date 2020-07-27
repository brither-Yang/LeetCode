'''
120. 三角形最小路径和
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。



例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
'''


class Solution:
    def minimumTotal(self, triangle):
        n = len(triangle)
        print(triangle)

        for i in range(n-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] = triangle[i][j] + min(triangle[i+1][j], triangle[i+1][j+1])

        print(triangle)
        return triangle[0][0]



ss = Solution()
print(ss.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 10, 8, 3]]))