'''
69. x 的平方根
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。
'''


class Solution:
    def mySqrt(self, x):
        if x < 1:
            return x

        low = 1
        high = x

        while low <= high:

            mid = int((high + low) / 2)
            sqrt = x / mid
            if sqrt == mid:
                return mid

            elif sqrt >= mid:
                low = mid + 1
            else:
                high = mid - 1
        return high


if __name__ == '__main__':

    ss = Solution()
    print(ss.mySqrt(16))