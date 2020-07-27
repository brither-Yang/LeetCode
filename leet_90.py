class Solution:
    def subsetsWithDup(self, nums):
        res = []

        def helper(nums, p):
            p.sort()
            if p not in res:
                res.append(p)
            if not nums:
                return

            for i in range(len(nums)):
                helper(nums[i+1:], p+[nums[i]])

        helper(nums, [])
        return res