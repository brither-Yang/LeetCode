'''
1. 两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''


class Solution:
    def twoSum(self, nums, target):

        # num_dic = {}
        # for i, num in enumerate(nums):
        #     if target-num in num_dic:
        #         return [num_dic[target-num], i]
        #     else:
        #         num_dic[num] = i
        # else:
        #     return False
        for i in range(len(nums)):
            ss = target - nums[i]
            if ss in nums[i+1:]:
                return [i, nums[i+1:].index(ss)+1+i]
        return False


ss = Solution()
print(ss.twoSum([2, 7, 11, 15], 13))


