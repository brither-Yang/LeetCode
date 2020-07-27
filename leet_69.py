class Solution:
    def mySqrt(self, x):
        if x < 0:
            return -1

        low = 0
        high = x
        error = 1e-6
        while low <= high:
            if x**2 == x:
                return int(x)
            mid = (high + low) / 2
            if mid**2 == x or abs(mid**2 - x) <= error:
                return int(mid)
            elif mid**2 > x:
                high = mid
            else:
                low = mid


ss = Solution()
print(ss.mySqrt(6))