class Solution:
    def addToArrayForm(self, A, K):

        ss = 0
        for i, num in enumerate(A[::-1]):
            ss += num * 10 ** i

        ssSum = ss + K

        return [int(i) for i in str(ssSum)]

ss = Solution()
print(ss.addToArrayForm([1, 2, 0, 0], 34))