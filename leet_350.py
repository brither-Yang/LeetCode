'''
350. 两个数组的交集 II
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
'''


class Solution:
    def intersect(self, nums1, nums2):

        num = []
        dic1 = {}
        for i in nums1: dic1[i] = dic1.get(i, 0) + 1

        for i in nums2:
            if i in dic1 and dic1[i] != 0:
                num.append(i)
                dic1[i] -= 1
        return num


ss = Solution()
print(ss.intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))
