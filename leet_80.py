
def removeDuplicates(nums):
    i, count = 1, 1

    while i < len(nums):
        if nums[i] == nums[i-1]:
            count += 1
            if count > 2:
                nums.pop(i)
                i -= 1
        else:
            count = 1
        i += 1

    return nums


print(removeDuplicates([1, 1, 1, 2, 3, 3, 3, 3]))