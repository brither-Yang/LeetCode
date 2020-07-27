'''
242. 有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
'''


from collections import defaultdict

class Solution:
    def isAnagram(self, s, t):

        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for i in s: s_dict[i] += 1
        for i in t: t_dict[i] += 1
        if s_dict == t_dict:
            return True
        else:
            return False


ss = Solution()
print(ss.isAnagram("ab", "ba"))