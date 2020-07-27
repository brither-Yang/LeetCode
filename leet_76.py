'''
76. 最小覆盖子串
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。
'''


from collections import defaultdict
from collections import Counter


class Solution:
    def minWindow(self, s, t):

        def contains(counter, target):

            if len(counter) < len(target):
                return False
            for i in target:
                if i not in counter or counter[i] < target[i]:
                    return False

            return True

        target = Counter(t)
        counter = defaultdict(int)
        l, r = 0, 0
        min_str = ""
        min_length = len(s)

        while r < len(s):

            counter[s[r]] += 1

            while contains(counter, target):
                length = r - l + 1
                if min_length >= length:
                    min_length = length
                    min_str = s[l: r+1]

                counter[s[l]] -= 1
                l += 1

            r += 1

        return min_str


ss = Solution()
print(ss.minWindow("abc", "ac"))
