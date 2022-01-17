# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 如果数组中不存在目标值 target，返回 [-1, -1]。
# 进阶：
# 你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？


def search(nums: list, target: int) -> list:
    """
    通过 x <= target 查找右侧外界
    通过 x >= target 查找左侧外界
    """
    if not nums:
        return [-1, -1]

    length = len(nums)
    i = j = 0  # 这里初始化值不会影响结果
    left, right = 0, length - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1

    j = left
    # 如果不满足条件则提前返回
    if j < 0 or nums[j - 1] != target:
        return [-1, -1]

    left = 0  # right 此时已经是右侧内界了，不用更新，还缩小了查询范围
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    i = right

    return [i + 1, j - 1]


if __name__ == "__main__":
    assert search([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert search([1], 1) == [0, 0]
    assert search([], 0) == [-1, -1]
