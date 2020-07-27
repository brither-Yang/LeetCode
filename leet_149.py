'''
149. 直线上最多的点数
给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。

示例 1:

输入: [[1,1],[2,2],[3,3]]
输出: 3
解释:
^
|
|        o
|     o
|  o
+------------->
0  1  2  3  4
示例 2:

输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出: 4
解释:
^
|
# # |  o
# # |     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
'''


class Solution:
    def maxPoints(self, points):
        if len(points) <= 2:
            return len(points)

        def tan(point1, point2):
            if point1[1] == point2[1]:
                return 0
            return (point1[0] - point2[0]) / (point1[1] - point2[1])

        count = 0

        for i in range(len(points)):
            counter = {}
            for j in range(i+1, len(points)):
                if points[i] == points[j]:
                    count += 1
                    continue
                if i != j:

                    k = tan(points[i], points[j])
                    counter[k] = counter.get(k, 0) + 1

            for value in counter.values():
                if value >= count:
                    count = value + 1

        return count


ss = Solution()
print(ss.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))

