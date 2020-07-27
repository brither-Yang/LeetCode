'''
16. 最接近的三数之和
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案。

示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

提示：

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
'''


class Solution:
    def threeSumClosest(self, nums, target):
        n = len(nums)
        if n < 3:
            return False

        close_num = abs(target)
        nums.sort()
        for i in range(n):

            l, r = i+1, n-1

            while l < r:
                threeS = nums[i] + nums[l] + nums[r]
                sub_num = abs(target - threeS)
                close_num = min(close_num, sub_num)

                if close_num

