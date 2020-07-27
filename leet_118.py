'''
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
'''

class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []

        res = [[1]]

        for i in range(numRows-1):

            tem = [1]

            p = res[-1]
            if len(p) > 1:
                for j in range(len(p)-1):
                    ss = p[j] + p[j+1]
                    tem.append(ss)
            tem.append(1)
            res.append(tem)

        return res


ss = Solution()
print(ss.generate(5))