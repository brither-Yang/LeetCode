'''
128. 最长连续序列
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
'''


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        s = set(nums)
        res = 0

        for num in nums:

            if num - 1 in s:
                continue

            length = 1
            while num + 1 in s:
                num += 1
                length += 1

            res = max(res, length)

        return res


ss = Solution()
print(ss.longestConsecutive([100, 4, 200, 1, 3, 2]))