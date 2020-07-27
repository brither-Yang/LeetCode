'''
209. 长度最小的子数组
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的子数组，并返回其长度。
如果不存在符合条件的子数组，返回 0。

示例：

输入：s = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
'''


class Solution:
    def minSubArrayLen(self, s, nums):

        if sum(nums) < s:
            return 0
        min_length = len(nums)
        i, j = 0, 0

        while j < len(nums):
            nums_sum = sum(nums[i: j])
            if nums_sum >= s:
                length = j - i
                if length < min_length:
                    min_length = length
                i += 1
            else:
                j += 1
        return min_length


ss = Solution()
print(ss.minSubArrayLen(s=7, nums=[1, 1]))
