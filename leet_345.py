'''
345. 反转字符串中的元音字母
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:

输入: "hello"
输出: "holle"
示例 2:

输入: "leetcode"
输出: "leotcede"
说明:
元音字母不包含字母"y"。
'''


class Solution:
    def reverseVowels(self, s):
        ss = [i for i in s]
        i = 0
        j = len(ss) - 1
        l = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        while i < j:
            if ss[i] in l and ss[j] in l:
                ss[i], ss[j] = ss[j], ss[i]
                i += 1
                j -=1
            if ss[i] not in l:
                i += 1
            if ss[j] not in l:
                j -= 1
        return ''.join(ss)

ss = Solution()
print(ss.reverseVowels('aA'))