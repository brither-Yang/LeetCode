'''
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
'''

class Solution:
    def getRow(self, rowIndex):

        res = [1]

        for i in range(rowIndex):

            tem = [1]

            if len(res) > 1:
                for j in range(len(res)-1):
                    ss = res[j] + res[j+1]
                    tem.append(ss)
            tem.append(1)
            res = tem

        return res


ss = Solution()
print(ss.getRow(3))