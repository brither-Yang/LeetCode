'''
75. 颜色分类
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
'''


class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = -1
        two = len(nums)

        i = 0
        while i < two:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                two -= 1
                nums[i], nums[two] = nums[two], nums[i]
            else:
                zero += 1
                nums[i], nums[zero] = nums[zero], nums[i]
                i += 1
        return nums


li = [1, 0, 2]
ss = Solution()
print(ss.sortColors(li))