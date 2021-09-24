# 给定两个数组，编写一个函数来计算它们的交集。
# 输出结果中的每个元素一定是唯一的。我们可以不考虑输出结果的顺序。


# 1. Use hashtable: 时间复杂度 O(min(m, n))，空间复杂度 O(m+n)
def intersection_with_set(nums1: list, nums2: list) -> list:
    set1, set2 = set(nums1), set(nums2)
    res = []

    if len(set1) > len(set2):
        set1, set2 = set2, set1

    for num in set1:
        if num in set2:
            res.append(num)

    return res


# 2. Sort and use two pointers: 时间复杂度 O(m*logm+n*logn)，空间复杂度 O(logm+logn)
def intersection_with_two_pointers(nums1: list, nums2: list) -> list:
    nums1.sort()
    nums2.sort()

    res = []
    i, j, cur = 0, 0, None

    while i < len(nums1) and j < len(nums2):
        m, n = nums1[i], nums2[j]

        if m == n and m != cur:
            res.append(m)
            cur = m
        elif m < n:
            i += 1
        else:
            j += 1

    return res


if __name__ == '__main__':
    for method in [intersection_with_set, intersection_with_two_pointers]:
        nums1, nums2 = [4, 9, 5], [9, 4, 9, 8, 4]
        res = method(nums1, nums2)
        assert sorted(res) == [4, 9], res
