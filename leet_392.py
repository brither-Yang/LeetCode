class Solution:
    def isSubsequence(self, s, t):

        ss = sorted([i for i in s])
        tt = sorted([i for i in t])
        print(ss, tt)

        i, j = 0, 0
        while i < len(ss) and j < len(tt):
            if ss[i] == tt[j]:
                i += 1
                j += 1
            else:
                j += 1
            if 
        if i == len(ss) - 1:
            return True
        else:
            return False

ss = Solution()
print(ss.isSubsequence(s = "abc", t = "ahbgdc"))