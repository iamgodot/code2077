# 整数数组 nums 按升序排列，数组中的值 互不相同 。
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。


from typing import List


# 考虑每次二分的两部分，一定有一半是有序另一半不完全有序的
# 所以对于有序的一半，分成两种情况：
# 1. target 在有序的这一半中
# 2. target 在另外一半
def search(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        # NOTE: 这里把相等的情况单独列出来更好理解
        # 比如 [3, 1], 1 的情况
        elif nums[low] == nums[mid]:
            low = mid + 1
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


# 已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,4,4,5,6,7] 在变化后可能得到：
# 若旋转 4 次，则可以得到 [4,5,6,7,0,1,4]
# 若旋转 7 次，则可以得到 [0,1,4,4,5,6,7]
# 注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。

# 给你一个可能存在 重复 元素值的数组 nums，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。


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
