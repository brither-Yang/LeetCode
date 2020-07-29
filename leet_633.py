'''
633. 平方数之和
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。

示例1:

输入: 5
输出: True
解释: 1 * 1 + 2 * 2 = 5

示例2:

输入: 3
输出: False
'''


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c < 0:
            return False
        l = 0
        r = int(c ** 0.5)
        while l <= r:
            res = l * l + r * r
            if res == c:
                return True
            elif res > c:
                r -= 1
            else:
                l += 1
        return False


if __name__ == '__main__':
    ss = Solution()
    print(ss.judgeSquareSum(1000000000))