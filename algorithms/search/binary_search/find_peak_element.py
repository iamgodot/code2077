# 峰值元素是指其值严格大于左右相邻值的元素。
# 给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
# 你可以假设 nums[-1] = nums[n] = -∞ 。
# 你必须实现时间复杂度为 O(log n) 的算法来解决此问题。


def find_peak(nums) -> int:
    """
    Whichever side shows a larger value, we split and apply binary search.
    Watch out for cases on both ends.
    """
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if (mid == 0 or nums[mid - 1] < nums[mid]) and (
            mid == len(nums) - 1 or nums[mid] > nums[mid + 1]
        ):
            return mid
        elif mid > 0 and nums[mid - 1] > nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == "__main__":
    assert find_peak([1, 2, 3, 1]) == 2
    assert find_peak([1, 2, 1, 3, 5, 6, 4]) == 5
    assert find_peak([1]) == 0
    assert find_peak([1, 2]) == 1
