'''
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

示例 1:

输入:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出: 3
解释:
长度最长的公共子数组是 [3, 2, 1]。

'''

class Solution:
    def findLength(self, A, B):

        s1 = ''
        s2 = ''
        for i, j in zip(A, B):
            s1 += str(i)
            s2 += str(j)

        l = 0
        r = 0
        max_length = 0

        while r <= len(A):
            ss = s1[l:r]
            if ss in s2 and len(ss) > max_length:
                max_length = len(ss)
            

