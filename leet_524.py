'''
524. 通过删除字母匹配到字典里最长单词
给定一个字符串和一个字符串字典，找到字典里面最长的字符串，
该字符串可以通过删除给定字符串的某些字符来得到。如果答案不止一个，
返回长度最长且字典顺序最小的字符串。如果答案不存在，则返回空字符串。

示例 1:

输入:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

输出:
"apple"
示例 2:

输入:
s = "abpcplea", d = ["a","b","c"]

输出:
"a"
说明:

所有输入的字符串只包含小写字母。
字典的大小不会超过 1000。
所有输入的字符串长度不会超过 1000。
'''


class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """

        def is_substr(s, target):
            i, j = 0, 0
            while i < len(s) and j < len(target):
                if s[i] == target[j]:
                    j += 1
                i += 1
            return j == len(target)

        d.sort()
        longest_word = ""
        for target in d:
            l1, l2 = len(longest_word), len(target)
            if l1 > l2 or l1 == l2:
                continue

            if is_substr(s, target):
                longest_word = target

        return longest_word


if __name__ == '__main__':
    ss = Solution()
    print(ss.findLongestWord(s="abpcplea", d=["ale", "apple", "monkey", "plea"]))