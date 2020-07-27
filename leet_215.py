'''
215. 数组中的第K个最大元素
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
'''


class Solution:
    def findKthLargest(self, nums, k):

        # 替换nums[i]后维护最小堆：自顶向下调整新元素位置，直至该值满足(parent value < son value)
        def shift(i, k):
            flag = 0
            while (i*2+1) < k and flag == 0:
                t = i
                if nums[i] > nums[2*i+1]:
                    t = 2 * i + 1
                if (i*2+2) < k and nums[t] > nums[2*i+2]:
                    t = 2 * i + 2
                if t == i:
                    flag = 1
                else:
                    nums[i], nums[t] = nums[t], nums[i]
                    i = t

        # O(k):建立大小为K的最小堆， k/2 - 1是最后一个非叶节点，因为shift是向下调整，所以倒序从最下面出发
        # 不然(4 32 1)->(2 34 1)->(2 14 3)->(2 14 3) 结果不对
        for i in range(k / 2, -1, -1):
            shift(i, k)

        # O((N-k)logK)，剩余元素依次比较替换
        for i in range(k, len(nums)):
            if nums[0] < nums[i]:
                nums[0] = nums[i]
                shift(0, k)
        return nums[0]
        # sum=O(Nlogk-k(logK-1))

