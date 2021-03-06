'''
15. 三数之和
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


class Solution:
    def threeSum(self, nums):

        n = len(nums)
        if n < 3:
            return []
        res = []
        nums.sort()
        for i in range(n):

            if nums[i] > 0:
                return res

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = n - 1
            while l < r:
                threeS = nums[i] + nums[l] + nums[r]
                if threeS == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while nums[l] == nums[l+1]:
                        l += 1
                    while nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif threeS > 0:
                    r -= 1
                else:
                    l += 1

        return res


ss = Solution()
print(ss.threeSum([-1, 0, 1, 2, -1, -4]))
