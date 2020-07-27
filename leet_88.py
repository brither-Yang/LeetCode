class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        newNums = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                min_num = nums1[i]
                i += 1
            else:
                min_num = nums2[j]
                j += 1
            newNums.append(min_num)
        newNums.extend(nums1[i:n])
        newNums.extend(nums2[j:m])
        return newNums


l1 = [1, 2, 3, 0, 0, 0]
l2 = [2, 5, 6]
ss = Solution()
print(ss.merge(l1, 3, l2, 3))