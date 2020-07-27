import numpy as np


def backet(value_list, weight_list, total_weight):

    # 考虑从 [0, index] 物品填充背包的最大价值
    def best_value(v, w, index, c):
        assert len(v) == len(w)

        if index < 0 or c <= 0:
            return 0
        if dp[index][c] != -1:
            return dp[index][c]
        res = max(best_value(v, w, index-1, c), v[index] + best_value(v, w, index-1, c-w[index]))
        dp[index][c] = res

        return res

    n = len(weight_list)
    dp = [[-1 for _ in range(total_weight+1)] for _ in range(n)]
    return best_value(value_list, weight_list, n-1, total_weight)


# 2*C 的空间复杂度
def backet1(value_list, weight_list, total_weight):
    assert len(weight_list) == len(value_list)

    n = len(weight_list)
    if n == 0:
        return 0

    dp = [[-1 for _ in range(total_weight+1)] for _ in range(2)]

    for i in range(total_weight+1):
        dp[0][i] = value_list[0] if i >= weight_list[0] else 0

    for i in range(1, n):
        for j in range(total_weight+1):

            dp[i%2][j] = dp[(i-1)%2][j]
            if j >= weight_list[i]:
                dp[i%2][j] = max(dp[(i-1)%2][j], value_list[i] + dp[(i-1)%2][j - weight_list[i]])
    return dp[(n-1)%2][total_weight]


# C 的空间复杂度
def backet2(value_list, weight_list, total_weight):
    assert len(weight_list) == len(value_list)

    n = len(weight_list)
    if n == 0:
        return 0

    dp = [-1 for _ in range(total_weight+1)]

    for i in range(total_weight+1):
        dp[i] = value_list[0] if i >= weight_list[0] else 0

    for i in range(1, n):
        for j in range(total_weight, weight_list[i]-1, -1):
            dp[j] = max(dp[j-2], value_list[i] + dp[j - weight_list[i]])

    return dp[total_weight]


print(backet1([6, 10, 12], [1, 2, 3], 5))


# 解题思路
# 常见的背包问题有1、组合问题。2、True、False问题。3、最大最小问题。

# 我在大神整理的基础上，又做了细分的整理。分为三类。

# 1、组合问题：
# 377. 组合总和 Ⅳ
# 494. 目标和
# 518. 零钱兑换 II

# 2、True、False问题：
# 139. 单词拆分
# 416. 分割等和子集

# 3、最大最小问题：
# 474. 一和零
# 322. 零钱兑换
#
# 组合问题公式: dp[i] += dp[i-num]
# True、False问题公式: dp[i] = dp[i] or dp[i-num]
# 最大最小问题公式: dp[i] = min(dp[i], dp[i-num]+1)或者dp[i] = max(dp[i], dp[i-num]+1)
# 以上三组公式是解决对应问题的核心公式。
#
# 当然拿到问题后，需要做到以下几个步骤：
# 1.分析是否为背包问题。
# 2.是以上三种背包问题中的哪一种。
# 3.是0-1背包问题还是完全背包问题。也就是题目给的nums数组中的元素是否可以重复使用。
# 4.如果是组合问题，是否需要考虑元素之间的顺序。需要考虑顺序有顺序的解法，不需要考虑顺序又有对应的解法。
#
# 接下来讲一下背包问题的判定
# 背包问题具备的特征：给定一个target，target可以是数字也可以是字符串，
# 再给定一个数组nums，nums中装的可能是数字，也可能是字符串，
# 问：能否使用nums中的元素做各种排列组合得到target。
#
# 背包问题技巧：

nums = [1, 2, 3]
target = 4

# 1.如果是0-1背包，即数组中的元素不可重复使用，nums放在外循环，target在内循环，且内循环倒序；
dp = [0 for _ in range(target+1)]
for num in nums:
    for i in range(target, num-1, -1):
        dp[i] += dp[i-num]

# 2.如果是完全背包，即数组中的元素可重复使用，nums放在外循环，target在内循环。且内循环正序。
for num in nums:
    for i in range(num, target+1):
        pass

# 3.如果组合问题需考虑元素之间的顺序，需将target放在外循环，将nums放在内循环。
for i in range(1, target+1):
    for num in nums:
        pass


class Solution:
    def combinationSum4(self, nums, target):
        if not nums:
            return 0
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(1,target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        return dp[target]

'''
如果是0-1背包，即数组中的元素不可重复使用，nums放在外循环，
target在内循环，且内循环倒序； 因为顺着nums遍历可以做到选和不选，
过了num就与下一个num无关了，因此nums在外循环， 内循环倒序是因为倒序更新第c个值时，
前面的第c-num的状态是未选择当前num的状态，从前往后更新不知道前面的状态是否选了num。

如果是完全背包，数组中的元素可以重复出现，此时nums放在外层循环是为了方便递归，
其实完全背包nums在外循环或内循环均可，nums放在外层可以避免target重复调用，
但target必须正序遍历。完全背包的目的一般是求最值。

如果是组合背包，数组中的元素可以重复出现但顺序可以不一致，
此时nums放在内循环，target放在外循环，正序遍历，
因为这样dp的每个状态更新时都不用考虑前面的状态是否选择了第i个num。
组合背包的问题一般是求组合个数。
'''


