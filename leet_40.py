class Solution:
    def combinationSum2(self, candidates, target):

        res = []
        candidates.sort()

        def helper(nums, p):

            p.sort()
            if p in res:
                return
            else:
                if sum(p) == target:
                    res.append(p)
                    return
            if sum(p) > target:
                return

            for i in range(len(nums)):
                helper(nums[i+1:], p+[nums[i]])

        helper(candidates, [])
        return res


ss = Solution()
print(ss.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))