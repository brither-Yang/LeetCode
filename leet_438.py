class Solution:
    def findAnagrams(self, s, p):

        p_dic = {}
        for i in p: p_dic[i] = p_dic.get(i, 0) + 1

        l = 0
        r = len(p)
        res = []
        window = {}
        for i in s[l: r]: window[i] = window.get(i, 0) + 1

        while r <= len(s):

            if window == p_dic:
                res.append(l)

            if r == len(s):
                break

            window[s[l]] -= 1
            window[s[r]] = window.get(s[r], 0) + 1
            if window[s[l]] == 0:
                del window[s[l]]
            if window[s[r]] == 0:
                del window[s[r]]
            l += 1
            r += 1
        return res


s1 = 'a' * 20001
s2 = 'a' * 10001
ss = Solution()
print(ss.findAnagrams('', 'ab'))


from collections import Counter
from collections import defaultdict

class Solution1:

    def haha(self, s, p):
        if len(s) < len(p):
            return []

        def contains(s_dic, p_dic):
            if len(s_dic) < len(p_dic):
                return False
            for i in p_dic:
                if i not in s_dic or s_dic[i] < p_dic[i]:
                    return False
            return True

        p_dic = Counter(p)
        s_dic = defaultdict(int)
        l, r = 0, len(p)
        res = []

        for i in range(len(p)):
            s_dic[s[i]] += 1

        while r <= len(s):

            if contains(s_dic, p_dic):
                res.append(l)

            if r == len(s):
                break

            s_dic[s[l]] -= 1
            s_dic[s[r]] += 1

            l += 1
            r += 1

        return res


ss = Solution1()
print(ss.haha('', 'ab'))