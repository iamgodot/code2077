# Jump Game
# https://leetcode.com/problems/jump-game/description/


def can_jump(nums: list[int]) -> bool:
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


# Jump Game II
# https://leetcode.com/problems/jump-game-ii/description/


def jump(nums: list[int]) -> int:
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


def jump2(nums: list[int]) -> int:
    jumps = pos = 0
    length = len(nums)
    while pos < length - 1:
        jumps += 1
        if pos + nums[pos] >= length - 1:
            break
        reach = 0
        for i in range(pos + 1, pos + nums[pos] + 1):
            distance = i + nums[i]
            if distance > reach:
                pos = i
                reach = distance
    return jumps


if __name__ == "__main__":
    assert can_jump([2, 3, 1, 1, 4]) is True
    assert can_jump([3, 2, 1, 0, 4]) is False
    assert jump([2, 3, 1, 1, 4]) == 2
    assert jump([2, 3, 0, 1, 4]) == 2
