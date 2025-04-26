# Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/


def longest_consecutive(nums: list[int]) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    # NOTE: initialize set with all numbers
    hash_set = set(nums)
    res = 0
    for num in hash_set:  # NOTE: use hash_set to avoid duplicate elements
        if num - 1 not in hash_set:
            count = 1
            start = num
            while start + 1 in hash_set:
                count += 1
                start += 1
            res = max(res, count)
    return res


if __name__ == "__main__":
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
