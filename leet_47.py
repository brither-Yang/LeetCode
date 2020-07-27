class Solution:
    def permuteUnique(self, nums):
        res = []

        def helper(nums, p):

            if not nums:
                if p in res:
                    return
                else:
                    res.append(p)
                    return

            for i in range(len(nums)):
                helper(nums[:i]+nums[i+1:], p+[nums[i]])

        helper(nums, [])
        return res


ss = Solution()
print(ss.permuteUnique([1, 1, 2]))