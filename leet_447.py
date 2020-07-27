'''
447. 回旋镖的数量
给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，
其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。

找到所有回旋镖的数量。你可以假设 n 最大为 500，
所有点的坐标在闭区间 [-10000, 10000] 中。

示例:

输入:
[[0,0],[1,0],[2,0]]

输出:
2

解释:
两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
'''


class Solution:
    def numberOfBoomerangs(self, points):

        def distance(x1, x2):
            return (x1[0] - x2[0]) ** 2 + (x1[1] - x2[1]) ** 2
        count = 0
        for i in range(len(points)):
            counter = {}
            for j in range(len(points)):
                if i != j:
                    dis = distance(points[i], points[j])
                    counter[dis] = counter.get(dis, 0) + 1
            for value in counter.values():
                count += value * (value - 1)

        return count


ss = Solution()
print(ss.numberOfBoomerangs([[0,0],[1,0],[2,0]]))