'''
二分查找法 O(nlogn)
'''

class Solution:
    def twoSum(self, numbers, target):

        for i in range(len(numbers)):
            new_num = numbers[i+1:]
            n = len(new_num)
            left = 0
            right = n - 1

            res = target - numbers[i]

            while left <= right:
                mid = (left + right) // 2
                index = new_num.index(new_num[mid])

                if res == new_num[mid]:
                    return [i+1, index+1+i+1]
                elif res > new_num[mid]:
                    left = mid + 1
                else:
                    right = mid - 1


h = Solution()
print(h.twoSum([0, 0, 3, 6], 0))