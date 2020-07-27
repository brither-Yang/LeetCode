class Solution:
    def fourSum(self, nums, target):

        n = len(nums)
        if n < 4:
            return []

        res = []
        nums.sort()
        for i in range(n-1):
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                if i > 0 and nums[i] == nums[i-1]:
                    continue

                l, r = j+1, n-1
                while l < r:
                    fourS = nums[i] + nums[j] + nums[l] + nums[r]

                    if fourS == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])

                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        while l < r and nums[l] == nums[l+1]:
                            l += 1

                        r -= 1
                        l += 1

                    elif fourS > target:
                        r -= 1
                    else:
                        l += 1
        return res


ss = Solution()
print(ss.fourSum([-1,-5,-5,-3,2,5,0,4], -7))