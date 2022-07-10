# 给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。


from typing import List


def find_max_length(nums: List[int]) -> int:
    """
    将 nums 中的 0 替换成 -1，问题则变成求和为 0 的连续子数组。
    Time: O(n)
    Space: O(n)
    """
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i] = -1

    hashtable = {0: -1}
    res = total = 0
    for i in range(len(nums)):
        total += nums[i]
        if total in hashtable:
            res = max(res, i - hashtable[total])
        else:
            hashtable[total] = i
    return res


if __name__ == "__main__":
    assert find_max_length([0, 1]) == 2
    assert find_max_length([0, 1, 0]) == 2
