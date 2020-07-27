'''
二分查找法：对于有序系列
'''


def binary_search(array, target):

    n = len(array)
    # 在 [l, r] 区间中寻找 target
    l = 0
    r = n - 1

    while l <= r:   # 当 l == r 时，区间依然有效
        mid = int((l + r) / 2)         # l + (r - l) / 2
        if array[mid] == target:
            return array[mid]
        elif array[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))
