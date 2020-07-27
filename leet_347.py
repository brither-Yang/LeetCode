
class Solution:
    def topKFrequent(self, nums, k):

        num_count = {}
        for i in nums:
            if i in num_count:
                num_count[i] += 1
            else:
                num_count[i] = 1

        sorted_count = sorted(num_count.items(), key=lambda i: i[1], reverse=True)

        res = []
        for i in range(k):
            res.append(sorted_count[i][0])
        return res

ss = Solution()
print(ss.topKFrequent([1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 6, 6, 6, 6, 6, 7], 3))