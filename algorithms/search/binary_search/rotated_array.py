# Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/


def search(nums: list[int], target: int) -> int:
    """
    For the two halves every time, there's must be one sorted half and one unsorted. So we will search in both of them.
    """
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        # NOTE: 这里把相等的情况单独列出来更好理解
        # 比如 [3, 1], 1 的情况
        # FIXME: 不能是 right = mid - 1，因为此时 low 已经等于 mid，我们应当尝试右边的元素，已经没可能再往左了
        elif nums[low] == nums[mid]:
            low = mid + 1
        # NOTE: we can also merge the above case here
        # because when nums[low] equals nums[mid], it
        # can also be seen as the left half is sorted
        # elif nums[low] <= nums[mid]:
        elif nums[low] < nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


# Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/


def find_min(nums) -> int:
    """
    It's better to compare nums[right] with nums[mid] since the logic is identical
    for both all-sorted case and half-sorted case, meaning should take left half
    when mid < right whether for case like [0, 1, 2] or [4, 0, 1, 2, 3].

    If use nums[left], we have to diff two cases because when nums[left] < nums[mid]:
        for all-sorted case: take left half.
        for half-sorted case: take right half.

    It doesn't matter which condition adopts the equal case.
    """
    res = nums[0]
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        res = min(res, nums[mid])
        if nums[mid] <= nums[right]:
            right = mid - 1
        else:
            left = mid + 1
    return res


if __name__ == "__main__":
    assert find_min([1, 3, 5]) == 1
    assert find_min([2, 2, 2, 0, 1]) == 0
