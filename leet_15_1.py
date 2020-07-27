class Solution:
    def threeSum(self, nums):

        n = len(nums)
        if n < 3:
            return []
        res = []
        nums.sort()

        for i in range(n-2):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-1):
                if nums[j] > abs(nums[i]):
                    break

                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                target = -(nums[i] + nums[j])
                if target in nums[j+1:]:
                    res.append([nums[i], nums[j], target])

        return res


ss = Solution()
print(ss.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
