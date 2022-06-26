# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 如果数组中不存在目标值 target，返回 [-1, -1]。
# 进阶：
# 你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？


def search(nums: list, target: int) -> list:
    """
    通过 x <= target 查找右侧外界
    通过 x >= target 查找左侧外界
    """

    def bisect_left(nums, target) -> int:
        i, j = 0, len(nums)
        while i < j:
            mid = (i + j) // 2
            if target <= nums[mid]:
                j = mid
            else:
                i = mid + 1
        return i

    def bisect_right(nums, target) -> int:
        i, j = 0, len(nums)
        while i < j:
            mid = (i + j) // 2
            if target >= nums[mid]:
                i = mid + 1
            else:
                j = mid
        return i - 1

    bound_left = bisect_left(nums, target)
    length = len(nums)
    if bound_left > length - 1 or nums[bound_left] != target:
        return [-1, -1]
    bound_right = bisect_right(nums, target)
    return [bound_left, bound_right]


if __name__ == "__main__":
    assert search([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert search([1], 1) == [0, 0]
    assert search([1], 2) == [-1, -1]
    assert search([], 0) == [-1, -1]
