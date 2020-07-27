'''
220. 存在重复元素 III
在整数数组 nums 中，是否存在两个下标 i 和 j
使得 nums[i] 和 nums[j] 的差的绝对值小于等于 t
且满足 i 和 j 的差的绝对值也小于等于 ķ 。

如果存在则返回 true，不存在返回 false。

示例 1:

输入: nums = [1,2,3,1], k = 3, t = 0
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1, t = 2
输出: true
示例 3:

输入: nums = [1,5,9,1,5,9], k = 2, t = 3
输出: false
'''


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):

        recoder = set()
        max_val = float('-inf')
        min_val = float('inf')
        for i in range(len(nums)):
            if len(recoder):
                max_val = max(recoder)
                min_val = min(recoder)
            if min_val <= (nums[i] + t) and (nums[i] - t) <= max_val:
                return True
            else:
                recoder.add(nums[i])
            print(recoder)

            if len(recoder) == k+1:
                recoder.remove(nums[i-k])

        return False


ss = Solution()
print(ss.containsNearbyAlmostDuplicate(nums=[1, 5, 9, 1, 5, 9], k=2, t=3))