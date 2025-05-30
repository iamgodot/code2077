# Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/description/

# NOTE: for every position, the units of water is the minimum of its left and right maximum minus its own height


def trap(height: list[int]) -> int:
    """
    For every position, the most possibile water is the minimum of both left and right maximum height minus its own height.

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


def trap2(height: list[int]) -> int:
    """
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
            # NOTE: if we don't update max_left first, here the subtraction needs to be checked as positive
            res += max_left - height[i]
        else:
            j -= 1
            max_right = max(max_right, height[j])
            res += max_right - height[j]
    return res


if __name__ == "__main__":
    for func in trap, trap2:
        assert func([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
