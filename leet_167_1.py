'''
O(n)
'''
class Solution():
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers) - 1
        while i < j:
            res = numbers[i] + numbers[j]
            if target == res:
                return [i+1, j+1]
            elif target > res:
                i += 1
            elif target < res:
                j -= 1

ss = Solution()
print(ss.twoSum([2, 7, 9, 41], 10))

