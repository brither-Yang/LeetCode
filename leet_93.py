class Solution:
    def restoreIpAddresses(self, s):
        res = []
        n = len(s)

        def backtrack(i, tmp, flag):
            if i == n and flag == 0:
                res.append(tmp[:-1])
                return
            if flag < 0:
                return
            for j in range(i, i + 3):
                if j < n:
                    if i == j and s[j] == "0":
                        backtrack(j + 1, tmp + s[j] + ".", flag - 1)
                        break
                    if 0 < int(s[i:j + 1]) <= 255:
                        backtrack(j + 1, tmp + s[i:j + 1] + ".", flag - 1)

        backtrack(0, "", 4)
        return res

ss = Solution()
print(ss.restoreIpAddresses('25525511125'))
