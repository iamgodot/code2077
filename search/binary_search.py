# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
# 提示：
# 你可以假设 nums 中的所有元素是不重复的。
# n 将在 [1, 10000]之间。
# nums 的每个元素都将在 [-9999, 9999]之间。


# 二分查找法，时间复杂度 O(logn)，空间复杂度 O(1)
def search(nums: list, target: int) -> int:
    res = -1
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            res = mid

            break
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return res


if __name__ == '__main__':
    assert search([1, 2, 3], 3) == 2
    assert search([1, 2, 3], 0) == -1
    assert search([1, 2, 3, 4], 2) == 1
    assert search([-1, 0, 3, 5, 9, 12], 13) == -1
