def merge(l1: list, l2: list) -> list:
    res = []

    while l1 and l2:
        if l1[0] <= l2[0]:
            res.append(l1.pop(0))
        else:
            res.append(l2.pop(0))

    res += l1 or l2

    return res


def merge_sort(nums: list) -> list:
    length = len(nums)

    if length <= 1:
        return nums

    return merge(merge_sort(nums[: length // 2]), merge_sort(nums[length // 2 :]))


if __name__ == "__main__":
    nums = [5, 8, 6, 3, 9, 2, 1, 7, 4]
    assert merge_sort(nums) == list(range(1, 10))
