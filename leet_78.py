class Solution:
    def subsets(self, nums):
        res = []

        def helper(nums, p):
            res.append(p)
            if not nums:
                return

            for i in range(len(nums)):
                helper(nums[i+1:], p+[nums[i]])

        helper(nums, [])
        return res

ss = Solution()
print(ss.subsets([1, 2, 3]))