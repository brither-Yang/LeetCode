'''
91. 解码方法
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。

示例 2:

输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
'''

class Solution:

    def numDecodings(self, s):

        # dp[i] 表示前 i 个数字可以表示成的字母方式数目
        n = len(s)
        if n == 0:
            return 0

        dp = [0] * (n+1)
        dp[0] = 1

        for i in range(1, n+1):
            t = int(s[i-1])
            if 0 < t < 10:
                dp[i] += dp[i-1]
            if i >= 2:
                t = int(s[i-2])*10 + int(s[i-1])
                if 10 <= t <= 26:
                    dp[i] += dp[i-2]

        return dp[-1]


ss = Solution()
print(ss.numDecodings('226'))