class Solution:
    def reverse(self, x: int) -> int:
        num = str(x)
        if num[0] is '-':
            sl = list(num[1:])[::-1]
            ss = ''.join(sl)
            res = -1 * int(ss)
        else:
            sl = list(num)[::-1]
            ss = ''.join(sl)
            res = int(ss)

        if res < -2 ** 31 or res > 2 ** 31 - 1:
            return 0
        return res


ss = Solution()
print(ss.reverse(1534236469))