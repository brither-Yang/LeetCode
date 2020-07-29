'''
540. 有序数组中的单一元素
给定一个只包含整数的有序数组，每个元素都会出现两次，唯有一个数只会出现一次，找出这个数。

示例 1:

输入: [1,1,2,3,3,4,4,8,8]
输出: 2
示例 2:

输入: [3,3,7,7,10,11,11]
输出: 10
注意: 您的方案应该在 O(log n)时间复杂度和 O(1)空间复杂度中运行。
'''


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # res = 0
        # for i in nums:
        #     res = res ^ i
        # return res
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            print(m)

            if m % 2 == 1:
                m -= 1

            if nums[m] == nums[m+1]:
                l = m + 2
            else:
                r = m
        return nums[l]


if __name__ == '__main__':
    ss = Solution()
    print(ss.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))