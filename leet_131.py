class Solution:
    def partition(self, s):
        res = []

        def helper(s, tem):

            if not s:
                res.append(tem)

            for i in range(1, len(s)+1):
                if s[:i] == s[:i][::-1]:
                    helper(s[i:], tem+[s[:i]])
        helper(s, [])
        return res

ss = Solution()
print(ss.partition('aab'))