'''
70. 爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
'''

# 递归 + 记忆化搜索
class Solution:
    def climbStairs(self, n):

        memory = [-1] * (n+1)

        def find_ways(n):

            if n == 0 or n == 1:
                return 1

            if memory[n] == -1:
                memory[n] = find_ways(n-1) + find_ways(n-2)
            return memory[n]

        return find_ways(n)


ss = Solution()
print(ss.climbStairs(3))