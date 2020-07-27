'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
'''

import numpy as np
class Solution:
    def longestPalindrome(self, s):

        n = len(s)
        dp = np.zeros((n, n), bool)
        ans = ''

        for l in range(n):
            for i in range(n):
                j = i + 1
                if j >= n:
                    break

                if l == 0:
                    dp[i, j] = True
                elif l == 1:
                    dp[i, j] = (s[i] == s[j])
                else:
                    dp[i, j] = (dp[i+1, j-1] and s[i] == s[j])

                if dp[i, j] and l+i > len(ans):
                    ans = s[i: j+1]
        return ans

ss = Solution()
print(ss.longestPalindrome('abcdcd'))