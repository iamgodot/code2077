# 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个下标。

from typing import List


def can_jump(nums: List[int]) -> bool:
    """
    Iterate through nums:
        For each element, if it can be reached,
        update max cover value, otherwise return False.
    """
    cover = 0
    for i in range(len(nums)):
        if cover < i:
            return False
        cover = max(cover, i + nums[i])

    return True


# 给你一个非负整数数组 nums ，你最初位于数组的第一个位置。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
# 假设你总是可以到达数组的最后一个位置。


def jump(nums: List[int]) -> int:
    """
    前提条件是总是可以到达数组的重点。
    那么只需要在可行的情况下跳最远的距离即可，
    也就是在当前最长范围的边界做判断，如果没到终点，则增加一步，否则直接返回。
    """
    res = cover = cur = 0
    for i in range(len(nums)):
        cover = max(cover, i + nums[i])
        if i == cur:
            if i == len(nums) - 1:
                break
            res += 1
            cur = cover

    return res


if __name__ == "__main__":
    assert can_jump([2, 3, 1, 1, 4]) is True
    assert can_jump([3, 2, 1, 0, 4]) is False
    assert jump([2, 3, 1, 1, 4]) == 2
    assert jump([2, 3, 0, 1, 4]) == 2
