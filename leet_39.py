class Solution:
    def combinationSum(self, candidates, target):

        res = []

        def helper(nums, p):

            if sum(p) == target:
                res.append(p)
                return
            if sum(p) > target:
                return

            for i in range(len(nums)):
                helper(nums[i:], p+[nums[i]])

        helper(candidates, [])
        return res

ss = Solution()
print(ss.combinationSum([2, 3, 5], 8))
