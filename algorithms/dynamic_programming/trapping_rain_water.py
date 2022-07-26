# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。


from typing import List


def trap(height: List[int]) -> int:
    """
    动态规划：
    1. 对于每个元素来说，雨水增量等于左右最大高度的最小值减去当前高度。
    2. 如果在每个位置都重新扫描左右两边的话总体复杂度为 O(n^2)。
    3. 可以用两个数组记录每个位置的左右最大高度集合。

    Time: O(n)
    Space: O(n)
    """
    length = len(height)
    max_left, max_right = [0] * length, [0] * length
    for i in range(length):
        if i > 0:
            max_left[i] = max(max_left[i - 1], height[i])
        else:
            max_left[i] = height[i]
    for i in range(length - 1, -1, -1):
        if i < length - 1:
            max_right[i] = max(max_right[i + 1], height[i])
        else:
            max_right[i] = height[i]
    res = 0
    for i in range(length):
        res += min(max_left[i], max_right[i]) - height[i]
    return res


def trap2(height: List[int]) -> int:
    """
    双指针：
    1. 在扫描过程中，用两个变量维护每个位置的左右最大值集合。
    2. 如果 max_left 小于 max_right，那么左右两边最大值的较小者一定是 max_left
        所以左指针右移，然后比较 max_left 与 height[i] 决定 res 的增量。
    3. 反之则可以确定 max_right 的值。

    注意对于 height 为空的情况要单独判断。

    Time: O(n)
    Space: O(1)
    """
    if not height:
        return 0
    res = 0
    i, j = 0, len(height) - 1
    max_left, max_right = height[i], height[j]

    while i < j:
        if max_left < max_right:
            i += 1
            max_left = max(max_left, height[i])
            res += max_left - height[i]
        else:
            j -= 1
            max_right = max(max_right, height[j])
            res += max_right - height[j]
    return res


if __name__ == "__main__":
    for func in trap, trap2:
        assert func([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
