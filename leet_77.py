class Solution:
    def combine(self, n, k):
        res = []

        def helper(nums, p):

            if len(p) == k:
                res.append(p)
                return

            for i in range(len(nums)):
                helper(nums[i+1:], p+[nums[i]])
            return

        helper([i for i in range(1, n+1)], [])
        return res


ss = Solution()
print(ss.combine(4, 2))
