# Subarray Sums Divisible by K
# https://leetcode.com/problems/subarray-sums-divisible-by-k/


def find_subarrays(nums: list[int], k: int) -> int:
    """
    Time: O(n)
    Space: O(min(n, k))
    """
    from collections import defaultdict

    hashtable = defaultdict(int, {0: 1})
    res = remain = 0
    for num in nums:
        remain = (remain + num) % k
        res += hashtable.get(remain, 0)
        hashtable[remain] += 1
    return res


if __name__ == "__main__":
    assert find_subarrays([4, 5, 0, -2, -3, 1], 5) == 7
    assert find_subarrays([5], 9) == 0
