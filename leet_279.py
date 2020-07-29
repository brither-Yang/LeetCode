'''
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）
使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.

'''

# from math import sqrt
# class Solution:
#     def numSquares(self, n):
#
#         memory = [i for i in range(n+1)]
#
#         for i in range(2, n+1):
#             for j in range(1, int(sqrt(i))+1):
#
#                 memory[i] = min(memory[i], memory[i-j*j]+1)
#
#         return memory[n]
#
#
# ss = Solution()
# print(ss.numSquares(8))


# class node:
#     def __init__(self, value, step=0):
#         self.value = value
#         self.step = step
#
#     def __str__(self):
#         return '<value:{}, step:{}>'.format(self.value, self.step)
#
#
# class Solution1:
#     def numSquares(self, n: int) -> int:
#         queue = [node(n)]
#         visited = set([node(n).value])
#
#         while queue
#             vertex = queue.pop(0)
#             residuals = [vertex.value - n * n for n in range(1, int(vertex.value ** .5) + 1)]
#             for i in residuals:
#                 new_vertex = node(i, vertex.step + 1)
#                 if i == 0:
#                     return new_vertex.step
#
#                 elif i not in visited:
#                     queue.append(new_vertex)
#                     visited.add(i)
#
#         return -1
#
#
# sss = Solution1()
# print(sss.numSquares(13))


class Solution:

    def numSquares(self, n):

        queue = [(n, 0)]
        visited = {n, }
        while queue:
            node = queue.pop(0)
            value = node[0]
            step = node[1]

            i = 1
            while True:
                res = value - i * i
                if res < 0:
                    break
                if res == 0:
                    return step + 1
                if res not in visited:
                    queue.append((res, step + 1))
                    visited.add(res)
                i += 1
        return -1


ss = Solution()
print(ss.numSquares(13))
