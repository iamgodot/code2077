def merge(nums1: list, nums2: list) -> list:
    res = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            res.append(nums1[i])
            i += 1
        else:
            res.append(nums2[j])
            j += 1

    res += nums1[i:] or nums2[j:]

    return res


def merge_sort(nums: list) -> list:
    length = len(nums)

    if length <= 1:
        return nums

    mid = length // 2
    nums1 = merge_sort(nums[:mid])
    nums2 = merge_sort(nums[mid:])
    return merge(nums1, nums2)


if __name__ == "__main__":
    assert merge_sort([5, 8, 6, 3, 9, 2, 1, 7, 4]) == list(range(1, 10))
