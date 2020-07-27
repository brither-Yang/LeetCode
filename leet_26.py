'''
26. 删除排序数组中的重复项
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。



示例 1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。
'''


class Solution:
    def removeDuplicates(self, nums):

        n = len(nums)
        k = 0
        for i in range(1, n):
            if nums[i] != nums[k]:
                nums[k + 1] = nums[i]
                k += 1

        return len(nums[:k+1])


ss = Solution()
print(ss.removeDuplicates([0,1,1,1,2,2,3,3,4]))


class Solution:
    def removeDuplicates(self, nums):

        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i += 1

        return len(nums)

