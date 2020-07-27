class Solution:
    def readBinaryWatch(self, num):

        hours = [1, 2, 4, 8]
        minite = [1, 2, 4, 8, 16, 32]
        res = []

        def helper(num, index, p):
            """
            num : 还剩下的可点亮的灯的数量
            index: 是当前选择点亮哪一个灯
            status: 记录是哪些位置的灯被点亮了
            """
            if num == 0:
                h = sum([i*j for i, j in zip(hours, p[:4])])
                m = sum([i*j for i, j in zip(minite, p[4:])])
                if h < 12 and m < 60:
                    res.append('%d:%02d' % (h, m))
                return

            for i in range(index, 10):
                p[i] = 1
                helper(num-1, i+1, p)
                p[i] = 0
        helper(num, 0, [0]*10)
        return res

ss = Solution()
print(ss.readBinaryWatch(1))