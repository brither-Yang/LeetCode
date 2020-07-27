'''
11. 盛最多水的容器
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。
图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例：

输入：[1,8,6,2,5,4,8,3,7]
输出：49
'''


class Solution:
    def maxArea(self, height):
        i = 0
        j = len(height) - 1

        max_s = 0
        while i < j:
            h = min(height[i], height[j])
            w = j - i
            s = h * w
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
            if max_s < s:
                max_s = s
        return max_s

ss = Solution()
print(ss.maxArea([1,8,6,2,5,4,8,3,7]))


array = [1,8,6,2,5,4,8,3,7]
l = 0
r = len(array) - 1

max_s = 0
while l < r:
    s = (r - l) * min(array[r], array[l])
    if s > max_s:
        max_s = s
    if min(array[l], array[r]) == array[l]:
        l += 1
    else:
        r -= 1
print(max_s)