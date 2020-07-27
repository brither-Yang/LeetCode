'''
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。
'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        n = len(nums1) + len(nums2)

        nums = nums1 + nums2
        nums.sort()

        mid = n // 2
        if n % 2 == 0:
            return (nums[mid-1] + nums[mid]) / 2
        else:
            return nums[mid]


ss = Solution()
print(ss.findMedianSortedArrays([1, 3, 5], [2, 4]))