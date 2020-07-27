class Solution:
    def combinationSum3(self, k, n):

        res = []
        ran = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        def helper(nums, p):
            if len(p) == k and sum(p) == n:
                res.append(p)
                return
            if len(p) > k or sum(p) > n:
                return

            for i in range(len(nums)):
                helper(nums[i+1:], p+[nums[i]])

        helper(ran, [])
        return res


ss = Solution()
print(ss.combinationSum3(3, 9))
