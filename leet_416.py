'''
416. 分割等和子集
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:

输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].


示例 2:

输入: [1, 2, 3, 5]

输出: false

解释: 数组不能分割成两个元素和相等的子集.
'''


class Solution:
    def canPartition(self, nums):

        # 思路：选出其中一些数据，是的其和为 sum(nums) / 2

        def helper(nums, index, s):

            if s == 0:
                return True
            if index < 0 or s < 0:
                return False

            if memory[index][s] != -1:
                return memory[index][s] == 1

            res = helper(nums, index - 1, s) or helper(nums, index - 1, s - nums[index])

            memory[index][s] = 1 if res else 0

            return memory[index][s]

        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False

        S = int(nums_sum / 2)
        memory = [[-1 for _ in range(S+1)] for _ in range(len(nums))]

        return bool(helper(nums, len(nums)-1, S))


ss = Solution()
print(ss.canPartition([1, 5, 5, 11]))

def dp(nums):

    nums_sum = sum(nums)
    if nums_sum % 2:
        return False

    n = len(nums)
    C = int(nums_sum / 2)

    dp = [False for _ in range(C+1)]

    for i in range(C):
        dp[i] = nums[0] == i

    for i in range(1, n):
        for j in range(C, nums[i]-1, -1):
            dp[j] = dp[j] or dp[j-nums[i]]

    return dp[C]


print(dp([1, 1]))


