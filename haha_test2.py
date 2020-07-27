def Solution(nums):


    def track(target, sets):
        if len(sets) == 1 and target in sets:
            return res.append(True)
        elif len(sets) == 1 and target not in sets:
            return
        else:
            for i in sets[0]:
                track(target-i, sets[1:])

    res = []
    track(2018, nums)
    if True in res:
        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':

    nums = [[200, -90, 90],
            [18, 680, 2000],
            [21, 1800, 18],
            [10, -100, 0],
            [396, 0, -856]]

    print(Solution(nums))