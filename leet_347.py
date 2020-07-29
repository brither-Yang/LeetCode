'''
347. 前 K 个高频元素
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
提示：

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
你可以按任意顺序返回答案。
'''

import heapq


class Solution:
    def topKFrequent(self, nums, k):

        num_count = {}
        for i in nums: num_count[i] = num_count.get(i, 0) + 1

        # sorted_count = sorted(num_count.items(), key=lambda i: i[1], reverse=True)
        # print(sorted_count)
        #
        # res = []
        # for i in range(k):
        #     res.append(sorted_count[i][0])
        # return res

        res = []
        max_heap = [(-val, key) for key, val in num_count.items()]
        heapq.heapify(max_heap)

        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res


if __name__ == '__main__':

    ss = Solution()
    print(ss.topKFrequent([1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 6, 6, 6, 6, 6, 7], 3))