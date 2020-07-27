class Solution:
    def permute(self, nums):

        if not nums:
            return []
        res = []

        def helper(nums, p):
            if not nums:
                res.append(p)
                return

            for i in range(len(nums)):
                helper(nums[:i] + nums[i+1:], p+[nums[i]])
        helper(nums, [])
        return res


ss = Solution()
print(ss.permute([1, 2, 3]))